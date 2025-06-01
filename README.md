# Minnesota GIS Boundaries

[![Launch Minnesota GIS Boundaries](https://img.shields.io/badge/Launch-Life_Expectancy_Compare-blue?logo=binder)](https://mybinder.org/v2/gh/denisecase/mn-gis-boundaries/HEAD?urlpath=voila%2Frender%2Fnotebooks%2Fmain.ipynb)

> Explore public geographic boundary data for Minnesota counties, including precincts, polling places, school districts, and county borders. 

Data is derived from official sources such as the Minnesota Secretary of State and Minnesota county GIS portals.
Currently **St. Louis County** data is available. 

## Structure

- `data/`: One folder per county, containing `.geojson` files
- Each county folder includes a `metadata.json` with source information

## License

All data in this repository is made available under the **Open Database License (ODbL) v1.0**.

> Contains data derived from the Minnesota Secretary of State and Minnesota county GIS sources, reorganized and published under the Open Database License.

## Sources

- [MN Secretary of State](https://www.sos.state.mn.us/)
- [St. Louis County GIS](https://gis.stlouiscountymn.gov/)
- [St. Louis County GIS Open Data Hub](https://open-data-slcgis.hub.arcgis.com/search?tags=administrative%2520boundaries)

Files have been subset by county in the `.geojson` format.  
**No geometry or feature content has been altered.**  
Refer to the official sites for the most current and authoritative versions.

## St. Louis County GIS Sources

- [Voting Precincts](https://open-data-slcgis.hub.arcgis.com/maps/b9bf94e80d994aaba6eeb8e6995e7bf8)
- [Polling Places](https://open-data-slcgis.hub.arcgis.com/maps/cc8f2caab4bc45629563f6d8198c6746)
- [County Boundary](https://open-data-slcgis.hub.arcgis.com/maps/038b4dede892458484b1ea1faa5df354)
- [School Districts](https://open-data-slcgis.hub.arcgis.com/maps/25a498c7b85a44bf8af238139fb8fe2e)
- [Civil Divisions](https://open-data-slcgis.hub.arcgis.com/maps/1d21431d0ea9423cbcc6cffb56e29c8a)
- [Commissioner Districts](https://open-data-slcgis.hub.arcgis.com/maps/2d43c4be95eb40dfaa4b3313e56397a8)
