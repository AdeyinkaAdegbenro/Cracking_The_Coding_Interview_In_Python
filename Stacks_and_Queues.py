#! python3
# CRACKING THE CODING INTERVIEW by GAYLE LAAKMANN  4th Edition [in Python 3]
#Chapter 3 | Stacks and Queues

class Stack():
    '''the Stack abstract data type'''
    def __init__(self):
        self.items = []
        self.min_items = []
	
    #3.2 How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time
    def push(self, item):
        self.items.append(item)
        if not self.min_items or item <= self.min():
            self.min_items.append(item)

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        # returns the most recent addition to the stack
        item = self.items.pop()
        if item == self.min():
            self.min_items.pop()
        return item

    def size(self):
        # returns the number of items in the stack
        return len(self.items)

    def min(self):
        # returns the minimum item in the stack
        return self.min_items[-1]
		
    def popAt(self,index):
        return self.items.pop(index)
		
    def __str__(self):
        n = 0
        while  n < len(self.items) :
            print(self.items[n])
            n += 1
		
class Set_of_Stacks:
    #   3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
    #   Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
    #   Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
       
    def __init__(self):
        self.set_of_stacks = Stack()
        self.single_stack = Stack()
		
    def push(self, item):
        if self.single_stack.size() < 10:
            self.single_stack.push(item)
        elif self.single_stack.size() == 10:
            print('Stack Overflow','creating new stack', sep='---')
            self.set_of_stacks.push(self.single_stack)
            self.single_stack = Stack()
            self.single_stack.push(item)
			
    def pop(self):
        if self.single_stack.size() > 0:
            return self.single_stack.pop()
        else:
            current = self.set_of_stacks.pop()  #pops set of stack
            value = current.pop()
            if current.size() > 0 :
                self.set_of_stacks.push(current)
            return value				 #pops the substack from line above
			
    def popAt(self, index):
        #FOLLOW UP: Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
        if self.set_of_stacks.size() >= index:
            if index == self.set_of_stacks.size():
                popped_answer = self.single_stack
                self.single_stack = Stack() #assign an empty stack to single_stack as replacement for the popped one above
                return popped_answer
            else:
                return self.set_of_stacks.popAt(index)		


#--------------------------------------------------------------------------------------------------------------------
#3.4 In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (e.g., each disk sits on top of an even larger one). You have the following constraints:
#(A) Only one disk can be moved at a time.
#(B) A disk is slid off the top of one rod onto the next rod.
#(C) A disk can only be placed on top of a larger disk.
#Write a program to move the disks from the first rod to the last using Stacks.
class Tower_of_Hanoi:
    def __init__(self,n):
        self.diskNums  = n
        self.towers = [Stack() for i in range(3)]
        for i in range(n,-1,-1): 
            towers[0].push(i)
			
    def move_disk(pole1, pole3):
        towers[pole3].push(towers[pole1].pop())
		
    def move_Tower(n, pole1,pole2,pole3):
        if n == 0:
            move_disk(pole1,pole3)
        else:
            move_Tower(n-1, pole1,pole3,pole2)
            move_disk(pole1,pole3)
            move_Tower(n-1, pole2,pole1,pole3)				
#------------------------------------------------------------------------------------------------------------------	
#3.5 Implement a MyQueue class which implements a queue using two stacks.
class MyQueue:
    def __init__(self):
        self.front_stack = Stack()  #front of the queue
        self.rear_stack = Stack()   #back of the queue
		
    def is_empty(self):
        return self.front_stack.size() == 0
		
    def enqueue(self, item):
        self.rear_stack.push(item)           
        self.front_stack.push(self.rear_stack.pop())
		
    def dequeue(self):
        return self.front_stack.popAt(0)
		
    def size(self):
        return self.front_stack.size()	
		
#--------------------------------------------------------------------------------------------
#3.6 Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented. The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.        
def sorter(s1,s2,s3):
    #an helper function to the sort() method below
    while not s1.is_empty() :
        if s1.peek() <= s2.peek():
            s2.push(s1.pop())
        else:
            while not s2.is_empty() :
                if s2.peek() <= s1.peek():
                    s3.push(s2.pop())
                else:
                    break
            s2.push(s1.pop())
            while not s3.is_empty():
                s2.push(s3.pop())
    if s1.is_empty():
        return s2
    return sorter(s1,s2,s3)	
	
def sort(stack_object):
    s1 = stack_object
    s2 = Stack()
    s3 = Stack()
    s2.push(s1.pop())
    return sorter(s1,s2,s3)
    #TEST CASE below \|/
    '''if __name__ == "__main__":
           stack_object = Stack()
           d = [4,7,9,3,2,0,8,1,5,6]	
           for i in d:
               stack_object.push(i)
	
           sorted_stack = sort(stack_object)
           for i in range(10):
               print(sorted_stack.pop())
    '''
		


	

	
