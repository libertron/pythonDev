#variable scope
#global
x = "awesome"

def myfunc():
    print('python is ' + x)

myfunc()

#local scope
def myNewFunc():
    x = "fantastic"
    print("Python is " + x)

myNewFunc()

#create a global variable inside a function / override a global variable from a function

def myLastFunc() :
    global x
    x = "Powerfull"
    print("Python is " + x)

myLastFunc()