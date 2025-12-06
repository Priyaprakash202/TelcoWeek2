import requests
import json

def call_api(api_url):
    try:
        response = requests.get(api_url)

        # Print status code
        print("Status Code:", response.status_code)

        # Check for success (200 OK)
        if response.status_code == 200:
            print("Success: Valid API key")

        # Check for unauthorized (401)
        elif response.status_code == 401:
            print("Error: Invalid API key")

        # Try to parse json safely
        try:
            data = response.json()
            print("\nJSON Response:")
            print(json.dumps(data, indent=4))
        except json.JSONDecodeError:
            print("Response is not valid JSON")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)


if __name__ == "__main__":
    # Correct key
    url = "http://api.ipapi.com/api/161.185.160.93?access_key=7988817e94631d739259b6dfb8b0209d"

    # For testing wrong key:
    #url = "http://api.ipapi.com/api/161.185.160.93?access_key=wrongkey123"

    call_api(url)
