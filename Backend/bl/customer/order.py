from dal.customer.order import get_orders_dal

def get_orders_bl(email):
    try:
        return get_orders_dal(email)
    except Exception as e:
        # print(e)
        return {'message': 'Some error occured'}, 500