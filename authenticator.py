import requests
import logging

# Configure logging
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
        if isinstance(user_details, list) and len(user_details) == 2:
            if user_details[0] == "Verified" and user_details[1] == "True":
                # Assign roles based on email
                role = "admin" if email == "grace@plymouth.ac.uk" else "user"
                user_id = 1 if role == "admin" else 2  # Example UserID for admin and non-admin
                logging.info(f"Authentication successful. Role: {role}")
                return {"role": role, "user_id": user_id}
            else:
                logging.info("Authentication failed: Invalid credentials.")
                return None

        # Handle unexpected cases
        logging.warning("Unexpected response format from the API.")
        return None
    except requests.RequestException as e:
        logging.error(f"Error connecting to Authenticator API: {e}")
        return None
