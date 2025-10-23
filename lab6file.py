import os
import string


path = "."
print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print("All:", os.listdir(path))

path = "1 assignment.py"

print("Exists:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

path = "1 assignment.py"

if os.path.exists(path):
    print("Path exists!")
    print("Directory:", os.path.dirname(path))
    print("Filename:", os.path.basename(path))
else:
    print("Path does not exist.")

def count_lines(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())

print(count_lines("sample-data.json"))

data = ["apple", "banana", "cherry"]

with open("./6_assignment_folder/fruits.txt", "w") as f:
    for item in data:
        f.write(f"{item}\n")

for letter in string.ascii_uppercase:
    open(f"./6_assignment_folder/{letter}.txt", "w").close()

def copy_file(src, dest):
    with open(src, 'r') as f1, open(dest, 'w') as f2:
        f2.write(f1.read())

copy_file("./6_assignment_folder/fruits.txt", "./6_assignment_folder/fruits2.txt")

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"{path} deleted successfully.")
        else:
            print("No write permission to delete file.")
    else:
        print("File does not exist.")

delete_file("./6_assignment_folder/fruits.txt")