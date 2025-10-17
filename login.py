# Simple Login Authentication System
# Author: Suraj Bhatt
# Language: Python

import getpass  # For hiding password input

# --- Helper Functions ---

def register():
    print("\n=== User Registration ===")
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")

    # Check if username already exists
    with open("users.txt", "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")
            if username == stored_user:
                print("⚠️ Username already exists! Try another one.")
                return

    # Save new user
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("✅ Registration successful!")


def login():
    print("\n=== User Login ===")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    with open("users.txt", "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")
            if username == stored_user and password == stored_pass:
                print("✅ Login successful!")
                secured_page(username)
                return
    print("❌ Invalid username or password!")


def secured_page(username):
    print("\n=== Welcome to the Secured Page ===")
    print(f"Hello, {username}! 🎉 You have access to this page.")
    print("Here you can access secret data or perform secure actions.")
    input("\nPress Enter to log out...")


# --- Main Program ---

def main():
    # Create file if it doesn’t exist
    open("users.txt", "a").close()

    while True:
        print("\n=== Simple Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Try again.")


if __name__ == "__main__":
    main()
