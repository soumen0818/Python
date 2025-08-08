# Property ==> Decorator used to define a method as a property (it can be accessed like an attribute)
#          Benifits ==> add additional logic when read , write, or delete attributes gives you  getter , setter, and deleter method.


# Getter
class Alphabet:
    def __init__(self, value):
        self._value = value

    def getValue(self):
        print("Getting value")
        return self._value

    def setValue(self, value):
        print("Setting value to " + value)
        self._value = value

    def delValue(self):
        print("Deleting value")
        del self._value

    value = property(getValue, setValue, delValue)

# Usage
x = Alphabet("soumen")
print(x.value)

x.value = "some"
del x.value
              

