class User:
    def __init__(self, user_id, name):
        self.name = name
        self.user_id = user_id


user_1 = User('001', 'joe')
user_2 = User('002', 'don')

print(user_1.name)
print(user_1.user_id)


class NAS:
    # This is a class attribute
    storage_capacity = '10TB'

    def __init__(self, location):
        # This is an instance attribute
        self.location = location

    # This is a method
    def report_status(self):
        return f"NAS located at {self.location} with storage: {self.storage_capacity}"


# Creating an object of the NAS class
my_nas = NAS('Data Center 1')

# Accessing the object's attribute
print(my_nas.location)  # Output: Data Center 1

# Calling the object's method
print(my_nas.report_status())  # Output: NAS located at Data Center 1 with storage: 10TB
