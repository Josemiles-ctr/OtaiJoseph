location_tax_rates = {
    "Wandegeya": 0.08,
    "Kikoni": 0.09,
    "Kukumikukumi": 0.07,
    "Africa": 0.06,
    "Mitchell": 0.075,
}

coupon_codes = {
    "BSSE": 0.10,
    "JOSE": 0.20,
    "HASH": 0.30,
}


def apply_coupon_discount(total_price, coupon_code=None):
    if coupon_code is None or coupon_code == "":
        return total_price

    coupon_code = coupon_code.upper()
    if coupon_code in coupon_codes:
        discount_rate = coupon_codes[coupon_code]
        if discount_rate > 0:
            return total_price - (total_price * discount_rate)
        return total_price
    raise ValueError("Invalid coupon code.")


def calculate_total_price(location="Unknown", price=0.0):
    if location in location_tax_rates:
        tax_rate = location_tax_rates[location]
        if tax_rate > 0:
            return price + (price * tax_rate)
        return price
    return price


def get_price_based_discount(sub_price):
    if 0 <= sub_price <= 100:
        return 0
    if sub_price > 100:
        if sub_price <= 500:
            return 0.05
        if sub_price <= 1000:
            return 0.10
        if sub_price > 1000:
            return 0.15
    raise ValueError("Invalid sub price.")


def ecommerce_pricing():
    location = input("Enter the location: ").strip()
    price = float(input("Enter the price: "))
    subtotal = calculate_total_price(location, price)
    print(f"Total price after tax: {subtotal:.2f}")

    sub_price = float(input("Enter the subtotal for discount calculation: "))
    discount_rate = get_price_based_discount(sub_price)
    discounted_price = subtotal - (subtotal * discount_rate)
    print(f"Total price after price-based discount: {discounted_price:.2f}")

    coupon_code = input("Enter a coupon code (or press Enter to skip): ").strip()
    try:
        final_price = apply_coupon_discount(discounted_price, coupon_code)
        print(f"Final price after coupon: {final_price:.2f}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    ecommerce_pricing()
