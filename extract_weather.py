import requests

def main():
	URL = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": 41.8827,
		"longitude": -87.6233,
		"hourly": "temperature_2m",
		"forecast_days": 1,
	}
	print("Starting Chicago weather extraction")
	response = requests.get(URL, timeout=30, params=params)
	response.raise_for_status()
	print(response.status_code)
	data = response.json()
	hourly = data["hourly"]
	timestamps = hourly["time"]
	temperatures = hourly["temperature_2m"]
	
	records = []
	for timestamp, temperature in zip(timestamps, temperatures, strict=True):
	
		record = {
			"timestamp": timestamp,
			"temperature_c": temperature,
			}
		records.append(record)
	print(len(records))

if __name__ == "__main__":
	main()
