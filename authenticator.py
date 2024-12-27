import requests

def authenticate_user(email, password):
    url = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"
    try:
        # Send the POST request
        response = requests.post(url, json={"email": email, "password": password})
        print(f"Raw response: {response.text}")

        # Ensure the response is valid JSON
        try:
            user_details = response.json()  # Attempt to parse the JSON
        except ValueError:
            print("Error: Response is not valid JSON.")
            return None

        # Handle specific response format
        if isinstance(user_details, list):
            if len(user_details) == 2 and user_details[0] == "Verified" and user_details[1] == "True":
                # Mock role and user_id for the sake of testing
                return {"role": "admin", "user_id": 1}  # Update based on your testing needs
            elif len(user_details) == 2 and user_details[0] == "Verified" and user_details[1] == "False":
                print("Authentication failed.")
                return None

        # Handle unexpected cases
        print("Unexpected response format from the API.")
        return None
    except requests.RequestException as e:
        print("Error connecting to Authenticator API:", e)
        return None
