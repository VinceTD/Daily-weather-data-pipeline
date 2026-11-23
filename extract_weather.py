import requests

def main():
	URL = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": 41.8827,
		"longitude": -87.6233,
		"hourly": "temperature_2m",
	}
	print("Starting Chicago weather extraction")
	response = requests.get(URL, timeout=30, params=params)
	response.raise_for_status()
	print(response.status_code)
	data = response.json()
	hourly = data["hourly"]
	timestamp = hourly["time"][0]
	temperature = hourly["temperature_2m"][0]
	record = {
		"timestamp": timestamp,
		"temperature_c": temperature,
		}
	print(record)

if __name__ == "__main__":
	main()
