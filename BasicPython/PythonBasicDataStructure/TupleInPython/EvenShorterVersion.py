# tuple in list compression
c = {'a': 10, 'd': 1, 'c': 22}
print(sorted(c))
print(sorted([(v, k) for v, k in c.items()]))
"""
the above is list comprehension what is called  expression  
that generate all the element
"""
