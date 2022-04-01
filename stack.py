#what is stack?
'''

linear data structure that stores items in a Last-In/First-our (LIFO) manner.

****use cases****

1. function calling in any programming language is managed using stack.
2. undo (ctrl-z) function
3. History back function (navigating to previous pages)in browsers like chrome.

'''


# implementing stacks using list

s=[]
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/India')
s.append('https://www.cnn.com/china')

s.pop()  # remove last appended s 
print(s)

last_s=s[-1]  
print(last_s)

'''
list is dynamic arary,it have to allocate new memory spaces and copy elements .
hence order is O(n)
hence it is nor recommended to use list for implementing stacks
recommended approch is using collection.deque -they are implemented
using double link list.Hence problem with lists is solved

'''

# implementing stacks using collection.deque


from collections import deque

stack=deque()
stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/India')
stack.append('https://www.cnn.com/china')
print(stack)



class Stack:

    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)


def reverse_string(string):

   stack=Stack()

   for s in string:
       stack.push(s)

   rev_str=''

   while stack.size()!=0:
       rev_str+=stack.pop()

   return rev_str


def is_match(str1,str2):

   match_dict={'}':'{',
               ']':'[',
               ')':'('
               }
   return match_dict[str1]==str2

def is_balanced(str):

    stack=Stack()
    for s in str:
        if s=='{' or s=='(' or s=='[':
            stack.push(s)

        if s=='}' or s==')' or s==']':
            if stack.size()==0:
                print("loop1")
                return False

            if not is_match(s,stack.pop()):
                print("loop2")
                return False
                
    return stack.size()==0
    

if __name__=="__main__":

    print(reverse_string("covid"))
    print(reverse_string("we will conquer COVID-19"))
    print(is_balanced("({a+b})"))
    print(is_balanced("{(a+b)}"))
   


#--------------------Excercise---------------------------------------#

'''
1.write a fuction in python that can reverse a string  using stack data structure.
use Stack class

reverse_string("we will conquer COVID-19")

2. write a function in python that check if paranthesis  in the string are balanced
or not.Possible paranthesis {}, (), [].use stack class.
is_balanced("({a+b})"))

matching first closing paranthesis obtained with last pushed open paranthesis.
'''

