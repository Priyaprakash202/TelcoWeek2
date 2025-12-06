import requests
import json

url2 = "https://api.open-meteo.com/v1/forecast?latitude=13.3347&longitude=74.7462&hourly=temperature_2m"

def main():
    response = requests.get(url2)
    response.raise_for_status()
    data = response.json()

    # Save to file
    with open("data2.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Location 2 Data Saved to data2.json")
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
