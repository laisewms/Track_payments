melon_cost = 1.00

def account_app():

    """program to track customer payments."""

    #it will open the file
    customers_list = open('customer-orders.txt')
    #




    for client in customers_list:

        client = client.rstrip()
        item = client.split('|')

        customer = item[1]
        melons_quantity = item[2]
        paid_amount = item [3]

        melons_quantity = float(melons_quantity)
     

        customers_expected_total = melons_quantity * melon_cost
        if customers_expected_total != paid_amount:
            print(f"{customer} paid ${paid_amount},",
             f" expected ${customers_expected_total}")



    customers_list.close()

account_app()

