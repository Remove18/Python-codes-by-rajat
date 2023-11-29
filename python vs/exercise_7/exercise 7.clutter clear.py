import os
# print(dir(os))

# print(f"\n{os.getcwd()}\n")

l = os.listdir(f"New folder")
# # print(l)

# or

i = 1
for file in l:
    if file.endswith(".png"):
        os.rename(f"New folder/{file}",f"New folder/logo {i}.png")
        i = i + 1
        
# n = []
# for file in l:
#     if file.endswith(".png"):
#         n.append(file)
        
# # print(n)
# i = 1
# for file in n:
#     os.rename(f"New folder/{file}",f"New folder/logo {i}.png")
#     i = i + 1