# Architecture

UrbanPulse is planned as a straightforward analytics pipeline, with Python as the primary analytics language and PostgreSQL/PostGIS as the spatial database.

## Planned Pipeline

Data Sources -> Data Ingestion -> Data Cleaning -> Geospatial Processing -> PostgreSQL/PostGIS -> Spatial/Network Analysis -> Accessibility Metrics -> Business Insights -> Power BI / Web Dashboard

## Directory Responsibilities

- `data/raw/`: Original downloaded or collected datasets, separated by source domain. Raw files should not be committed.
- `data/processed/`: Cleaned, transformed, or analysis-ready datasets. Processed files should not be committed unless a small metadata artifact is intentionally added later.
- `data/external/`: Reference data from external systems that does not fit the raw/processed split.
- `notebooks/`: Exploratory and narrative analysis notebooks. Notebooks should call reusable code from `src/` instead of holding core logic.
- `src/`: Reusable Python source code for ingestion, cleaning, geospatial processing, analytics, database access, and shared utilities.
- `sql/`: PostGIS schema, indexes, views, and future analysis query files.
- `backend/`: Placeholder for a future FastAPI service. The API is not implemented during initial setup.
- `frontend/`: Placeholder for a future React + TypeScript interactive frontend.
- `powerbi/`: Power BI dashboard files, exports, and related documentation.
- `tests/`: Pytest-based checks for reusable Python modules.
- `docs/`: Architecture, methodology, and data dictionary documentation.
