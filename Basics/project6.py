# testing python datatypes
# In python variable type defined either by assigning value or by using datatype function to add value
# Variable declaration

#string - function str()
a = "Hello World"
# int - function int()
b = 20
# float - function float()
c = 20.5
# complex - function complex()
d = 1j
# list - function list()
e = ["a","b","c"]
# tuple - function tuple()
f = ("a","b","c")
# range
g = range(6)
# dict / dictionnary - function dict()
h = {"a" : "1", "b" : "2", "c" : 3}
# set - function set()
i = {"a", "b", "c"}
# frozenset - function frozenset()
j = frozenset({"a", "b", "c"})
# boolean - function bool( [ any value != 0 is considered as true ] )
k = True # note that boolean are in Capitalize letter
# byte - function bytes() byte with (s)
l = b"Hello"
# bytearray
m = bytearray(6)
# memoryview, you put bytes in memoryview (it's a memory allocation)
n = memoryview(bytes(6))
# none type
o = None