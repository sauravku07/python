myDict = {
    "Fast": "In a Quick Manner ",
    "Harry": "a Coder",
    "marks": "[2,4,6]"
}
print(myDict["Fast"])
print(myDict["Harry"])
print(myDict["marks"])

# print the keys of the dictionary
print((myDict.keys()))
# print the value of the dictionary
print(myDict.values())
# print the (key,value) for all value  of the dictionary
print(myDict.items())
# for get value
print(myDict.get("marks"))
# for copy dictionary
print(myDict.copy())
# setdefault
print(myDict.setdefault("Harry", 45))
# update
# pop
# popitem
# clear
