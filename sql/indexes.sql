CREATE INDEX IF NOT EXISTS idx_neighborhoods_geometry
    ON neighborhoods USING GIST (geometry);

CREATE INDEX IF NOT EXISTS idx_services_geometry
    ON services USING GIST (geometry);

CREATE INDEX IF NOT EXISTS idx_services_service_type
    ON services (service_type);

CREATE INDEX IF NOT EXISTS idx_transit_stations_geometry
    ON transit_stations USING GIST (geometry);

CREATE INDEX IF NOT EXISTS idx_accessibility_neighborhood_id
    ON accessibility (neighborhood_id);

CREATE INDEX IF NOT EXISTS idx_accessibility_service_id
    ON accessibility (service_id);

CREATE INDEX IF NOT EXISTS idx_accessibility_accessible
    ON accessibility (accessible);
