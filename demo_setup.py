"""
This script is used for demo setup. It includes the following processes:
1. clean up the workspace geodatabase
2. transform crash data from excel table to feature class
2. break down road data into multiple parts by county_id, and stored in scratch
   workspace.
"""

import arcpy
import os


def clean_up_geodatabase(gdb):
    """ remove all data from the input gdb """
    # if gdb not exist, create one and return
    if not arcpy.Exists(gdb):
        dirname, gdbname = os.path.dirname(gdb), os.path.basename(gdb).split('.')[0]
        arcpy.management.CreateFileGDB(dirname, gdbname)
        return

    # gdb exists, remove all contents
    for dirpath, dirname, filenames in arcpy.da.Walk(gdb):
        for filename in filenames:
            feature = os.path.join(dirpath, filename)
            try:
                arcpy.management.Delete(feature)
            except arcpy.ExecuteError as e:
                print('Delete {} failed... ({})'.format(filename, e))


def split_road_data(road_shapefile, scratchGDB):
    """
    1. clean up scratchGDB
    2. import road shapefile as feature class
    3. split input road shapefile by county_id, and stored in scratch gdb
    4. rename outputs as "county_{id}"
    """
    clean_up_geodatabase(scratchGDB)

    road = arcpy.conversion.FeatureClassToFeatureClass(road_shapefile,
                                                       scratchGDB,
                                                       'road')[0]
    arcpy.analysis.SplitByAttributes(road, scratchGDB, "COUNTY_ID")

    # rename features
    for dirpath, dirname, filenames in arcpy.da.Walk(scratchGDB):
        for filename in filenames:
            if filename.startswith('T'):  # splitted data filename starts with T
                feature = os.path.join(dirpath, filename)
                new_name = 'county_{}'.format(filename[1:])
                arcpy.management.Rename(feature, new_name)

    # delete the road data
    try:
        arcpy.management.Delete(road)
    except arcpy.ExecuteError as e:
        print('Delete road data failed... ({})'.format(e))


def demo_setup():
    arcpy.env.workspace = '.\\WorkingWithFeatureData.gdb'
    arcpy.env.scratchWorkspace = '.\\scratch.gdb'
    arcpy.env.overwriteOutput = True
    data_folder = '.\\data'

    clean_up_geodatabase(arcpy.env.workspace)
    input_table = os.path.join(data_folder, 'Crash_Qtr04_2017.xlsx', 'CRASH$')
    arcpy.management.XYTableToPoint(input_table, 'crash', 'LONGITUDE', 'LATITUDE')

    shapefile = 'Maryland_Annual_Average_Daily_Traffic__Annual_Average_Daily_Traffic_SHA_Statewide_AADT_Lines.shp'
    split_road_data(os.path.join(data_folder, shapefile), arcpy.env.scratchGDB)


if __name__ == '__main__':
    demo_setup()
