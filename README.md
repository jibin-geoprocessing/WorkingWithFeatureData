# WorkingWithFeatureData
This repo contains demos (python scripts and Jupyter Notebook) and data for the *Working with Feature Data* technical session. This presentation was given at the Esri 2018 Developer Summit in Palm Springs.

# Prerequisite
ArcGIS Desktop (any of the following):
- (Recommended) ArcGIS Pro 2.0 or later. These versions of ArcGIS Pro have jupyter notebook pre-installed
- ArcGIS Pro 1.4 or below, or ArcMap 10.2 or later. Install `Jupyter Notebook` as below

# Install Jupyter Notebook
- For ArcGIS Pro 1.4 or below:
```
pip3 install --upgrade pip
pip3 install jupyter
```

- For ArcMap 10.2 or later:
```
pip install --upgrade pip
pip install jupyter
```


# About the data
- The crash data and data dictionary can be retrieved from [Maryland Open Data Portal](https://data.maryland.gov/browse?q=Maryland+Statewide+Vehicle+Crashes&sortBy=relevance&utf8=&page=1). In this demo, we use `"Maryland Statewide Vehicle Crashes: CY2017 Quarter 4"` data.
- The road network data can be retrieved from [Maryland's GIS Data Catalog](http://data.imap.maryland.gov/datasets/maryland-annual-average-daily-traffic-annual-average-daily-traffic-sha-statewide-aadt-lines?geometry=-86.553%2C37.336%2C-67.986%2C40.331)

Once the data is downloaded, run demo_setup.py to setup for subsequent demos.

# Licensing
Copyright 2018 Esri

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

A copy of the license is available in the repository's [LICENSE](https://github.com/jibin-geoprocessing/WorkingWithFeatureData/blob/master/LICENSE) file.
