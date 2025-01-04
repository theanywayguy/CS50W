people=[
    {"name": "John","house": "london"},
    {"name": "Bob","house": "Swiss"},
    {"name": "Luce","house": "Germany"},
]

#instead of this one line function we can use lambda to declare a one line function
def f(person):
    return person["name"]


#people.sort(key=f)
people.sort(key= lambda person:person["name"])
print(people)