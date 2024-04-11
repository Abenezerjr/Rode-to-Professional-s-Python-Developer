# nesting is adding inside list dictionary or reverting


"""
Nesting:-
    dictionary={
    'key:[list],
    'key:{dict},
    }
"""

capitals = {
    'France': {"citiesVisited": ['Paris', 'Lille', 'dijon']},
    'Germany': {"citiesVisited": ['Berlin', 'hamburg'], 'totalVisited': 12, "featureVisited": ['parameterised']}
}
# example2 nested dice inside a list

projectNames = [
    {
        'title': 'E-commerce Website',
        'description': 'what is E-commerce Website',
        'worker': ['abenezer', 'bacha', 'mekonen']
    },
    {
        'title': 'Weather app',
        'description': 'A Weather app of farmers',
        'worker': ['Alemaz', 'gobena', 'heroot']
    },
    {
        'title': ' Mobile app',
        'description': 'mobile app of student',
        'worker': ['asefa', 'kenekayehu', 'meneber']
    },
]


def addNewProject(title, description, worker):
    newDictionary = {
        'title': title,
        'description': description,
        'worker': worker
    }

    projectNames.append(newDictionary)


#
# print(projectNames[0]['title'])
#
# for i in projectNames:
#     print(i['worker'])

addNewProject('CSC', 'wow about coffee', ['anent', 'joe', 'don'])
print(projectNames)

for i in projectNames:
    print(i)