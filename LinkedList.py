

# linkedlist?

'''
like arrays,Linked list is a linear data structure.unlike arrays, linkedlist elements are
not stored at a contiguous location,they are allocated at random memory space and are
linked using pointers which store memory location of another data. 

python donit have a standard libray for linkedlist.

why linked list?

In arrays insertion is not efficent since it involve swaping and copying into new
memory locations(python lists are dynamic array)


'''
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
         node = Node(data,self.head)
         self.head = node


    def print_data(self):
         if self.head is None:
              print("my linked list is empty")
              return
         

         itr=self.head
         llstring = ''

         while itr:
              llstring+=str(itr.data)+"-->"
              itr=itr.next
         print(llstring)

    def insert_at_end(self,data):
         if self.head is None:
              self.head = Node(data,None)
              return
         itr=self.head
         while itr.next:
               itr=itr.next
         itr.next =Node(data,None)


    def insert_values(self, data_list):
         self.head = None
         for data in data_list:
              self.insert_at_end(data)

    def get_length(self):
         
         itr=self.head
         count=0
         while itr:
              itr=itr.next
              count+=1
         return count

      

    def remove_at(self,index):#since python have automatic grabage collection
                              #when a variable is no longer referenced,it will be removed from memory.

       
         if index<0 or index>=self.get_length():
               raise Exception("invalid index")

         if index == 0:
              self.head = self.head.next
              return

         count=0
         itr=self.head

         while itr:
               if count == index-1:
                  itr.next = itr.next.next
                  break
               itr=itr.next
               count+=1

               
    def insert_at(self,index,data):

     
         if index<0 or index>=self.get_length():
               raise Exception("invalid index")

         if index == 0:
              self.insert_at_begining(data)
              return

         count=0
         itr=self.head

         while itr:
               if count == index-1:                  
                    node=Node(data,itr.next)
                    itr.next = node
                    break
               itr=itr.next
               count+=1
     
              
    def insert_after_value(self,data_after,data_to_insert):
         
         if self.head is None:
              return

         if self.head.data==data_after:
               self.head_next=Node(data_to_insert,self.head.next)
               return
          
         itr=self.head
         while itr:
              if data_after==itr.data:
                   itr.next=Node(data_to_insert,itr.next)
                   break

              itr=itr.next

    def remove_by_value(self, data):

          if self.head is None:
               return
          
          if self.head.data == data:
               self.head =self.head.next
               return

          itr=self.head
          while itr.next:
               if data==itr.next.data:
                    itr.next=itr.next.next
                    break
               itr=itr.next
             
          

     

    # remove first node that contain data

       


     
               


if __name__=="__main__":

     ll=LinkedList()
     ll.insert_values(["banana","mango","grapes","orange"])
     ll.print_data()
     ll.insert_after_value("orange","apple")
     ll.print_data()
     ll.remove_by_value("orange")
     ll.print_data()
     ll.remove_by_value("banana")
     ll.print_data()
     ll.remove_by_value("mango")
     ll.print_data()
     ll.remove_by_value("apple")
     ll.print_data()
     ll.remove_by_value("grapes")
     ll.print_data()
     ll.insert_after_value("orange","apple")
     ll.print_data()
     
     

     


#-----------------------------Excercise 1--------------------------------------------#

'''
1. add two methods

def insert_after_value(self,data_after,data_to_insert)

    search for first occurence of the data_after in the linkedlist
    now insert data_to_insert after data_after node.

def remove by value(self, data)

    # remove first node that contain data


Now make following calls

ll.LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insrt apple after mango
ll.print()
ll.remove_by_value("orange")# remove orange from list
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")


'''
#-----------------------------------Excercise 2---------------------------#
'''
implement double link list. It has previous reference and next reference as well.
so that you can iterate in forward and backward direction.

class Node:

    def __init__(self, data=None, next=None, prev=None):

         self.data=data
         self.next=next
         self.prev=prev

add followig method

def print_forward(self):
  #print list in forward direction

def print_backword(self):
  #print list in reverse direction

implement all other call in regular linked list class in double linked list.
'''



class Node:

     def __init__(self, data=None, next=None, prev=None):
          self.data=data
          self.next=next
          self.prev=prev
     

class DoubleLinkedList:

     def __init__(self):
          self.head=None

     def print_forward(self):

          if self.head is None:
               print(" Linked list is empty")
               return
          itr=self.head

          llstring=''
          while itr:
               llstring+=itr.data+"-->"
               itr=itr.next
          print("ll in forward",llstring)
          
     def print_backward (self):

          if self.head is None:
               print(" Linked list is empty")
               return
          
          last_node=self.get_last_node()
          itr=last_node
          
          llstring=''
          while itr:
               llstring+=itr.data+"-->"
               itr=itr.prev
          print("ll in reverse",llstring)


     def get_last_node(self):

               itr=self.head
               while itr.next:
                    itr=itr.next
               return itr
          


     def insert_at_begining(self,data):

          if self.head is None:
              node=Node(data, self.head, None)
              self.head=node

          else:
               node=Node(data, self.head, None)
               self.head=node
               self.head.prev=node

     
     def insert_at_end(self, data):

          if self.head is None:
               self.head=Node(data, None, None)
               return
          
          itr=self.head
          
          while itr.next:
               itr=itr.next

          itr.next=Node(data, None, itr)

     def get_length(self):
          count=0
          itr=self.head
          while itr:
               itr.next
               count+=1
          return(count)

     def insert_at(self, index, data):

          if index<0 or index>get_length():
               raise Exception("invalid syntax")

          if index==0:
               self.insert_at_begining(data)

          itr=self.head

          count=0
          while itr:
               if count==index-1:
                    node=Node(data, itr.next, itr)
                    if node.next:
                         node.next.prev=node
                    itr.next=node
                    break
               
               itr=itr.next
               count=count+1
               
               
     def remove_at(self, index, data):

          if index<0 or index>get_length():
               raise Exception("invalid syntax")

          if index==0:
               self.head=self.head.next
               self.head.prev=None
               return

          

          itr=self.head

          count=0
          while itr:
               if count==index:
                    itr.prev.next=itr.next
                    if itr.next:
                         itr.next.prev=itr.prev
                   
                    break
               
               itr=itr.next
               count=count+1
                        

          

     def insert_values(self,data_list):
          self.head=None
          for data in data_list:
               self.insert_at_end(data)

          

if __name__=="__main__":

     dll=DoubleLinkedList()
     dll.insert_values(["banana","mango","grapes","orange"])
     dll.print_forward()
     dll.print_backward()
     dll.insert_at_begining("fig")
     dll.insert_at_end("pineapple")
     dll.print_forward()
               

          












