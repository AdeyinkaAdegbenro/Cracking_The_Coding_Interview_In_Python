#! python3
# CRACKING THE CODING INTERVIEW by GAYLE LAAKMANN  4th Edition [in Python 3]
#Chapter 2 | Linked Lists


class Node:
    '''an helper class to the Class UnorderedList, that acts as container for holding the data of the items in the linked list '''
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
		
    def extract(self):
        #an helper method for exercise 2.4
        current = self.head
        n = []
        while current != None :
            n.append(current.get_data())
            current = current.get_next()
        return n
	
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
			

    
			
	
#2.4 You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1’s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
#EXAMPLE
#Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
#Output: 8 -> 0 -> 8
def add_list(l1,l2):
    a = l1.extract(); b = l2.extract()
    a = int("".join(list(map(str,a)))) ; b = int("".join(list(map(str, b))))
    sum_list = list(str(a + b))    #here the sum is converted to a string then a list, 
    sum_list.reverse()             #then reversed before being added to an empty linked list below
    L = UnorderedList()
    for i in sum_list:
        L.add(i)
		
    print(L)
#comment out the test below to use:
'''
if __name__ == "__main__":
    a = [3,1,5]; b = [5,9,2]
    l1 = UnorderedList(); l2 = UnorderedList()
    for i in a:
        l1.add(i)
    for i in b:
        l2.add(i)
    add_list(l1,l2)'''
#------------------------------------------------------------------------------------------------------------------
#2.5 Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
#DEFINITION
#Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node, so as to make a loop in the linked list.
#EXAMPLE
#input: A -> B -> C -> D -> E -> C [the same C as earlier]
#output: C
def circular(list_object):
    current = list_object.head
    l = []
    while current != None:
        if current.get_data() not in l:
            l.append(current.get_data())
        else:
            return current.get_data()
        current = current.get_next()
#comment out the test below to use:
'''
if __name__ == '__main__':
    d = ['C','E','D','C','B','A']
    L = UnorderedList()
    for i in d:
        L.add(i)		
    print(circular(L))	'''
#------------------------------------------------------------------------------------------------------------------	
    