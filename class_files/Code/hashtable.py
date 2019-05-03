#!python
from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n), must iterate over each item to append key to key list"""
        all_keys = []  # O(1) to create empty list
        for bucket in self.buckets:  # O(n) to iterate over all b
            for key, value in bucket.items():
                all_keys.append(key)  # O(n) to append all keys to list
        return all_keys  # O(1) to return list

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n), must iterate over all items to append all values to values list?"""
        all_values = []  # O(1) to create empty list
        for bucket in self.buckets:  # O(n) to iterate over all b
            for key, value in bucket.items():
                all_values.append(value)  # O(n) to append all values to list
        return all_values  # O(1) to return list

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) to collect all items and return?"""
        all_items = []  # O(1) to create empty list
        for bucket in self.buckets:  # O(n) to collect all items
            all_items.extend(bucket.items())
        return all_items  # O(1) to return a list

    # Getting Error += int and type unsupported
    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(b*l) => O(n), must traverse buckets and it's items to determine length"""
        length = 0  # O(1) to create this variable
        for bucket in self.buckets:  # O(b) to iterate over buckets
            length += bucket.length()  # O(l) for length method
        return length  # O(1) to return variable

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Find bucket where given key belongs
        for bucket in self.buckets:  # O(b) to traverse buckets
            for current_key, value in bucket.items():
                # TODO: Check if key-value entry exists in bucket
                if current_key is key:
                    return True  # O(1) to return boolean
        return False  # O(1) to return boolean

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index(key)]
        # Check if key-value entry exists in bucket
        def key_matcher(key_val): return key_val[0] == key
        entry_found = bucket.find(key_matcher)

        # If found, return value associated with given key
        if entry_found is not None:
            return entry_found[1]
        else:
            # TODO: Otherwise, raise error to tell user get failed
            # Hint: raise KeyError('Key not found: {}'.format(key))
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # if found
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        # else:
        #     raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
