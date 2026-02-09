"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inv_dict = dict()

    for item in items:
        if item in inv_dict.keys():
            inv_dict[item] = inv_dict[item] + 1
        else:
            inv_dict[item] = 1

    return inv_dict


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        if inventory.get(item, False):
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        # cheeky use of short circuit conditional checks >:3 or whatever
        if inventory.get(item, False) and inventory[item] > 0:
            inventory[item] = inventory[item] - 1

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if inventory.get(item, False):
        inventory.pop(item)

    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    final = []

    for item in inventory:
        if inventory[item] > 0:
            final.append((item, inventory[item]))

    return final

#list_inventory({'1': 'one', '2': 'two'})