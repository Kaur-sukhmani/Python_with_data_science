def fetch():
    file = open("ipl-data-2022.csv", "r")
    lines = file.readlines()

    for line in lines:
        yield line
        # return line

# if a funciton, yields, it means we get Generator in return
result = fetch()
print("result:", result)


# How to use with loop -> explore
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(result, "No more record ")

"""next is builtin function used in generators"""
while True:
    data = next(result, "Nothing")
    print(data)
    if data == "Nothing":
        break
