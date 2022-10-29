# named tuple, default dict
# string, list, tuple, namedtuple, dictionary, array module, set
# list comprehension, context manager -> opening files / clean-up
# math -> pi, sqrt, cos, sin, atan, scipy, numpy, pandas, pytest, matplot

from math import pi

print(pi)

s = "12345"

print(s[::-1])

d = {"a":1,"b":2}

print(d["a"])
print(d.keys())
print(len(d))

for key in d.keys():
    print(key)

l = [1,2,3,4]
l[0] = "b"
l[1] = "c"
l[2] = 3
l[3] = "a"
l.append(2)

print("l3:", l[3])
print("l:", l)

decimal_string = [int(x) for x in s]
print(decimal_string)

slice = l[1:3]
print(slice)
l.reverse()
print(l)
print(l[::-1])
print(l)
# elements must all be of the same type
dl = [3,2,5,4]
print(dl.sort())
print(dl)

def factorial(n):
    if n != 1:
        return n*factorial(n-1)
    else:
        return 1

f4 = factorial(4)
print("f4:", f4)
assert f4 == 24

def binary_to_decimal(bin_string):
    decimal_value = 0
    powers = len(bin_string)-1
    for digit in bin_string:
        if digit == "1":
            decimal_value += 2**powers
        powers -= 1
    return decimal_value

print("decimal:", binary_to_decimal("1001"))

def decimal_to_binary(decimal, l=list()):

    if decimal >= 1:
        decimal_to_binary(decimal//2,l)
    l.append(str(decimal % 2))

    return "".join(l)

print(decimal_to_binary(9))

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
                self.left.print_tree()
        print(self.data)
        if self.right:
                self.right.print_tree()

root = Node(10)
root.insert(3)
root.insert(2)
root.print_tree()

s = {2,3}
print(type(s))
print("set size:", len(s))
s.remove(2)
print("set:", s)


