
# This will create HashMap lass using chaining
# Citation:
# C950 - Webinar-2 - Getting Greedy, who moved my data?
# W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Ref: zyBooks: 3.3.1: MakeChange greedy algorithm.
# https://srm--c.na127.visual.force.com/apex/coursearticle?Id=kA03x000000e1g4CAA

class HashMap:
    # This method initializes an empty list with optional capacity parameter
    def __init__(self, initial_capacity=10):
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # Inserts a new item into the hash table, using two arguments
    # Time complexity of (O(n))(worst case), where n is the number of key-value pairs
    def insert(self, key, value):
        bucket = hash(key) % len(self.map)
        bucket_list = self.map[bucket]

        # This updates the key if it already exists in the bucket
        for hash_key in bucket_list:
            if hash_key[0] == key:
                hash_key[1] = value
                return True

        # This will append to the end of the list if it does not exist
        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # This will search for a matching key-value pair in the hashmap
    # It will return the item if found,or none if not found
    # Time complexity of (O(n))(worst case), where n is the number of key-value pairs
    def get_hash_value(self, key):
        bucket = hash(key) % len(self.map)
        bucket_list = self.map[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None

    # This removes an item with matching key from the hash table
    # Time complexity of (O(n))(worst case), where n is the number of key-value pairs
    def delete_hash_value(self, key):
        bucket = hash(key) % len(self.map)
        bucket_list = self.map[bucket]

        # This will remove the key if it is present in the hash map
        if key in bucket_list:
            bucket_list.remove(key)