#Break and Continue :)
"""
floor_number = int(input("Eneter Floor Number:"))

for floor in range(1, 11):
    print("Elevator Arrived on floor#",floor)

    if floor == floor_number:
        break
"""
#wnated to skip some statements

# the use of ocnitnue statements

for idx in range(1, 11):
    # if idx >= 5:
    #     print("idx is:", idx)

    if idx <= 5:
        continue
    print(f"Idx is :{idx})


