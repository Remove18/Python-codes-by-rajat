import shutil
import os

# os.mkdir("rajats")
# with open("rajats\\main.py", "w"):
#     pass

# os.rename("rajats", "rajats 1")
# shutil.copytree("rajats", "rajats 2")

for i in range (1, 101):
    # shutil.copytree("rajats 1", f"rajats {i}")
    os.remove(f"rajats {i}\\main.py")
    os.rmdir(f"rajats {i}")