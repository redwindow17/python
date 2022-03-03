civil_ele={}
print(civil_ele)
civil_ele=dict([(1,"Beam"),(2,"Plate")])
print(" the elements of civil structure are ",civil_ele)
print(" the value for key 1 is :",civil_ele[1])
civil_ele['three']='concrete'
print(civil_ele)
new=civil_ele.copy()
print(" The copy of civil_ele",new)
print(" The length is ",len(civil_ele))
for i in civil_ele:
 print(civil_ele[i])
