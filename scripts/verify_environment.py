"""Verify the UrbanPulse Python environment."""

from __future__ import annotations

from importlib import metadata

PACKAGES = {
    "pandas": "pandas",
    "geopandas": "geopandas",
    "shapely": "shapely",
    "pyproj": "pyproj",
    "osmnx": "osmnx",
    "networkx": "networkx",
    "folium": "folium",
    "sqlalchemy": "SQLAlchemy",
    "psycopg": "psycopg",
    "geoalchemy2": "GeoAlchemy2",
    "plotly": "plotly",
    "jupyter": "jupyter",
    "pytest": "pytest",
}


def main() -> None:
    for import_name, distribution_name in PACKAGES.items():
        __import__(import_name)
        version = metadata.version(distribution_name)
        print(f"{import_name}: {version}")


if __name__ == "__main__":
    main()
