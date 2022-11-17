# 1. Fibonacci series

'''
def fibo(n):                # No of fibo nos
    n1 = 0
    n2 = 1
    print(n1, n2,end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1, n2 = n2, n3
'''

'''
def fibo(n):            # Upto n fibo
    n1 = 0
    n2 = 1
    print(n1, n2,end=" ")
    while n2 < n:
        c = n1 + n2
        n1, n2 = n2, c
        print(c, end=" ")
        '''
'''
0 1 1 2 3 5 
0 1 1 2 3 5 8 13 
0 1 1 2 3 5 8 13 21 
'''
'''
fibo(5)
print()
fibo(10)
print()
fibo(15)
'''

'''
def fibo(n):                # CHECK 

    n1 = 0
    n2 = 1
    l = []
    l.append(n1)
    l.append(n2)
    while n2 < n:
        c = n1 + n2
        n1, n2 = n2, c
        l.append(c)
    if n in l:
        print("Fibo")
    else:
        print("Not Fibo")

fibo(5)
fibo(4)
'''

# 2. Checking for prime number

# wap to print the series of PRIME nos b/n the range 1 to 50
'''
n = int(input("Enter No:"))
for i in range(1, n+1):
    ind = 0
    for j in range(2, i):
        if i % j == 0:
            ind = 1
    if ind == 0:
        print(i)
'''

# Prime r not
'''

n = int(input("No : "))
for n1 in range(2, n):
    if n % n1 == 0:
        print("Not Prime")
        break
else:
    print("Prime")
'''

# Prime in range
'''
for i in range(100, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
'''

# 3. String palindrome
'''
s = input("Enter the string to check for Palindrome : ")
if s == s[::-1]:
    print(f"{s} is Palindrome")
else:
    print(f"{s} is Not Palindrome")
'''
# 4. Integer palindrome
'''
n = input("Enter the string to check for Palindrome : ")
if str(n) == str(n)[::-1]:
    print(f"{n} is Palindrome")
else:
    print(f"{n} is Not Palindrome")
'''

# without typecasting
'''
n = int(input("enter the num : "))
rev = 0
while n != 0:                        # n > 0
    rev = rev * 10 + n % 10
    n //= 10

if n == rev:
    print("Given number is Palindrome")
else:
    print("Given number is Not Palindrome")
'''
# 5. Armstrong number
# 6. Avoiding deadlocks
# 7. Factorial Program
# 8. Reversing strings
'''
s = "String"
print(s[::-1])
'''
# 9. Removing repeated elements
'''
l = [1, 2, "hi", "hello", "hi", 1, 3, "bro"]
for i in l:
    if l.count(i) > 1:
        l.remove(i)

print(l)
'''

# 10. Printing patterns
# 11. Printing repetitive characters
'''
s = "Hi bro how are you welcome to club !!!"
rep_set = set()
for i in s:
    if s.count(i) > 1 and i !=" ":
        rep_set.add(i)
for i in rep_set:
    print(i, end=" ")
'''
# 12. LCM & GCD of two numbers
# 13. Square Root of a Number
'''
n = int(input("Enter the number to check the squre root of that : "))
print(n ** 0.5)
'''

# 14. Reversing an array in place



# 15. Reversing the order of words
# 16. Determining leap year
# 17. Performing binary search
# 18. Checking for anagrams
'''
s = "abcd"
s1 = "bcda"

flag = 0
for i in s:
    if i not in s1:
        flag = 1

if flag == 1:
    print("The given two strings are not anagram!!")
else:
    print("The given two strings are anagram!!")
'''

# 19. Designing a vending machine
# 20. Reversing a Number
# 21. First Unique Character of a String
'''
s = "Hi bro how are you"
for i in s:
    if s.count(i) == 1:
        print(f"The unique char in string : {i}")
        break
'''

# 22. Find Middle Element of a Linked List
'''
def middle_ele(l):
    n = len(l) // 2
    if len(l) % 2 == 0:
        print(f"Its a even length list we can take {l[n-1]} or {l[n]} as middle element")
    else:
        print(f"Its odd length list and middle element is : {l[n]} ")


middle_ele([1, 2, 3, 4, 5])
middle_ele([10, 20, 30, 40, 50, 60])
'''

# 23. Performing Pre-order Traversal
# 24. Pre-order traversal without recursion
# 25. Performing in-order traversal
# 26. In-order Traversal without Recursion
# 27. Performing Post-order Traversal
# 28. Post-order traversal without recursion
# 29. Printing all leaves of a Binary Tree
# 30. Sorting an Array using Quick-Sort
# Another one in below
'''
• Divide and Conquer algorithm
• Breaks down problem into multiple subproblems recursively until they become simple to solve
• Solutions are combined to solve original problem
• Running time
• O(n2) worst case
• O(n * log(n)) best and average case
• Quicksort:
1.Choose pivot element (Usually last or random)
2.Stores elements less than pivot in left subarray
  Stores elements greater than pivot in right subarray
3.Call quicksort recursively on left subarray
  Call quicksort recursively on right subarray'''

'''
def quick_sort(l, left, right):
    if left < right:
        partition_pos = partition(l, left, right)
        quick_sort(l, left, partition_pos - 1)
        quick_sort(l, partition_pos + 1, right)


def partition(l, left, right):
    i = left
    j = right - 1
    piv = l[right]

    while i < j:
        while i < right and l[i] < piv:
            i += 1
        while j > left and l[j] >= piv:
            j -= 1

        if i < j:
            l[i], l[j] = l[j], l[i]

    if l[i] > piv:
        l[i], l[right] = l[right], l[i]

    return i


l = [1, 4, 6, 5, 2, 7, 3, 8]
quick_sort(l, 0, len(l)-1)
print(l)
'''


# 31. Performing Bubble Sort

'''
def bubble_sort(col):
    print(f"Before sort : {col}")
    for p in range(1, len(col)):
        for j in range(0, len(col)-p):
            if col[j] > col[j+1]:
                col[j], col[j+1] = col[j+1], col[j]

    print(f"After sort : {col}")


bubble_sort([2, 5, 7, 1, 4, 6, 3])
'''

'''
def bubble_sort(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                # temp = l[j]
                # l[j] = l[j+1]
                # l[j+1] = temp
    print(l)


bubble_sort([1, 3, 5, 2, 8, 9, 6, 4])
'''

# Selection Sort

'''
def selection_sort(col):
    print(f"Before sort : {col}")

    for p in range(1, len(col)):
        n = p - 1
        for j in range(p, len(col)):
            if col[n] > col[j]:
                n = j
        col[p - 1], col[n] = col[n], col[p - 1]

    print(f"After sort : {col}")


selection_sort([2, 5, 7, 1, 4, 6, 3])
'''

'''
def selection_sort(l):
    for i in range(len(l)):
        min = i
        for j in range(i, len(l)):
            if l[j] < l[min]:
                min = j
        t = l[i]
        l[i] = l[min]
        l[min] = t
    print(l)


selection_sort([1, 3, 4, 5, 7, 6, 8, 2])
'''

# 32. Performing Insertion Sort
# Algo :

'''
def insertion_sort(col):
    print(f"Before sort : {col}")

    for p in range(1, len(col)):
        i = p
        while i != 0 and col[i] < col[i - 1]:
            col[i], col[i - 1] = col[i - 1], col[i]
            i -= 1

    print(f"After sort : {col}")


insertion_sort([2, 5, 7, 1, 4, 6, 3])
'''

'''
def insertion_sort(l):
    for i in range(len(l)):
        j = i
        while l[j-1] > l[j] and j > 0:
            l[j-1], l[j] = l[j], l[j-1]
            # or
            # t = l[j-1]
            # l[j-1] = l[j]
            # l[j] = t
            j -= 1

    print(l)


insertion_sort([1, 3, 4 , 6, 7, 5, 2, 8])
'''

# Performing Merge Sort

'''
def merge_sort(col):
    if len(col) > 1:
        mid = len(col) // 2
        ll = col[:mid]
        rl = col[mid:]
        merge_sort(ll)
        merge_sort(rl)

        i, j, k = 0, 0, 0

        while i < len(ll) and j < len(rl):
            if ll[i] < rl[j]:
                col[k] = ll[i]
                i += 1
                k += 1
            else:
                col[k] = rl[j]
                j += 1
                k += 1

        while i < len(ll):
            col[k] = ll[i]
            i += 1
            k += 1

        while j < len(rl):
            col[k] = rl[j]
            j += 1
            k += 1


n = int(input("Length of list : "))
a = [int(input("No : ")) for i in range(n)]
merge_sort(a)
print(a)
'''
# Performing Quick-Sort

'''
def pivot_place(col, first, last):
    pivot = col[first]
    li = first + 1
    ri = last

    while True:
        while li <= ri and col[li] <= pivot:
            li += 1
        while li <= ri and col[ri] >= pivot:
            ri -= 1
        if li <= ri:
            col[li], col[ri] = col[ri], col[li]
        else:
            break
    col[first], col[ri] = col[ri], col[first]
    return ri


def quick_sort(col, first, last):
    if first < last:
        p = pivot_place(col, first, last)
        quick_sort(col, first, p - 1)
        quick_sort(col, p + 1, last)


l = [3, 2, 5, 4, 1]
print(f"Before sort : {l}")
quick_sort(l, 0, len(l) - 1)
print(f"After sort : {l}")

'''

# 33. Transposing a Matrix
# 34. Printing all permutations of a String
# 35. Reversing a String in Place
# 36. Adding Matrices
# 37. Multiplying Matrices
# 38. Removing Spaces in a String
# 39. Reversing a Linked List
# 40. Finding the Length of a Linked List
# 41. Checking for loops in a linked list
# 42. Find start of looping in a linked list
# 43. Finding the middle element of a linked list
# 44. Find nth element from the tail of a linked list
# 45. Converting a linked list to a binary tree
# 46. Sorting a linked list
# 47. Performing bucket sort
# 48. Performing counting sort
# 49. Performing merge sort

# Above

# 50. Check if 2 strings are rotations of each other

# 51. Linear Search
# Algo :
'''
def ls(col, n):
    for i in col:
        if i == n:
            return True
    return False


print(ls([1, 2, 3, 4, 5], 2))
print(ls([1, 2, 3, 4, 5], 20))
'''

# OR

'''
def linear_search(l, n):
    for i in l:
        if i == n:
            print(f"Item {n} found at {l.index(i+1)}")
            break
    else:
        print(f"Item {n} not found")


linear_search([1, 2, 3, 4, 5], 4)
linear_search([1, 2, 3, 4, 5], 10)
'''


# 52. Binary Search
# While using binary search we must do sort the list first
# Algo :

'''
def binary_search(col, val):
    li = 0
    hi = len(col)-1

    while li <= hi:
        mid = (li + hi) // 2

        if val == col[mid]:
            return True
        elif val < col[mid]:
            hi = mid -1
        elif val > col[mid]:
            li = mid + 1

    return False


print(binary_search([10, 20, 30, 40, 50], 40))
print(binary_search([10, 20, 30, 40, 50], 400))
'''

'''
def BS(l, n):
    l.sort()
    low = 0
    upp = len(l)

    while low < upp:
        mid = (low + upp) // 2
        if l[mid] == n:
            print(f"Item {n} found at {mid}")
            break
        else:
            if l[mid] < n:
                low = mid
            else:
                upp = mid
    else:
        print(f"Item {n} not found")


BS([10, 20, 30, 40, 50], 40)
BS([10, 20, 30, 40, 50], 7)
BS([10, 20, 30, 40, 50], 100)
'''

'''
pos = -1


def BS(l, n):
    l.sort()
    low = 0
    upp = len(l)-1
    
    while low <= upp:
        mid = (low + upp) // 2
        if l[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if l[mid] < n:
                low = mid + 1
            else:
                upp = mid - 1

    return False


if BS([1, 4, 2, 3, 8, 5], 5):
    print("Item Found")
else:
    print("Item Not Found")
'''

# Simple one

'''
def binary_search(l, n):
    l.sort()
    low = 0
    high = len(l) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if l[mid] < n:
            low = mid + 1
        elif l[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1


result = binary_search([2, 4, 10, 40, 3], 3)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in list")
'''

# Using Recursion

'''
def binary_search(l, low, high, n):
    if high >= low:
        mid = (high + low) // 2
        if l[mid] == n:
            return mid
        elif l[mid] < n:
            return binary_search(l, mid + 1, high, n)
        else:
            return binary_search(l, low, mid - 1, n)
    else:
        return -1


l = [2, 3, 4, 10, 40]
n = 10

result = binary_search(l, 0, len(l) - 1, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
'''































































































