def reversed_string(text):
 if len(text) == 1:
    return text
 return reversed_string(text[1:])+text[:1]
a=reversed_string(input("Enter your string:"))
print(a)
