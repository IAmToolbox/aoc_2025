import sys
from day1 import day_1

def main():
    day = int(input("What day will you run?"))
    part = int(input("What part will you run?"))
    match day:
        case 1:
            day_1(part)


if __name__ == "__main__":
    main()
