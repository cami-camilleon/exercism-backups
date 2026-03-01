"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagons1, wagons2, *wagons_rest = each_wagons_id
    *each_wagons_id, = *wagons_rest, wagons1, wagons2
    wagons1, *wagons_rest = each_wagons_id

    *fixed_list, = wagons1, *missing_wagons, *wagons_rest
    return fixed_list



def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    #print({**route, 'stops': list(stops.values())})
    return {**route, 'stops': list(stops.values())}

"""add_missing_stops({"from": "New York", "to": "Miami"},
                      stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                      stop_4="Jacksonville", stop_5="Orlando")"""


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    
    unpacked = []

    for thing in wagons_rows:
        *unpacked, = *unpacked, *thing

    list1 = []
    list2 = []
    list3 = []

    for i, item in enumerate(unpacked):
        if i % 3 == 0:
            list1.append(item)
        elif i % 3 == 1:
            list2.append(item)
        else:
            list3.append(item)

    return([list1, list2, list3])
    
fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ])