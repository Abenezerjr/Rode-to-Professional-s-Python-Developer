# function that returns something
def myFunction():
    result = 3 * 2
    return result


print(myFunction())
functionWith = myFunction() + 7
print(functionWith)


def nameChanger(firstname, lastname):
    formatedFirstname = firstname.title()
    formatedLastname = lastname.title()
    return f'{formatedFirstname}, {formatedLastname}'


result = nameChanger('aneDjd', 'jon')
print(result)

# Multiple value return
