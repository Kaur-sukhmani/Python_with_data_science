# Strings are immutable
# strings are never modified you will get a new string in the memory

names = "John, Jennie, Jim, Jack, Joe"
print("names:", names)  # names: John, Jennie, Jim, Jack, Joe

upper_case_names = names.upper()
lower_case_names = names.lower()

print("names now:", names, id(names))  # names now: John, Jennie, Jim, Jack, Joe 4304803824
print("Upper case names:", upper_case_names,
      id(upper_case_names))  # Upper case names: JOHN, JENNIE, JIM, JACK, JOE 4304806064
print("upper case names check:", lower_case_names, id(lower_case_names))
# upper case names check: john, jennie, jim, jack, joe 4365443408

s1 = names.capitalize()
quote = "be exceptional have a good day."
s2 = quote.title()
s4 = names.swapcase()
s5 = names.replace('J', 'KO')

print("s1", s1)  # s1 John, jennie, jim, jack, joe
print("s2", s2)  # s2 Be Exceptional Have A Good Day.
print("s4", s4)  # s4 jOHN,jENNIE,jIM,jACK, jOE
print("s5", s5)  # s5 KOohn,KOennie,KOim,KOack,KOoe

password = input("enter your password :")
print("Password:", password)
#
password = input("enter your password :")
print("Password:", password.strip())
# .strip remove the left and the right space
# same rstrip remove spaces from right
# ans lstrip remove from left

data = '0000000030205000'
print("data:", data)
# .strip remove the left and the right strings/ chaarachters

data = '0000000030205000'
print("data:", data.strip('0'))

number = 3.5600000
numbers = float(str(number).strip('0'))
print("number", numbers)

number = 5.6666
numbers = float(str(number).strip('6'))
print("number", numbers)

message = "No internet Connectivity"
print(message)
print(message.center(120))
print(message.ljust(120))
print(message.rjust(120))
"""No internet Connectivity
                                                No internet Connectivity                                                
No internet Connectivity                                                                                                
                                                                                                No internet Connectivity
                                                                                                """
data = "544"
print(data.zfill(50))
# 00000000000000000000000000000000000000000000000544

quote = "Search the candle rather than cursing the darkness"
print(quote.find("the"))  # 7
print(quote.find('sing'))  # 33
print(quote.index('the'))  # 7
print(quote.rindex('the'))  # right side se the kahan pe aa rha hain ->38
print(quote.index('sing'))
print(quote.rindex('sing'))

idx1 = quote.index('candle')
idx2 = idx1 + len('candle') - 1
print("idx1:", idx1)
print("idx2:", idx2)
print(quote[idx1:idx2])

for ch in quote:
    print(ch, end="")
