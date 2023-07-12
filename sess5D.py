# Assignment:
# Fibonaccie Series :)
# 0 1 1 2 3 5 8 ....
def fib(n):
    series = []
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        series = [0, 1]
        for idx in range(2, n+1):
            series.append(series[idx - 1]+series[idx - 2])
        return series
def main():
    num = int(input("enter the numebr:"))
    print(f"Fibonaccie Series:{fib(num)}")

if __name__ == "__main__":
    main()