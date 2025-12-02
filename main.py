from day1 import day_1
from day2 import day_2

def main():
    day = int(input("What day will you run? "))
    part = int(input("What part will you run? "))
    match day:
        case 1:
            day_1(part)
        case 2:
            day_2(part)

if __name__ == "__main__":
    main()
