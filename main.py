from day1 import day_1
from day2 import day_2
from day3 import day_3
from day4 import day_4

def main():
    day = int(input("What day will you run? "))
    part = int(input("What part will you run? "))
    match day:
        case 1:
            day_1(part)
        case 2:
            day_2(part)
        case 3:
            day_3(part)
        case 4:
            day_4(part)
        case _:
            print("Invalid input")
            exit(1)

if __name__ == "__main__":
    main()
