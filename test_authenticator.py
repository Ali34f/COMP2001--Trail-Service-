from authenticator import authenticate_user

def test_authenticator():
    # Test with admin credentials
    print("Testing admin credentials...")
    admin_user = authenticate_user("grace@plymouth.ac.uk", "ISAD123!")
    print(f"Admin credentials test result: {admin_user}")

    # Test with non-admin credentials
    print("\nTesting non-admin credentials...")
    non_admin_user = authenticate_user("ada@plymouth.ac.uk", "insecurePassword")
    print(f"Non-admin credentials test result: {non_admin_user}")

    # Test with invalid credentials
    print("\nTesting invalid credentials...")
    invalid_user = authenticate_user("invalid@plymouth.ac.uk", "wrongpassword")
    print(f"Invalid credentials test result: {invalid_user}")

    # Test with missing credentials
    print("\nTesting missing credentials...")
    missing_user = authenticate_user("", "")
    print(f"Missing credentials test result: {missing_user}")

    # Test with an unreachable API
    print("\nTesting unreachable API...")
    unreachable_user = authenticate_user("unreachable@test.com", "password")
    print(f"Unreachable API test result: {unreachable_user}")

if __name__ == "__main__":
    test_authenticator()
