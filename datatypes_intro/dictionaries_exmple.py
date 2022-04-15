# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# print(thisdict)
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
#
# }
# print(thisdict["brand"])
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
#
# }
# print(len(thisdict))
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964,
#     "colors":["red","white","blue"]
#
# }
# print(thisdict)
# print(type(thisdict))

# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
#
# }
# x=thisdict.keys()
# print(x)

# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
#
# }
# x=car.items()
# print(x)
# car["color"]="red"
# print(x)

# x=thisdict.values()
# print(x)
# x=car.values()
# print(x)
# car["color"]="red"
# print(x)
# x=thisdict.items()
# print(x)
# if "model" in thisdict:
#     print("yes,'model' is one of the keys in the thisdict dictionary")
# thisdict["year"]=2018
# print(thisdict)
# thisdict.update({"year":2020})
# print(thisdict)
# thisdict["color"]="red"
# print(thisdict)
# thisdict.update({"color":"red"})
# print(thisdict)
# thisdict.pop("model")
# print(thisdict)
# thisdict.popitem()
# print(thisdict)
# del thisdict["model"]
# print(thisdict)
# del thisdict
# print(thisdict)
# print(thisdict)
# thisdict.clear()
# print(thisdict)
# for x in thisdict:
#     print(x)
# for x in thisdict:
#     print(thisdict(x))
# for x in thisdict.values():
#     print(x)
# for x in thisdict.keys():
#     print(x)
# for x in thisdict.items():
#     print(x)
# mydict=thisdict.copy()
# print(mydict)
# mydict=dict(thisdict)
# print(mydict)
myfamily={
    "child1":{
        "name":"divya",
        "year":1991
    },
    "child2":{
        "name":"srija",
        "year":1995
    },
    "child3":{
        "name":"montu",
        "year":2019
    }
}
print(myfamily)
myfamily={
    "child1":"child1",
    "child2":"child2",
    "child3":"child3"
}
print(myfamily)
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(car.get("model"))