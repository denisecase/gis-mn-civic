from pathlib import Path
import pandas as pd
import geopandas as gpd
import folium
from IPython.display import display

DATA_DIR = Path("data")

LAYER_FILES = {
    "precincts": "Voting_Precincts2C_MN.geojson",
    "polling": "Polling_Places2C_MN.geojson",
    "schools": "School_Districts2C_MN.geojson",
    "mcd": "Minor_Civil_Divisions,_Saint_Louis_County,_MN.geojson",
    "county": "County_Boundary2C_MN.geojson",
}


def display_map(county_key, layer_key):
    county_path = DATA_DIR / county_key
    layer_file = county_path / LAYER_FILES[layer_key]

    if not layer_file.exists():
        print(f"Layer file not found: {layer_file}")
        return

    gdf = gpd.read_file(layer_file)

    # Filter out rows with missing or invalid geometry
    gdf = gdf[gdf.geometry.notnull() & gdf.is_valid]

    if gdf.empty:
        print("No valid geometries to display.")
        return

    centroid = gdf.geometry.unary_union.centroid
    m = folium.Map(location=[centroid.y, centroid.x], zoom_start=8)

    # Use tooltip column
    preferred_fields = ["NAME"]
    tooltip_field = next(
        (f for f in preferred_fields if f in gdf.columns), gdf.columns[0]
    )

    folium.GeoJson(gdf, tooltip=folium.GeoJsonTooltip(fields=[tooltip_field])).add_to(m)

    display(m)


def display_map_mcd(county_key):
    county_path = DATA_DIR / county_key
    layer_file = county_path / LAYER_FILES["mcd"]

    if not layer_file.exists():
        print(f"MCD layer not found: {layer_file}")
        return

    gdf = gpd.read_file(layer_file)

    # Ensure valid polygonal geometry only
    valid_geom_types = ["Polygon", "MultiPolygon"]
    gdf = gdf[
        gdf.geometry.notnull()
        & gdf.is_valid
        & gdf.geometry.geom_type.isin(valid_geom_types)
    ]

    if gdf.empty:
        print("No valid MCD geometries to display.")
        return

    # Drop or convert non-serializable columns
    for col in gdf.columns:
        if (
            gdf[col].dtype == "datetime64[ns]"
            or gdf[col].apply(lambda x: isinstance(x, pd.Timestamp)).any()
        ):
            gdf[col] = gdf[col].astype(str)

    # Compute centroid
    centroid = gdf.geometry.unary_union.centroid
    m = folium.Map(location=[centroid.y, centroid.x], zoom_start=8)

    # Tooltip field
    preferred_fields = ["MCD_NAME", "TSHIP_NAME", "Muni_Name", "NAME"]
    tooltip_field = next(
        (f for f in preferred_fields if f in gdf.columns), gdf.columns[0]
    )

    folium.GeoJson(gdf, tooltip=folium.GeoJsonTooltip(fields=[tooltip_field])).add_to(m)

    display(m)
