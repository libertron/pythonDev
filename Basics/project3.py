# Many values to multiple variables at the sane time
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables at the same time
x = y = z = "Orange"
print(x,y,z)

#unpack a collection of values
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)