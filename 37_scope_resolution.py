# variable scope ==> where a variable is visible and accessible
# scope resolution ==> (LEGB) Local > Enclosed > Global > Built in 

# Local scope ................

def func1():
    a = 1
    print (a)
    
def func2():
    b = 2
    print(b)
    
func1()
func2()

# Enclosed scope ...............

def func1():
    x = 5
    
    def func2():
        print(x)
    func2()
func1()

# Global Scope ..................

def func1():
    print (a)
    
def func2():
    print(a)

a = 8

func1()
func2()

# Built in scope.................

from math import e 

def func1():
    print(e)
    
# e = 5   ==> output is --> 5 // because a/c to LEGB global scope is first then built-in scope
func1()

