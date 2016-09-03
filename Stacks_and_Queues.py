class Stack():
    def __init__(self):
        self.items = []
    #3.2 How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time
    def push(self,item):
        return self.items.append(item)
		
    def is_empty(self):
        return self.items == []
		
    def peek(self):
        return self.items[len(self.items)-1]
		
    #3.6 Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented. The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.
    def sort(self):
        new_list = self.items
        new_list.sort()
        return new_list		
		
		
    def pop(self):
        return self.items.pop()
		
    def size(self):
        return len(self.items) 
	
    def min(self):
        return min(self.items)
		
    def __str__(self):
        #for i in self.items:print(i)
        return str(self.min())
		
    def join(self):
        return ' '.join(self.items)
