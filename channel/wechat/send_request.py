import requests
import json

def send_message_to_server(message):
    # URL of your Flask application
    url = "http://43.163.242.45:80/"# Adjust if your app is running on a different host or port
#    url = "http://127.0.0.1:80"

    # Prepare the JSON payload with the message
    payload = json.dumps({
        "message": message
    })

    # Set headers to indicate that we're sending JSON
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        # Send the POST request and wait for the response
        response = requests.post(url, headers=headers, data=payload)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse the JSON response and print the result
            response_data = response.json()
            print("Response from server:", response_data.get("response"))
            return response_data.get("response")
        else:
            # Handle HTTP errors (e.g., 404, 500)
            print("Failed to get a successful response from server, status code:", response.status_code)
            print("Response content:", response.text)
            return "对不起，我没有找到答案"
            
    except requests.exceptions.RequestException as e:
        # Handle errors that occur during the request sending process
        # (e.g., network errors, invalid URL)
        print("An error occurred while sending the request:", str(e))
        return "对不起，我没有找到答案"

# Example usage
if __name__ == "__main__":
    message = "Tell me a joke."
    send_message_to_server(message)
