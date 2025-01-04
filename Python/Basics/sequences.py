#Lists(arrays)-ordered
name=["Harry", "Smith", "bob"]
print(name)
print(name[0])
name.append("Dred") #adding to the list
name.sort()#auto sorting feature
print(name)


#Tuple(2d arrays)-ordered
coordinate=(10.0,20.0)
print(coordinate)


#set unique non-ordered/dublicated are ignored
s=set()
s.add(1)
s.add("James")
s.add(1)
print(s)
s.remove("James")
print(len(s))
print(f"this set has {len(s)} elements")
#dict dictionary similar to a map pairs of key-value
houses={"Harry":"Swiss", "Bob":"england"}
houses["John"]= "Swiss"
print(houses["Harry"])
print(houses["John"])