def generate_invoice(customer_name, products):
    print("\n----------- INVOICE -----------")
    print(f"Customer Name: {customer_name}")
    print("-------------------------------")
    print("Product\t\tPrice")
    print("-------------------------------")
    total = 0
    for product, price in products:
        print(f"{product}\t\t₹{price}")
        total += price
    print("-------------------------------")
    print(f"Total Amount:\t₹{total}")
    print("-------------------------------")

if __name__ == "__main__":
    name = input("Enter the customer's name: ")
    num_products = int(input("Enter the number of products: "))
    product_details = []

    for _ in range(num_products):
        product_name = input("Enter product name: ")
        price = float(input(f"Enter price for {product_name}: "))
        product_details.append((product_name, price))
    
    generate_invoice(name, product_details)
