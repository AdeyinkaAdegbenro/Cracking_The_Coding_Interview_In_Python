#! python3
# CRACKING THE CODING INTERVIEW by GAYLE LAAKMANN  4th Edition [in Python 3]
#Chapter 1 | Arrays and Strings
#1.1 Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
def uniqueXters(string):
    dico = {}
    for  i in string:
        if i not in dico:
            dico[i] = 0
        else:
            return False
    return True
	
#1.2 Write code to reverse a C-Style String. (C-String means that 'abcd' is represented as five characters, including the null character.)
def reverse_string(string):
    return string[::-1]

#1.3 Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.	
def remove_duplicates(string):
    new = []
    [new.append(i) for i in string if i not in new]
    return ''.join(new)	
	
#1.4 Write a method to decide if two strings are anagrams or not.
def is_anagram(a,b):
    if len(a) == len(b):
        a= list(a); b=list(b)
        a.sort(); b.sort()
        if a == b:
            return True
    return False
	
#1.5 Write a method to replace all spaces in a string with %20.
def replace_space(string):
    import re
    pattern = re.compile(r'\s+')
    return pattern.sub('%20', string)
	
#1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
def rotate_image(matrix):#example argument for rotate_image:[[1,2,3],[4,5,6],[7,8,9]] 
  b = []    #matrix container
  for j in range(len(matrix[0])):
    a = []   #rows container
    for i in range(len(matrix)-1,-1,-1):
      a.append(matrix[i][j])
    b.append(a)
  return b

#1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
def set_zero(matrix):#example argument for set_zero: [[1,2,3],[4,0,6],[7,8,0]]
    positions = []
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if matrix[a][b] == 0:
                positions.append((a,b))  #storing the postions of the zeros in a list for use below
    for i,j in positions:
        matrix[i] = [0,0,0]   #setting the rows to zero
        for s in range(len(matrix)):
            matrix[s][j] = 0  #setting the columns to zero
    return matrix
	
#1.8 Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., waterbottle is a rotation of erbottlewat).
def isSubstring(s1,s2):
    if len(s1) == len(s2) and s2 in s1+s1:
        return True
    return False