import requests

def main():
	URL = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": 41.8827,
		"longitude": -87.6233,
		"hourly": "temperature_2m,precipitation",
		"forecast_days": 1,
		"timezone": "UTC",
		"temperature_unit": "celsius",
		"precipitation_unit": "mm",
	}
	print("Starting Chicago weather extraction")
	response = requests.get(URL, timeout=30, params=params)
	response.raise_for_status()
	print(response.status_code)
	data = response.json()
	print(data["hourly_units"])
	hourly = data["hourly"]
	timestamps = hourly["time"]
	temperatures = hourly["temperature_2m"]
	precipitations = hourly["precipitation"]
	
	records = []
	for timestamp, temperature, precipitation in zip(timestamps, temperatures, precipitations, strict=True):
	
		record = {
			"timestamp": timestamp,
			"temperature_c": temperature,
			"precipitation_mm": precipitation,
			}
		records.append(record)
	print(len(records))
	print(records[0])

if __name__ == "__main__":
	main()
