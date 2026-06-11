users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "customer": {"password": "customer123", "role": "Customer"},
    "cashier": {"password": "cashier123", "role": "Cashier"},
}


def login_system():
    print("Login System")
    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ").strip()

    user = users.get(username)
    if user is None:
        print("Invalid credentials.")
        return None
    if user["password"] == password:
        if user["role"] == "Admin":
            print("Welcome, Admin.")
        elif user["role"] == "Customer":
            print("Welcome, Customer.")
        elif user["role"] == "Cashier":
            print("Welcome, Cashier.")
        return user["role"]
    print("Invalid credentials.")
    return None


def role_menu(role):
    print(f"\n{role} access granted.")

    if role == "Admin":
        print("You can access all features.")
    elif role == "Customer":
        print("You can view and buy products.")
    elif role == "Cashier":
        print("You can process payments and calculate totals.")
    else:
        print("Unknown role.")


if __name__ == "__main__":
    user_role = login_system()
    if user_role is not None:
        role_menu(user_role)
