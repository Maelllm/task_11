def example1():
    try:
        for i in range(3):
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
    except ValueError:
        print('You must enter valid numbers')
        example1()


def example2(*args):
    print("\n\nExample 2")
    # sum = 0
    sumOfPairs = []
    b = range(len(*args) // 2)
    try:
        for i in b:
            for k in args:
                sumOfPairs.append(k[i] + k[::-1][i])
    except:
        print('Nobody expect non int arguments here.')

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    file = open(fileName, "r")
    try:
        for line in file:
            print(line.upper())
    except:
        pass
    finally:
        file.close()


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    example2([10, 3, 5, 6])
    try:
        printUpperFile("doesNotExistYest.txt")
        printUpperFile("./Dessssktop/misspelled.txt")
    except:
        print('No such files found')


main()
