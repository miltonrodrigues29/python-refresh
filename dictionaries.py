# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()
# print(x)
# car["color"] = "red"
# car["model"]="hatchback"
# print(car)

# y = car.keys()
# print(y)

# if "model" in car:
#     print("Present")

# car.update({"year": 2020})
# car["model1"] = "sedan"
# print(car)


# m=car.get("model")
# print(m)

# f = car.items() #converts dic to list of tuples
# print(f)

# car["year"] = 2020
# print(car)
# print(f)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict.popitem()
# thisdict.pop("brand")

# print(thisdict)

# for x in thisdict:
#     print(thisdict[x])

# thisdict = {

#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for x in thisdict.values():
#     print(x)

# for y in thisdict.keys():
#     print(y)

# for x, y in thisdict.items():
#     print(x,y)

# newdict = thisdict.copy()
# print(newdict)



# #nested dictionaries

# airports = dict([
#     ("LHR", "London Heathrow"),
#     ("LGW", "London Gatwick")
# ])
# print(airports)

keys = ["IST", "SAW", "STN"]
values = ["Istanbul Airport", "Sabiha Gokcen International Airport", "London Stansted Airport"]

dictionary = dict(zip(keys,values))
print(dictionary)


# dictionary.pop("IST")
print(dictionary)


print(dictionary.get("IST")) #does not throw error if not found
print(dictionary["IST"]) #throws error if not found

print(dictionary.items())
print(dictionary.clear())
print(dictionary)




