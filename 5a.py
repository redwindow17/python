Language={}
print(" Empty Dictionary :",Language)
Language=dict({1: "english", "two": "tamil", 3: "malayalam"})
print(" Using dict() the languages are :",Language)
New_Language={4: "hindi",5: "hindi"}#duplicate values can create
Language.update(New_Language)
print(" the updated languages are :",Language)
print(" the length of the languages :",len(Language))
Language.pop(5)
print(" key 5 has been popped with value :",Language)
print(" the keys are :",Language.keys())
print(" the values are :",Language.values())
print(" the items in languages are :",Language.items())
Language.clear()
print(" The items are cleared in dictionary ",Language)
del Language
print(Language)
