import requests
import json

api_url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/btc.json"
output_file_path = "data/btc_data.json"

try:
    # Make the API request
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    # Parse the JSON response
    data = response.json()

    # Save the JSON data to a file
    with open(output_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Data saved to {output_file_path}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
