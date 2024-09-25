import os

folder =os.getcwd()
print(folder)
# os.mkdir("new")
# print(os.getcwd())
if not os.path.exists("data"):
    os.mkdir("data")
for i in range (0,3):
    # os.mkdir(f"data/temp{i+1}")
    os.rename(f"data/temp{i+1}",f"data/tutorial{i+1}")
    

