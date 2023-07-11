# Functions in Memory

def square(num):
    print(f"[square] num is: {num}")
    num **= 2#num = num * num
    print("[square] num now is :", num)



def main():
    a = 10
    print("[main] a is:", a, id(a))
    square(a)
    print("[main] a now is:", a, id(a))


if __name__ == "__main__":
    main()