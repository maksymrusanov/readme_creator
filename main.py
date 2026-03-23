with open("./.git/config") as file:
    res = file.readlines()
print(res[8].split("=")[1])
