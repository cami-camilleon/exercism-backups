"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] = current_cart[item] + 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = dict()

    for item in notes:
        cart.setdefault(item, 0)
        cart[item] = cart[item] + 1

    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas |= recipe_updates

    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    # /they call me the one liner.../
    # yes i know i couldve one lined some other functions in this file.
    # yes i know the comments are creating more lines leading to 
    # a defeat of purpose of one lining the solution to this section.
    #
    # frick you.
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    rev_cart = dict(reversed((sorted(cart.items()))))
    ful_cart = dict()

    for item in rev_cart:
        #print(item)
        # ok now each thing is an entry to a dict
        # variable item is going to be a ummm tuple?...
        if item in aisle_mapping.keys():
            # UR TELLING ME THE PROBLEM THE HWOLE TIME WAS THAT I WAS USING 
            # TUPLE PARENTHESIS INSTEAD OF LIST BRACKETS??????
            # FUCK MY PYCHUD LIFE BRO...
            ful_cart[item] = [rev_cart[item], *aisle_mapping[item]]
            #print(ful_cart)

    return ful_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    # correct me if im wrong but it seems like when u have to have 
    # two dicts interact with each other in a manner more 
    # complicated than a simple .update or union can handle, 
    # the easiest way to handle that scenario is by making one or 
    # both dicts tuple lists... perchance

    # (after debugging) oh this solution just reeks man...

    for item in fulfillment_cart.items():
        # btw im just checking to be safe. im being safe, ok?
        if item[0] in store_inventory.keys():
            if store_inventory[item[0]][0] > fulfillment_cart[item[0]][0]:
                store_inventory[item[0]][0] = store_inventory[item[0]][0] - fulfillment_cart[item[0]][0]
            else:
                store_inventory[item[0]][0] = 'Out of Stock'

    return store_inventory

# debugging sucks ass with these tests bro.
"""send_to_store(
        {
            "Banana": 3, 
            "Apple": 2, 
            "Orange": 1, 
            "Milk": 2
        },
        {
            "Banana": ["Aisle 5", False],
            "Apple": ["Aisle 4", False],
            "Orange": ["Aisle 4", False],
            "Milk": ["Aisle 2", True],
        })"""