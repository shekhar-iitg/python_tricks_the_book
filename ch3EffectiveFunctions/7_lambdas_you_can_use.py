tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
sorted_tuples = sorted(tuples, key = lambda x: x[1])
print(sorted_tuples)

print(sorted(range(-5, 6), key=lambda x: x*x))
