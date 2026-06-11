from login import login_system, role_menu
from ecommerce import ecommerce_pricing


def main():
    role = login_system()
    if role is None:
        return

    role_menu(role)
    ecommerce_pricing()


if __name__ == "__main__":
    main()
