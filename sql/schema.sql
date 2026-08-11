CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS neighborhoods (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    population INTEGER CHECK (population IS NULL OR population >= 0),
    geometry geometry(MultiPolygon, 4326) NOT NULL
);

CREATE TABLE IF NOT EXISTS services (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    service_type TEXT NOT NULL CHECK (
        service_type IN (
            'hospital',
            'school',
            'grocery',
            'park',
            'transit'
        )
    ),
    geometry geometry(Point, 4326) NOT NULL
);

CREATE TABLE IF NOT EXISTS transit_stations (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    line TEXT,
    geometry geometry(Point, 4326) NOT NULL
);

CREATE TABLE IF NOT EXISTS accessibility (
    id BIGSERIAL PRIMARY KEY,
    neighborhood_id BIGINT NOT NULL REFERENCES neighborhoods (id),
    service_id BIGINT NOT NULL REFERENCES services (id),
    travel_time_minutes NUMERIC(6, 2) CHECK (
        travel_time_minutes IS NULL OR travel_time_minutes >= 0
    ),
    accessible BOOLEAN NOT NULL,
    UNIQUE (neighborhood_id, service_id)
);

CREATE TABLE IF NOT EXISTS accessibility_scores (
    neighborhood_id BIGINT PRIMARY KEY REFERENCES neighborhoods (id),
    healthcare_score NUMERIC(5, 2) CHECK (
        healthcare_score IS NULL OR healthcare_score BETWEEN 0 AND 100
    ),
    education_score NUMERIC(5, 2) CHECK (
        education_score IS NULL OR education_score BETWEEN 0 AND 100
    ),
    grocery_score NUMERIC(5, 2) CHECK (
        grocery_score IS NULL OR grocery_score BETWEEN 0 AND 100
    ),
    transport_score NUMERIC(5, 2) CHECK (
        transport_score IS NULL OR transport_score BETWEEN 0 AND 100
    ),
    recreation_score NUMERIC(5, 2) CHECK (
        recreation_score IS NULL OR recreation_score BETWEEN 0 AND 100
    ),
    overall_score NUMERIC(5, 2) CHECK (
        overall_score IS NULL OR overall_score BETWEEN 0 AND 100
    )
);
