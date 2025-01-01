from authenticator import authenticate_user

def test_authenticator():
    # Test the authenticator with valid credentials
    print("Testing valid credentials...")
    user_details = authenticate_user("grace@plymouth.ac.uk", "ISAD123!")
    print(f"Valid credentials test result: {user_details}")


    # Test the authenticator with invalid credentials
    print("\nTesting invalid credentials...")
    invalid_user = authenticate_user("invalid@plymouth.ac.uk", "wrongpassword")
    print(f"Invalid credentials test result: {invalid_user}")

    # Test the authenticator with missing credentials
    print("\nTesting missing credentials...")
    missing_user = authenticate_user("", "")
    print(f"Missing credentials test result: {missing_user}")

    # Test the authenticator with an unreachable API
    print("\nTesting unreachable API...")
    unreachable_user = authenticate_user("unreachable@test.com", "password")
    print(f"Unreachable API test result: {unreachable_user}")

if __name__ == "__main__":
    test_authenticator()
