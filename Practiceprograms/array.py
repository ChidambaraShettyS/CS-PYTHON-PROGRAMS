# from array import *

'''
vals = array('i', [1, 4, 2, 5, 3])
vals1 = array('u', ['a', 'e', 'i', 'o', 'u'])
'''
'''
for i in range(len(vals)):
    print(vals[i])
'''
'''
for i in vals:
    print(i)
'''
'''
for i in vals1:
    print(i)
'''
'''
new_arr = array(vals.typecode, (a for a in vals))       # coping elements from one array to another

for i in new_arr:
    print(i)
'''
'''
new_arr = array(vals.typecode, (a*a for a in vals))

for i in new_arr:
    print(i)

j = 0
while j < len(new_arr):
    print(new_arr[j])
    j += 1
'''

# taking array values from user
'''
arr = array('i', [])

n = int(input("Enter the length of array : "))

for i in range(n):
    x = int(input("Enter the element : "))
    arr.append(x)


print(arr)
'''

'''
o/p:
Enter the length of array : 4
Enter the element : 1
Enter the element : 2
Enter the element : 3
Enter the element : 4
array('i', [1, 2, 3, 4])
'''

'''
arr = array('i', [1, 2, 3, 4, 5, 3])
val = int(input("Enter the value to SEARCH : "))
'''
'''
for i in range(len(arr)):           # Searching value manually
    if arr[i] == val:
        print(f"index {i},value {val}")
'''

'''
k = 0                   # Searching value manually
for ele in arr:
    if ele == val:
        print(k)
        break

    k += 1
'''
'''
print(arr.index(val))       # searching value using inbuilt method
'''

# ------------------------------- NumPy For Multi dimensional array's --------------------------------------------------
# Whenever we use numpy no need to import array module and no need assign type of the array while declaring

from numpy import *

'''
arr = array([1, 2, 3, 4, 5], int)       # Only int
arr1 = array([1, 2, 3, 'hi', 4, 5])     #

print(arr)              # o/p : [1 2 3 4 5]
print(arr1)             # o/p : ['1' '2' '3' 'hi' '4' '5']

print(arr.dtype)        # type : int32
print(arr1.dtype)       # type : <U11
'''

# Adding some value for existing values
'''
arr = array([1, 2, 3, 4, 5])

arr = arr + 5
print(arr)      # [ 6  7  8  9 10]
'''

# Adding Two Arrays (called vectorized operations)
'''
arr = array([1, 2, 3, 4, 5])
arr1 = array([6, 7, 8, 9, 10])

arr3 = arr + arr1

print(arr3)         # [ 7  9 11 13 15]
'''

# Concatenation of 2 arrays
'''
arr = array([1, 2, 3, 4, 5])
arr1 = array([6, 7, 8, 9, 10])

print(concatenate([arr, arr1]))         # [ 1  2  3  4  5  6  7  8  9 10]
'''


# Coping one array to another
'''
arr = array([1, 2, 3, 4, 5])

# arr1 = arr                # the memory will be for each variable 
# arr1 = arr.view()       # view() -> Shallow copy affects each other but also if its in diff memory
arr1 = arr.copy()       # copy() -> deep copy not affects each other

arr[1] = 10

print(arr)
print(arr1)
print(id(arr))
print(id(arr1))
'''

'''
o/p:
[1 2 3 4 5]
[1 2 3 4 5]
1573207393184
1573210644272
'''

# -------------- 2D array -------------------
'''
arr = array([
            [1, 2, 3],
            [4, 5, 6]
            ])

print(arr)
'''

'''
m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('1 2 3; 4 5 6; 7 8 9')

m3 = m1 + m2
m4 = m1 * m2

print(diagonal(m1))
print(m3)
print(m4)
'''

















































































































