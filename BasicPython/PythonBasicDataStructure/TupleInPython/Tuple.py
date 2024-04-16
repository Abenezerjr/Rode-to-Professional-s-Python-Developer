# tuple are like list but Tuple are 'immutable
"""
tuples are another kind of sequence that functions much like a list
they have elements which are indexed starting at 0, but you can't modify it

Tuples are more efficient

Since Python does not have to build tuple structures to be modifiable,
they are simpler and more efficient in
terms of memory use
and performance than lists

So in our program when we are making "temporary variables" we prefer tuples over lists
"""
names = ('joe', 'ben', 'sally',)
print(type(names))
print(names)
print(names[2])

"""
tuples and Assignment 
we can also use a tuple on the left-g=hand side of the assignment statement
"""
(x, y) = (4, 'joe')
print(y)
print(x)
(a, b) = (99, 98)
print(a)
print(b)
# tuples and dic
d = dict()
d['joe'] = 2
d['mo'] = 4
print(d)
print('_______')
for (a, b) in d.items():  # items methode in dic return a list of (kay,value) tuples
    print(a, b)
print("++++++++++++++")
t = d.items()
print('TTTT')
print(t)

# sorting list of tuples

d = {'a': 10, 'b': 1, 'c': 22}
d.items()  # change tuple of list tuple
print(d.items())

print(sorted(d.items()))  # change a list of tuple
