import requests

def authenticate_user(email, password):
    """
    Authenticate the user using the Authenticator API.

    Args:
        email (str): The user's email.
        password (str): The user's password.

    Returns:
        dict: User details if authentication is successful.
        None: If authentication fails.
    """
    url = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"
    try:
        response = requests.post(url, json={"email": email, "password": password})
        if response.status_code == 200:
            return response.json()  # Returns user details (e.g., role, user_id)
        else:
            print(f"Authentication failed: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print("Error connecting to Authenticator API:", e)
        return None
