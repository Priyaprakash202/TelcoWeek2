import requests

def main():
    url = "https://api.nationalize.io?name=priya"

    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

if __name__ == "__main__":
    main()
