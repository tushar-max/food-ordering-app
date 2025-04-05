from dal.owner.dish_by_id_dal import delete_data_dal, get_dish_by_id_dal


def get_dish_by_id(dish_id):
    try:
        return get_dish_by_id_dal(dish_id)
    except Exception as e:
        return {'message': 'Some error occured'}, 500

# Delete
def delete_data(book_id):
    try:
        return delete_data_dal(book_id)
    except:
        return False