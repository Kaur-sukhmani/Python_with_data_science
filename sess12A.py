names = "John, Jennie, Jim, Jack, Joe"
print("Indexing:", names[0])  # J
print("Negative indexing:", names[-1])  # e

print("slicing:", names[:5])  # John,
print("slicing:", names[2:10])  # hn, Jenn

print("Multiplicity:", names * 2)  # Multiplicity: John, Jennie, Jim, Jack, JoeJohn, Jennie, Jim, Jack, Joe

# since they are immuatable so a new names is developed if
# names = names + ", khushi"
names2 = "Love, Khushi"
names3 = names2 + names
print("Concatenation :", names3)  # Concatenation : Love, KhushiJohn, Jennie, Jim, Jack, Joe

# membership testing
print("John" in names)  # True
