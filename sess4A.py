"""
   Another brick in the wall :)


   john: 1 2 3 ..
   jack: 2 4 6..

   total brick: 13
"""

# total_brick = int(input("Enter number of bricks you want:"))
# bricks_in_wall=0 # total brick

# for idx in range(1,total_brick):
#     john_bricks = idx
#     jack_bricks = 2 * idx
#
#     brick_in_wall += john_bricks + jack_bricks
# print(f"bricks_in_wall: {brick_in_wall}")

# Enter number of bricks you want:13
# brick_in_wall: 234
# but we want the number of bricks to be 13
# so13

"""
for idx in range(1,total_brick):
    john_bricks = idx
    jack_bricks = 2 * idx

    brick_in_wall += john_bricks + jack_bricks

    if brick_in_wall >= total_brick:
        break
print(f"bricks_in_wall: {brick_in_wall}")
"""


# problem statement the bricks in the wall should be 13
#  print who put the brick at the last and how many
"""
    Another Brick in the Wall :)

    john: 1 2 3...
    jack: 2 4 6...

    total: 12 + 1 -> 13
           jack: 1

    total bricks: 13

"""


#     MY SOLUTION
"""
for idx in range(1, total_brick):
    john_bricks = idx
    if (bricks_in_wall < total_brick) and (total_brick - bricks_in_wall < idx):
        sol = total_brick - bricks_in_wall
        bricks_in_wall += sol
        print(f"John Placed the Last Brick:{sol}")
        print(f"brick in the wall :{bricks_in_wall}")
        break
    else:
        bricks_in_wall += john_bricks

    jack_bricks = 2 * idx
    if (bricks_in_wall < total_brick) and (total_brick - bricks_in_wall < (2 * idx)):
        sol = total_brick - bricks_in_wall
        bricks_in_wall += sol
        print(f"Jack Placed the Last Brick:{sol}")
        print(f"brick in the wall :{bricks_in_wall}")
        break
    else:
        bricks_in_wall += jack_bricks
"""


# ALTERNATE SIR'S SOLUTION
"""
total_bricks = int(input("Enter Number of Bricks: "))
bricks_in_wall = 0

for idx in range(1, total_bricks):
    john_bricks = idx
    bricks_in_wall += john_bricks

    if bricks_in_wall >= total_bricks:
        difference = bricks_in_wall - total_bricks
        print("John Placed the Last Brick:", (john_bricks - difference))
        break

    jack_bricks = idx * 2
    bricks_in_wall += jack_bricks

    if bricks_in_wall >= total_bricks:
        difference = bricks_in_wall - total_bricks
        print("Jack Placed the Last Brick:", (jack_bricks-difference))
        break


print("bricks_in_wall is:", (bricks_in_wall-difference))

"""

# the same problem using
#while loop
"""
total_bricks = int(input("Enter Number of Bricks: "))
bricks_in_wall = 0
idx =1
while idx < total_bricks:
    john_bricks = idx
    bricks_in_wall += john_bricks

    if bricks_in_wall >= total_bricks:
        difference = bricks_in_wall - total_bricks
        print("John Placed the Last Brick:", (john_bricks - difference))
        break

    jack_bricks = idx * 2
    bricks_in_wall += jack_bricks

    if bricks_in_wall >= total_bricks:
        difference = bricks_in_wall - total_bricks
        print("Jack Placed the Last Brick:", (jack_bricks - difference))
        break
    idx += 1

print("bricks_in_wall is:", (bricks_in_wall - difference))

"""