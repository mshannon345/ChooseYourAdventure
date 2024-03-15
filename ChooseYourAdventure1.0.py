#Programmer: Miles Shannon
#Date: 02/15/2024
#Program: Choose Your Adventure

import time


class Noodle:
    def __init__(self, name):
        self.name = name

    def compete(self):
        print(f"{self.name} is determined to compete in the cooking competition!")
        time.sleep(2)
        print(f"{self.name} practices tirelessly, honing his skills.")
        time.sleep(2)
        print(f"The day of the competition arrives, and {self.name} steps onto the grand stage!")
        time.sleep(2)

    def win(self):
        print(f"With determination and courage, {self.name} impresses the judges with his culinary skills!")
        time.sleep(2)
        print(f"The judges announce {self.name} as the winner!")
        time.sleep(2)
        print(f"{self.name} becomes a legend, inspiring noodles everywhere!")
        time.sleep(2)
        print(f"And so, {self.name} lives happily ever after, his name forever etched in culinary history.")


def main():
    noodle_name = input("What would you like to name your noodle? ")
    noodle = Noodle(noodle_name)

    print("\nOnce upon a time, in a bustling city...")
    time.sleep(2)

    noodle.compete()
    noodle.win()


if __name__ == "__main__":
    main()
