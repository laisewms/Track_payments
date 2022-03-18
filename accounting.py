melon_cost = 1.00

def account_app():

    """program to track customer payments."""

    customers_list = open('customer-orders.txt')
    

    print("Customers and the amount paid")
    for client in customers_list:

        client = client.rstrip()
        item = client.split('|')

        customer = item[1]
        melons_quantity = item[2]
        paid_amount = item [3]

        melons_quantity = float(melons_quantity)
        paid_amount = float(paid_amount)

        customers_expected_total = melons_quantity * melon_cost

        print(f"{customer} paid ${paid_amount},",
             f" expected ${customers_expected_total}")
        
        if customers_expected_total < paid_amount:
            print(f"{customer} has OVERPAID for their melons.")
    
        elif customers_expected_total > paid_amount:
            print(f"{customer} has UNDERPAID for their melons.")

    customers_list.close()

account_app()

