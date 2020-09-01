class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.item_count = 0
        if capacity >= MIN_CAPACITY:
            self.storage = [None] * self.capacity
        else:
            print(f"\nYou must pick a capacity larger than {MIN_CAPACITY}. Capacity is set to {MIN_CAPACITY}\n")
            self.storage = [None] * MIN_CAPACITY

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.item_count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        str_key = str(key).encode()
        hash_value = 5381

        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff
        
            return hash_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)

        if self.storage[idx] == None:
            self.storage[idx] == HashTableEntry(key, value)
            self.item_count += 1
        else:
            current_entry = self.storage[idx]
            while current_entry.next != None and current_entry.key != key:
                current_entry = current_entry.next
            if current_entry.key == key:
                current_entry.value = value
            else:
                new_entry = HashTableEntry(key, value)
                new_entry.next = self.storage[idx]
                self.storage[idx] = new_entry
                self.item_count += 1
        
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)

        if self.storage[idx].key == key:
            if self.storage[idx].next == None:
                self.storage[idx] = None
                self.item_count -= 1
            else:
                new_head = self.storage[idx].next
                self.storage[idx].next = None
                self.storage[idx] = new_head
                self.item_count -= 1
        else:
            if self.storage[idx] == None:
                return
            else:
                current_value = self.storage[idx]
                previous_value = None
                while current_value.next is not None and current_value.key != key:
                    previous_value = current_value
                    current_value = current_value.next
                if current_value.key == key:
                    previous_value.next = current_value.next
                    self.item_count -= 1
                    return current_value
                else:
                    return
        
        if self.get_load_factor() < .2:
            if self.capacity / 2 > MIN_CAPACITY:
                self.resize(self.capacity / 2)
            elif self.capacity > MIN_CAPACITY:
                self.resize(MIN_CAPACITY)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)

        if self.storage[idx] is not None and self.storage[idx].key == key:
            return self.storage[idx].value
        elif self.storage[idx] is None:
            return
        else:
            while self.storage[idx].next is not None and self.storage[idx].key != key:
                self.storage[idx] = self.storage[idx].next
            if self.storage[idx] == None:
                return
            else:
                return self.storage[idx].value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        previous_table = self.storage[:]
        previous_capacity = self.capacity
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        for i in range(0, previous_capacity):
            if previous_table[i] is not None:
                current_entry = previous_table[i]
                self.put(current_entry.key, current_entry.value)

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
