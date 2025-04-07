CREATE DATABASE airflow;
CREATE DATABASE weather;

\c weather;

CREATE TABLE raw_data (
    id SERIAL PRIMARY KEY,
    year VARCHAR(4),
    month VARCHAR(2),
    day VARCHAR(2),
    temperature_avg_f VARCHAR(10),
	humidity_percent VARCHAR(10),
	wind_speed_avg_mph VARCHAR(10),
    processed BOOLEAN DEFAULT FALSE
);

CREATE TABLE processed_data (
    id SERIAL PRIMARY KEY,        
    year INT,            
    month INT,             
    day INT,
	season INT,
    temperature_avg_f FLOAT,
	humidity_percent FLOAT,
	wind_speed_avg_mph FLOAT
);
