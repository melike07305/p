def cafe_system():
    print("Welcome to the Cafe")
    products = {
        "Coffee" : {"category" : "drinks","price" : 3},
        "Tea" : {"category" : "drinks","price" : 2}, 
        "Sandwich" : {"category" : "food","price" : 5}, 
        "Cake" : {"category" : "deserts","price" : 4},
    }
    selected = []
    while True:
        print("menu:")
        for i,j in products.items():
            print(f"{i} ({j['category']}) : {j['price']} $")
            ask = input("enter the item you want to order or 'done': ")
            quantity = int(input("Enter the quantity: "))
            if ask == "done":
                break
            else:
                print(f"{quantity} {ask} (s) added to your order")
                n = quantity * {j['price']}
cafe_system()

            


