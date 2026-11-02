
class Student:

    def __init__(self, name):
        self._name = name  # Private attribute

    @property
    def profile(self):
        return f"Student Name: {self._name}"  # Public method to access the private attribute    

    @profile.setter
    def profile(self, new_name):
        self._name = new_name  # Public method to modify the private attribute
        return f"Student Name updated to: {self._name}"  # Return a message indicating the update

obj = Student("Harsh Pardhi")
print(obj.profile)  # Accessing the private attribute using the public method
obj.profile = "John Doe"  # Modifying the private attribute using the public method 
print(obj.profile)  # Accessing the updated private attribute using the public method
