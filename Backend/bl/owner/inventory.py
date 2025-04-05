from dal.owner.inventory_dal import delete_data_dal, get_inventory_dal


def get_inventory(email):
    return get_inventory_dal(email)


def delete_data(id):
    return delete_data_dal(id)