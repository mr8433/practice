import os
show=os.listdir("data")
print(show)

for i in show:
    print(i)
    print(os.listdir(f"data/{i}"))
    