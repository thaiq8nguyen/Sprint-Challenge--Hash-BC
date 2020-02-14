#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    a = []

    for i in range(len(weights)):
        if hash_table_retrieve(ht, weights[i]) is not None:
            if weights[i]*2 == limit:
                return [i, hash_table_retrieve(ht, weights[i])]
        else:
            hash_table_insert(ht, weights[i], i)

    for j in weights:
        if hash_table_retrieve(ht, limit - j):
            a.append(hash_table_retrieve(ht, limit - j))
            a.append(hash_table_retrieve(ht, j))
            return a

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
