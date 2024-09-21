dict={'name':"Mayank Rajput",'age':18,'id':202423}
# print(dict.get('name'))
# print(dict['age'])
# print(dict.items())
print(dict.values())
# for key in dict:
#     print(f"the value corresponding to the {key} is {dict[key]}")
for key,value in dict.items():
     print(f"the value corresponding to the {key} is {value}")

emp1={2276247:90,2276380:80,2275012:70}
emp2={50076142:67,500076143:78}
emp1.update(emp2)
# emp1.pop(2276247)
# emp1.clear()
# del emp1[2276247]
print(emp1)
