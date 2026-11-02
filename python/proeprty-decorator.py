class Secret:

    def __init__(self, secret):
        self._secret = secret  # Private attribute

    @property
    def get_secret(self):
        return self._secret  # Public method to access the private attribute
     
    @get_secret.setter
    def set_secret(self, new_secret):
        if new_secret>8:
            self._secret = new_secret  # Public method to modify the private attribute


obj = Secret(5532224)
obj.set_secret = 12345678  # Modifying the private attribute using the public method
print(obj.get_secret)  # Accessing the private attribute using the public method