
# ------------------------- Pattern Programs Using Nested For Loop ------------------------------

'''
for num in range(1, 6):
    for n in range(1, num):
        print(n)
'''
'''
for num in range(1, 6):
    for n in range(1, num + 1):
        print(n, end=" ")
    print()
'''
'''
o/p:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
'''
for num in range(5, 0, -1):
    for n in range(1, num + 1):
        print(n, end=" ")
    print()
'''
'''
o/p:
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
'''
n = int(input("Enter the no of rows n col : "))     # n = 5
for i in range(1, n+1):           # i for row
    for j in range(1, n+1):       # j for clo
        print("*", end=" ")
    print()
'''
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
'''
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
'''
'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
'''
'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i >= j:
            print("*", end=" ")
    print()
'''
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i + j >= n+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

'''
Enter the no : 5
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i <= j :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Enter the no : 5
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i + j <= n+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Enter the no : 5
* * * * * 
* * * *   
* * *     
* *       
*    
'''

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j >= 1 or j == n and i <= n or i == n and j <= n or j == 1 and j >= 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

'''
Enter the no : 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''



'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j == n or i == n or j == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Enter the no : 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

'''
Enter the no : 5
*         
  *       
    *     
      *   
        * 
'''


'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i + j == n+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Enter the no : 5
        * 
      *   
    *     
  *       
*         
'''
'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i + j == n+1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Enter the no : 5
*       * 
  *   *   
    *     
  *   *   
*       * 
'''

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j == n or i == n or j == 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

'''
Enter the no : 5
* * * * * 
* *     * 
*   *   * 
*     * * 
* * * * * 
'''

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Enter the no : 5
  $ $ $ $ 
$   $ $ $ 
$ $   $ $ 
$ $ $   $ 
$ $ $ $   
'''
'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j:
            print("#", end=" ")
        elif i > j:
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Enter the no : 5
  # # # # 
$   # # # 
$ $   # # 
$ $ $   # 
$ $ $ $   
'''

# A

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j != 1 and j != n or \
                n >= j and i == (n+1)//2 or \
                j == n and i != 1 or\
                j == 1 and i != 1:

            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Enter the no : 5
  * * *   
*       * 
* * * * * 
*       * 
*       *
'''

# CS

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j and i == 1 or\
                j == 1 and i + j <= n and i + j >= 3 or\
                i == n and i + j != n+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or \
                n >= j and i == (n+1)//2 or\
                j == 1 and i + j > 2 and i + j < n - 1 or\
                i + j == 9:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''


'''
Enter the no : 5
  * * * * 
*         
*         
*         
  * * * * 

* * * * * 
*         
* * * * * 
        * 
* * * * * 
'''

# P

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j != n or j == 1 and i <= n or\
                i < (n + 1)//2 and i > 1 and j == n or\
                i == (n+1)//2 and j != n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# Y

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i + j == (n+1) and i <= j or\
                i == j and i <= (n + 1)//2 and j <= (n+1)//2 or\
                j == (n+1)//2 and i >= j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# T

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j == (n+1)//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# H
'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == n or n >= j and i == (n+1)//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# O

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j != 1 and j != n or\
                i == n and j != 1 and j != n or\
                j == 1 and i != 1 and i != n or\
                j == n and i != 1 and i != n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# N

'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == n or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
# -------------------------------------------------------
'''
n = int(input("Enter the no : "))           # Only for 5 as count
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == (n+1)//2 or j == (n+1)//2 or i + j == n - 1 or\
                i + j == n + 1 and j != 1 and j != n or\
                i + j == n + 3:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
Enter the no : 5
    #     
  # # #   
# # # # # 
  # # #   
    #   
'''
'''
n = int(input("Enter the no : "))           # Only for 5 as count
for i in range(1, n+1):
    for j in range(1, n+1):
        if :
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# GR

# G
'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j != 1 and j != n or\
                i == n and j != 1 and j != n or\
                j == 1 and i != 1 and i != n or\
                j == n and i >= (n+1)//2 and i != n or\
                i == (n+1)//2 and j >= (n+1)//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# R
'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j != n or j == 1 and i <= n or\
                i < (n + 1)//2 and i > 1 and j == n or\
                i == (n+1)//2 and j != n or\
                i > j and (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# Heart

'''n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j != 1 and j != n and j != (n+1)//2 or\
                i == 2 and j in (1, 4, 7) or\
                i + j == n + 3 and i <= n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''


'''
for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or\
                (row == 1 and col % 3 == 0) or\
                (row - col == 2) or\
                (row + col == 8):  
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
  * *   * *   
*     *     * 
*           * 
  *       *   
    *   *     
      *       
'''

# LN
'''
n = int(input("Enter the no : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or i == j or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
n = 7
L = [[" " for i in range(n)] for j in range(n)]
N = [[" " for i in range(n)] for j in range(n)]

for row in range(n):
    for col in range(1, n+1):
        if col == 0 or row == n - 1:
            L[row][col] = "*"

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if col == 0 or col == row or \
                (col == n - 1 and row <= n-1):
            N[row][col] = "*"

for i in range(n):
    for j in range(n):
        print(L[i][j], end="")
    print()
    for k in range(n):
        print(N[i][k], end="")
    print()
'''
# LN
'''
n = 7

for row in range(1, n+1):
    for col in range(1, n+1):
        if col == 0 or row == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end=" ")

    for col in range(1, n+1):
        if col == 0 or col == row or col == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

'''n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()'''

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
'''
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
'''

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 

'''

'''
n = 5
for i in range(1, n + 1):
    for j in range(n, i-1, -1):
        print(j, end=" ")
    print()
'''
'''
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
'''

'''
u = ord("A")
l = ord("y")
n = 5

for i in range(n):
    for j in range(n):
        print(chr(u) + chr(l), end=" ")
        u += 1
        l -= 1
    print()
'''

'''
Ay Bx Cw Dv Eu 
Ft Gs Hr Iq Jp 
Ko Ln Mm Nl Ok 
Pj Qi Rh Sg Tf 
Ue Vd Wc Xb Ya 
'''
'''
u = ord("A")
l = ord("y")
n = 5

for i in range(n):
    for j in range(n):
        if i == j:
            print(chr(u) + chr(l), end=" ")
        else:
            print(" ", end=" ")
        u += 1
        l -= 1
    print()
'''
'''
Ay         
  Gs       
    Mm     
      Sg   
        Ya 

'''
'''
n = int(input("Enter Row N Col : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i, end=" ")
        i += n
    print()
'''
'''
Enter Row N Col : 5
1 6 11 16 21 
2 7 12 17 22 
3 8 13 18 23 
4 9 14 19 24 
5 10 15 20 25 
'''









































































































































































































































































































