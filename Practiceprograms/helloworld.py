# print("Hello World")

'''
num = int(input("Enter the number : "))

if num == 5:
    print("The entered number is 5.")
else:
    print("The entered number is not 5.")

'''

# Wapt check for the largest count or valued key and for the key with its value
# aabbbc  ---> b
# aabbbc  ---> a2b3c1

'''
d = {}
l = []


def largecount(string):
    global d, l
    for i in string:
        count = 0
        for j in string:
            if i == j:
                count += 1
        d[i] = count
    print()
    print(d)
    l = list(d.values())
    l.sort()
    
    for k, v in d.items():
        print(k, v, end=" ")           # For Key with Its value in series
        # if v == l[-1]:
        #     print(k, end='')         # For largest valued Key


largecount("aaabbbbc")
largecount("abcc")
largecount("abc")

'''



























































