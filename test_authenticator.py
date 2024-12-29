from authenticator import authenticate_user

# Test the authenticator with a valid user
print("Testing valid credentials...")
user_details = authenticate_user("grace@plymouth.ac.uk", "ISAD123!",)

print(f"Valid credentials test result: {user_details}")

# Test the authenticator with invalid credentials
print("\nTesting invalid credentials...")
invalid_user = authenticate_user("invalid@plymouth.ac.uk", "wrongpassword")
print(f"Invalid credentials test result: {invalid_user}")

# Test edge cases
print("\nTesting missing credentials...")
missing_user = authenticate_user("", "")
print(f"Missing credentials test result: {missing_user}")
