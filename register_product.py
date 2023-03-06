from main import Product
try:
    product_Price = input("Enter product price \n")
    product_Quantity = input("Enter product quantity \n")
    product_Description = input("Enter product description \n")

    Product.create(product_price=product_Price, product_quantity=product_Quantity, product_description=product_Description)
    print("Product created successfully")

except:
    print("Failed to create Product")
