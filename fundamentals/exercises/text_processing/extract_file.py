path = input().split("\\")
file_name, extension = path[len(path) - 1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {extension}")
