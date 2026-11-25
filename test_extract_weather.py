from extract_weather import build_records

def test_missing_precipitation():

	sample_data = {
        	"hourly": {
                	"time": ["2026-11-24T00:00"],
                	"temperature_2m": [5.0],
                	"precipitation": [None],
        	}
	}

	records = build_records(sample_data)
	assert len(records) == 1
	assert records[0]["precipitation_mm"] is None

def test_missing_temperature():

        sample_data = {
                "hourly": {
                        "time": ["2026-11-24T00:00"],
                        "temperature_2m": [None],
                        "precipitation": [0.0],
                }
        }

        records = build_records(sample_data)
        assert records == []

def test_valid_record():
        sample_data = {
                "hourly": {
                        "time": ["2026-11-24T00:00"],
                        "temperature_2m": [5.0],
                        "precipitation": [0.0],
                }
        }

        records = build_records(sample_data)
        assert records == [
    		{
        		"timestamp": "2026-11-24T00:00",
        		"temperature_c": 5.0,
        		"precipitation_mm": 0.0,
    		}
	]
