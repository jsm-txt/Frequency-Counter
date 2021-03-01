from LinkedList import LinkedList


class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    arr_list = []

    for i in range(self.size):
      arr_list.append(LinkedList())

    return arr_list


  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    key_length = len(key)

    index = key_length % self.size

    return index



  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):

    index = self.hash_func(key)

    bucket = self.arr[index]

    item = (key,value)
  
    is_in_ll= bucket.find(key)
    
    print(item)
    print(is_in_ll)

    if is_in_ll != -1:
      
      current =bucket.head

      for i in range(is_in_ll):
        print(current.data)
        current = current.next

      value = current.data[1] +1
      item = (key, value)
      current.data = item
      
    else:
      
      bucket.append(item)
    
    

  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    counter = 1
    for llist in self.arr:
      if llist.length == 0:
        print(f'NO DATA IN HASH: {counter}')
        pass
      else:
        print(f'IN HASH: {counter}')
        current =llist.head
        while current != None:
          print(current.data)
          current = current.next
      counter = counter +1
    



