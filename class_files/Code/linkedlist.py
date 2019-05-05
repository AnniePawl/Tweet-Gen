class Node(object):

    def __init__(self, data):
        """Initialize node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize a linked list and append the given items, if any."""
        self.head = None
        self.tail = None

        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in linked list.
        Best and worst case running time: O(n) for n items in the list (length) because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # O(n) always n iterations, no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty.
        Running time: 0(1), just checking 1 value"""
        return self.head is None  # O(1), just checking 1 value

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n), for n items in linkedlist(length)iterates over All items to count them"""
        counter = 0  # O(1) time to assign variable
        current_node = self.head  # O(1) time to assign variable
        while current_node is not None:
            counter += 1  # O(1), add count is one step
            current_node = current_node.next  # O(1) time to assign variable
        return counter  # O(1) to return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1), one step, simply adding item to end """
        new_node = Node(item)
        if self.tail is not None:  #
            self.tail.next = new_node  # O(1) time to reassign next pointer
            self.tail = new_node  # O(1) time to reassign tail
        else:
            # if nothing in list, create first node! first and only node = head AND tail
            self.head = new_node  # O(1) to assign new variable
            self.tail = new_node  # O(1) to assign new variable

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1), one step, simply adding item at beginning"""
        new_node = Node(item)
        if self.head is not None:  # O(1), one step, just checking if empty
            # newest node is prepended (becomes head node)
            new_node.next = self.head  # O(1) to reassign next pointer
            self.head = new_node  # O(1) to reassign head pointer
        else:
            self.head = new_node  # O(1) to reassign head
            self.tail = new_node  # O(1) to reassign tail

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1), if data in first node?
        Worst case running time: O(n), if data not found"""
        current_node = self.head  # O(1) to assign head
        while current_node is not None:  # from 1 to n iterations, depends
            if quality(current_node.data):  # O(1) to check quality
                return current_node.data  # O(1) to return data
            else:
                current_node = current_node.next  # O(1) to reassign varaible
        if current_node == None:
            return None  # O(1) to return None

    # This method still needs to be tested
    def replace(old_item, new_item):
        """ Replaces old item with new item without creating new node"""
        current_node = self.head  # O(1) to assign variable
        while current_node is not None:  # O(1) to check if empty
            if current_node.data == old_item:  # O(1) to check
                current_node.data = new_item  # O(1) to reassign node
                return  # O(1) to return
            else:
                # O(1) to return
                raise ValueError('Item not found: {}'.format(item))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if LL empty or item at head
        Worst case running time: O(n), might traverse entire list"""
        previous_node = None
        # TODO: Loop through all nodes to find one whose data matches given item
        current_node = self.head
        while current_node is not None:
            if current_node.data == item:
                if current_node == self.head and current_node == self.tail:
                    self.head = None
                    self.tail = None
                elif current_node == self.head:
                    self.head = current_node.next
                    current_node.next = None
                elif current_node == self.tail:
                    self.tail = previous_node
                    previous_node.next = None
                else:
                    previous_node.next = current_node.next
                    current_node.next = None
                return
            else:
                previous_node = current_node
                current_node = current_node.next
        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
