import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def authenticate_user(email, password):
    """
    Authenticates the user against the given authentication API.
    """
    url = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"
    try:
        # Send the POST request
        response = requests.post(url, json={"email": email, "password": password}, timeout=10)
        logging.debug(f"Raw response: {response.text}")

        # Ensure the response is valid JSON
        try:
            user_details = response.json()
        except ValueError:
            logging.error("Response is not valid JSON.")
            return None

        # Handle specific response format
        if isinstance(user_details, list):
            if len(user_details) == 2 and user_details[0] == "Verified" and user_details[1] == "True":
                logging.info("Authentication successful.")
                return {"role": "admin", "user_id": 1}  # Adjust role and user_id as per your API
            elif len(user_details) == 2 and user_details[0] == "Verified" and user_details[1] == "False":
                logging.info("Authentication failed: Invalid credentials.")
                return None

        # Handle unexpected cases
        logging.warning("Unexpected response format from the API.")
        return None
    except requests.RequestException as e:
        logging.error(f"Error connecting to Authenticator API: {e}")
        return None
