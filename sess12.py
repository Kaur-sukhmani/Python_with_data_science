# String in python
# cafe_name = "John's Cafe"
# we can keep our string in single qoute but bec of apposttofy s ki wajah se double
cafe_name = 'John\'s Cafe'
print("Cafe_name :", cafe_name, type(cafe_name), hex(id(cafe_name)))

print("Length", len(cafe_name))
print("Max:", max(cafe_name))
print("Min", min(cafe_name))
# print("sum", sum(cafe_name))->error


# Multi Line quotes
johns_cafe_name = """Johns Cafe Delight
- An authentic Italian restuarant"""

# \n ->new line
# """Johns Cafe Delight
# - An authentic Italian restuarant
# """
# now their will be next line
print(johns_cafe_name)
quote = 'Be Exceptional'
print(quote)

# Strine ke aage small r / Capital R means RAW so \n or any escape characters becomes the string
quote = r'Be \nExceptional'
print(quote)

quote = R'Be \nExceptional'
print(quote)

# list of escape characters
"""
\\: Backslash
\': Single Quote
\": Double Quote
\n: Newline (line feed)
\r: Carriage Return
\t: Tab
\b: Backspace
\f: Formfeed
\v: Vertical Tab
\a: ASCII Bell (bell sound)
\ooo: Octal value (where ooo is a sequence of three octal digits)
\xhh: Hexadecimal value (where hh is a sequence of two hexadecimal digits)
"""
