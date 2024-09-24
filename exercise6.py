a=10
b=20
print("a is the  greater one")  if a>b else print("b is greater") 

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
