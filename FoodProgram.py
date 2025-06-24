import FoodClass as fc

# This dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid']

dict = {
    'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
    'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
    'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
    'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
}

# Start with first customer
customer_id = 570

while True:
    order_total = 0
    
    # Create customer instance based on current customer_id
    if customer_id == 570:
        customer = fc.Customer(570, "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", 
                              "dsellyarft@gmpg.org", "254-555-9362", False)
    elif customer_id == 569:
        customer = fc.Customer(569, "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", 
                              "ahimsworthfs@list-manage.com", "254-555-2273", True)
    
    # Create transaction instances for this customer
    customer_transactions = []
    
    for trans_id, trans_data in dict.items():
        date = trans_data[0]
        item_name = trans_data[1]
        cost = trans_data[2]
        customerid = trans_data[3]
        
        # Only add transactions for this customer
        if customerid == customer.get_customerid():
            transaction = fc.Transaction(date, item_name, cost, customerid)
            customer_transactions.append(transaction)
    
    # Calculate order total
    for transaction in customer_transactions:
        order_total += transaction.get_cost()
    
    # Display customer information and order details
    print(f"Customer Name: {customer.get_name()}")
    print(f"Phone: {customer.get_phone()}")
    
    # Display each ordered item
    for transaction in customer_transactions:
        print(f"Order Item: {transaction.get_item_name()}  Price: ${transaction.get_cost():.2f}")
    
    print(f"Total Cost: ${order_total:.2f}")
    
    # Apply member discount if applicable
    if customer.get_member_status():
        discount = order_total * 0.20
        total_after_discount = order_total - discount
        print(f"Member Discount: ${discount:.2f}")
        print(f"Total Cost after discount: ${total_after_discount:.2f}")
    
    # Press Enter for another customer
    input("\nEnter for another reciept: ")
    
    # Switch to the other customer
    customer_id = 569 if customer_id == 570 else 570
    print()