
import hashlib
import secrets
import hmac
import getpass

USER_FILE = "users.txt"
MAX_ATTEMPTS = 3
SPECIAL_CHARACTERS = "!@#$%^&*"


# =============== FILE HANDLING ===============

def load_users():
    users = {}

    try:
        with open(USER_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) == 3:
                    username, salt, hashed_password = parts
                    users[username] = (salt, hashed_password)

    except FileNotFoundError:
        pass

    return users


def save_user(username, salt, hashed_password):
    with open(USER_FILE, "a") as file:
        file.write(
            f"{username},{salt},{hashed_password}\n"
        )


# =============== PASSWORD SECURITY ===============

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        bytes.fromhex(salt),
        200000
    ).hex()

    return salt, hashed


# =============== VALIDATION FUNCTIONS ===============

def validate_username(username, users):
    if not username:
        raise ValueError("Username cannot be empty.")

    if len(username) < 4:
        raise ValueError(
            "Username must be at least 4 characters long."
        )

    if not username.isalnum():
        raise ValueError(
            "Username must contain only letters and digits."
        )

    if username in users:
        raise ValueError("Username already exists.")


def validate_password(password):
    if len(password) < 8:
        raise ValueError(
            "Password must be at least 8 characters long."
        )

    if any(ch.isspace() for ch in password):
        raise ValueError("Password cannot contain spaces.")

    if not any(ch.isupper() for ch in password):
        raise ValueError("Include an uppercase letter.")

    if not any(ch.islower() for ch in password):
        raise ValueError("Include a lowercase letter.")

    if not any(ch.isdigit() for ch in password):
        raise ValueError("Include a digit.")

    if not any(ch in SPECIAL_CHARACTERS for ch in password):
        raise ValueError(
            "Include a special character: !@#$%^&*"
        )


# =============== MENU FUNCTION ===============

def get_menu_choice():
    try:
        choice = int(input("Enter your choice (1-3): "))
        return choice

    except ValueError:
        print("Invalid input! Enter a number from 1 to 3.")
        return None


# =============== REGISTRATION ===============

def register_user(users):
    try:
        username = input("Choose a username: ").strip()
        validate_username(username, users)

        password = getpass.getpass("Choose a password: ")
        validate_password(password)

        confirm_password = getpass.getpass(
            "Confirm your password: "
        )

        if password != confirm_password:
            raise ValueError("Passwords do not match.")

    except ValueError as error:
        print("Registration failed:", error)

    except (EOFError, KeyboardInterrupt):
        print("\nRegistration cancelled.")

    else:
        salt, hashed = hash_password(password)

        save_user(username, salt, hashed)
        users[username] = (salt, hashed)

        print(f"User '{username}' registered successfully!")

    finally:
        print("-- Registration process finished --")


# =============== LOGIN ===============

def login_user(users, locked_users):
    if not users:
        print("No users registered. Please register first.")
        return

    username = input("Enter username: ").strip()

    if username in locked_users:
        print("This account is locked for this program run.")
        return

    for attempt in range(MAX_ATTEMPTS):
        try:
            password = getpass.getpass("Enter password: ")

            if username not in users:
                raise ValueError("Invalid credentials")

            salt, stored_hash = users[username]
            _, entered_hash = hash_password(password, salt)

            if not hmac.compare_digest(
                stored_hash, entered_hash
            ):
                raise ValueError("Invalid credentials")

        except ValueError:
            remaining = MAX_ATTEMPTS - attempt - 1
            print(
                "Invalid username or password.",
                "Attempts left:", remaining
            )

        except (EOFError, KeyboardInterrupt):
            print("\nLogin cancelled.")
            return

        else:
            print(f"\nLogin successful! Welcome, {username}!")
            return

    if username in users:
        locked_users.add(username)

    print("Too many failed attempts. Login blocked.")


# =============== MAIN PROGRAM ===============

def main():
    users = load_users()
    locked_users = set()

    print("=" * 45)
    print("          SECURE LOGIN SYSTEM")
    print("=" * 45)
    print(f"{len(users)} registered user(s) loaded.")

    while True:
        print("\n1. Register New User")
        print("2. Login")
        print("3. Exit")

        choice = get_menu_choice()

        if choice is None:
            continue

        elif choice == 1:
            register_user(users)

        elif choice == 2:
            try:
                login_user(users, locked_users)
            except (EOFError, KeyboardInterrupt):
                print("\nLogin cancelled.")

        elif choice == 3:
            print("Exiting Secure Login System. Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram terminated safely.")
