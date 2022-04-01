'''

BigO notations

Used to measure how
running time or space requirement of your program grows
as input sizes  grows

Rules for bigO notations

1.keep only fastest growing term
2.Drop constants

=============================================================

[1] Order(n)  -  O(n)


              n       time
size(arr) --> 100  --> 0.22ms
          --> 10000 --> 3 ms

size of arary and propotional and hence linear relation

t=an+b

1. keep only fastest growing term

 t=an

2. Drop constants

   t=n

   ==>  complexity is order of n ==>  O(n)

'''
# example of order(n)

def get_squared_numbers(nos):

    list_nos=[]
    for i in list_nos:
        list_nos.append(i*i)
    return list_nos

nos=[3,2,1]
get_squared_numbers(nos)


# here as size increases ,iteration also increase
#and hence running time will increase.
# size in linear relation with iteration
# complexity order of n O(n)


'''

=================================================================


[2] Order(1)  -  O(1)


              n       time
size(arr) --> 100  --> 0.22ms
          --> 10000 --> 0.23 ms

constant relation b/w time and size of array 

t=a

1. keep only fastest growing term

 t=a

2. Drop constants

   t=1

   ==>  complexity is order of 1 ==>  O(1)

'''

def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe

print(find_first_pe([1000,2000,4000],[10,20,30],1))

# here we are giving index thus avoiding for loop
# for getting only neccessary result of respective index
# size of array and running time are constant
# here complexitiy is order of 1 O(1)

'''

===================================================================

[3] Order(n^2)  -  O(n^2) two for loop simultaneously


              n       time
size(arr) --> 100  --> 0.22ms
          --> 10000 --> 5 ms

relation b/w time and size of array 

t=a*n^2+b



1. keep only fastest growing term

 t=a*n^2

2. Drop constants

   t=n^2

   ==>  complexity is order of n^2==>  O(n^2)
 
Note : two for loop simultaneously and one for loop extra

then relation become n^2 +n+c

n+c is negligible  so  oders is O(n^2) itself


'''
numbers=[3,6,2,4,3,4]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
            print( str(numbers[i]) +" is duplicate ")
            break

# here two for loops
# so order of complexity O(n^2)

# when we add one more iteration in above code

for i in numbers:
    if i%2==0:
      print("even")
      
# in this case  qquation is n^2 +n+c
# since n+c is negligible
# so  oders is O(n^2) itself


'''
 ===================================================================

[4] Order(log n)  -  O(log n)


in binary search in every iteration size of array is reduced to half
relation b/w time and size of array 

k=n/2^k     k=iteration

in worse case k=1 

1= n/2^k

2^k=n

applying log

log 2^k =log n

k log2=logn

log2 -constant

   ==>  complexity is order of log n==>  O(logn)
'''

#Normal search will take O(n) complexity


for i in range(len(numbers)):
               if numbers[i] == 2:
                 print(i)

'''

'''
