#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    begin = hash_table_retrieve(hashtable, "NONE")
    current = begin

    route[0] = current

    j = 0

    while current != "NONE":
        current = hash_table_retrieve(hashtable, current)
        j += 1
        route[j] = current

    for airport in route:
        if airport == "NONE":
            route.remove(airport)
    return route
