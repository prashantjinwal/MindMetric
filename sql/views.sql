CREATE OR REPLACE VIEW neighborhood_accessibility_summary AS
SELECT
    n.id AS neighborhood_id,
    n.name AS neighborhood_name,
    n.population,
    s.healthcare_score,
    s.education_score,
    s.grocery_score,
    s.transport_score,
    s.recreation_score,
    s.overall_score
FROM neighborhoods AS n
LEFT JOIN accessibility_scores AS s
    ON n.id = s.neighborhood_id;

CREATE OR REPLACE VIEW service_accessibility_summary AS
SELECT
    service_id,
    COUNT(*) AS evaluated_neighborhoods,
    COUNT(*) FILTER (WHERE accessible) AS accessible_neighborhoods,
    AVG(travel_time_minutes) AS avg_travel_time_minutes
FROM accessibility
GROUP BY service_id;
