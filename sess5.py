"""
    whatever , we write in py file , is executed by main thread
"""


def main():
    a = 10
    b = 2 * a
    print('b is:', b)

    print("NAME:", __name__)

if __name__ == "__main__":
    main()