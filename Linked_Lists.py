#! python3
# CRACKING THE CODING INTERVIEW by GAYLE LAAKMANN  4th Edition [in Python 3]
#Chapter 2 | Linked Lists


class Node:
    def __init__(self,init_data):
        self.data = init_data
        self.next = None
        self.position = 0
		
    def get_data(self):
        return self.data
		
    def get_next(self):
        return self.next
		
    def get_position(self):
        return self.position
		
    def set_data(self,new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next
	
    def set_position(self, new_position):
        self.position = new_position
		
		
class UnorderedList:
    def __init__(self):
        self.head = None
		
    def is_empty(self):
        return self.head == None
		
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.adjust_position()
		
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        return count
		
    def search(self,item):
        found = False
        current = self.head
        while current != None and not found :
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
	
    def __str__(self):
        current = self.head
        n = []
        while current != None:
            n.append(str(current.get_data()))
            current = current.get_next()
        return "->".join(n)
				
			
    #2.1 Write code to remove duplicates from an unsorted linked list.
    def remove_duplicate(self):
        previous = None
        current = self.head
        dictionary = {}
        while current != None:
            #checks if item is in dictionary and then inserts it
            if current.get_data() not in dictionary:
                dictionary[current.get_data()] = True
                previous = current
                current = current.get_next()
            #else if the item is already in dictionary:
            else:
                previous.set_next(current.get_next())				
                current = previous.get_next()
	
    #2.2 Implement an algorithm to find the nth to last element of a singly linked list.	
    def return_nth_data_downwards(self,n):
        current = self.head
        count =0
        g = list()
        while current != None:
            if count == n:
                break
            else:
                current = current.get_next()
                count += 1
        while current != None:
            g.append(current.get_data())
            current = current.get_next()
        return g 
		
    #2.3 Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.
    #EXAMPLE
    #Input: the node c from the linked list a->b->c->d->e
    #Result: nothing is returned, but the new linked list looks like a->b->d->e	
    def remove(self,item):
        try:
            previous = None
            current = self.head
            found =  False	
            while current != None and not found:
                if current.get_data() == item:
                    found = True
                else:
                    previous = current 
                    current = current.get_next()
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
        except:
            print('item does not exist')
			
	
	