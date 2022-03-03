auto_mobile={}
print(" Empty dictionary ",auto_mobile)
auto_mobile=dict({1:"Engine",2:"Clutch",3:"Gearbox"})
print(" Automobile parts :",auto_mobile)
print(" The value for 2 is ",auto_mobile.get(2))
auto_mobile['four']="chassis"
print(" Updated auto_mobile",auto_mobile)
print(auto_mobile.popitem())
print(" The current auto_mobile parts is :",auto_mobile)
print(" Is 2 available in automobile parts")
print(2 in auto_mobile)
