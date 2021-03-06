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
            for key, value in bucket.items():  # O(n) to iterate over items
                all_keys.append(key)  # O(n) to append all keys to list
        return all_keys  # O(1) to return list

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n), must iterate over all items to append all values to values list"""
        all_values = []  # O(1) to create empty list
        for bucket in self.buckets:  # O(n) to iterate over all b
            for key, value in bucket.items():  # O(n) to iterate over items
                all_values.append(value)  # O(n) to append all values to list
        return all_values  # O(1) to return list

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(b*l) -> O(n) to collect all items and return"""
        all_items = []  # O(1) to create empty list
        for bucket in self.buckets:  # O(b) iterate over all buckets
            all_items.extend(bucket.items())  # O(l)
        return all_items  # O(1) to return a list

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(b*l) => O(n), must traverse buckets and it's items to determine length"""
        length = 0  # O(1) to create this variable
        for bucket in self.buckets:  # O(b) to iterate over buckets
            length += bucket.length()  # O(l) for length method
        return length  # O(1) to return variable

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(l), l=bucket length, due to find method"""
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]  # O(1)
        item = bucket.find(lambda entry: entry[0] == key)   # O(l), l = length
        return item is not None  # O(1) to check if item found

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(l) due to find method"""
        index = self._bucket_index(key)  # O(1) to assign index
        bucket = self.buckets[index]  # O(1) to assign bucket
        item_found = bucket.find(
            lambda entry: entry[0] == key)   # O(l), l = length

        if item_found is not None:  # O(n) to find key
            return item_found[1]  # (1) to reutrn entry
        else:
            # O(1) to raise KeyError
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(l), l=bucket length """
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]  # O(1)
        entry_found = bucket.find(lambda pair: pair[0] == key)
        entry = (key, value)  # O(l) due to find method

        if entry_found is not None:  # Update old key w/ new value
            bucket.delete(entry_found)  # O(l) worst case

        bucket.append((key, value))  # O(1) to add item

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(n) to find key right key and delete?"""
        index = self._bucket_index(key)  # O(1) to assign index
        bucket = self.buckets[index]  # O(1) to assign bucket
        # Check if key-value entry exists in bucket
        def key_matcher(key_val): return key_val[0] == key
        entry_found = bucket.find(key_matcher)

        if entry_found is not None:  # O()
            bucket.delete(entry_found)  # O()
        else:
            # O(1) to raise error
            raise KeyError('Key not found: {}'.format(key))


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
