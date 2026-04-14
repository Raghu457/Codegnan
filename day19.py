'''
Generators
----------
-->This is a special type of function that return an ITERATOR which once at a time

yield
-----
--> It will take a pause and again resume,this is not a nrml keyword cannot be used in the nrml functions
--> This is used to produce a value and pause execution.

Next()
------
-->This is used to get next value from a generator
-->When the value is finished, it will stop the iterator

'''

'''
def my_generator():
    yield 1
    yield 2
    yield 3
an=my_generator()
print(next(an))
print(next(an))
print(next(an))
'''

'''
def square_gen(n):
    for i in range(n):
        yield i*i
for val in square_gen(5):
    print(val)
'''

'''

def square_gen(n):
    for i in range(n):
        yield i
        
for val in square_gen(100):
    print(val)
'''

