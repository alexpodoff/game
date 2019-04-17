import sys


class Menu:

    def __init__(self):
        self.gender = None
        self.race = None
        self.name = "unknown"

    def start(self):
        choice = input('main menu\n'
                       '1. start\n'
                       '2. quit\n')
        if choice == "1":
            print("Ok, lets play")
            self.pick_race()
        elif choice == "2":
            sys.exit("Bye!")
        else:
            print("Enter 1 or 2")
            self.start()

    def pick_race(self):
        choice = input('pick your race\n'
                       '1. human\n'
                       '2. elf\n'
                       '3. return to main menu\n')
        if choice == "1":
            print("Human it is")
            self.race = "human"
            self.pick_gender()
        elif choice == "2":
            print("So, elf...")
            self.race = "elf"
            self.pick_gender()
        elif choice == "3":
            self.start()
        else:
            print("Enter 1, 2 or 3")
            self.pick_race()

    def pick_gender(self):
        choice = input('pick your gender\n'
                       '1. male\n'
                       '2. femail\n'
                       '3. return to race pick\n'
                       '4. return to main menu\n')
        if choice == "1":
            print(f"You pick {self.race} male")
            self.gender = "male"
            self.name_selection()
        elif choice == "2":
            print(f"You pick {self.race} female")
            self.gender = "female"
            self.name_selection()
        elif choice == "3":
            self.pick_race()
        elif choice == "4":
            self.start()
        else:
            print("Enter 1, 2 or 3")
            self.pick_gender()

    def name_selection(self):
        choice = input(f'Enter your name, brave {self.race} {self.gender}\n'
                       'You can enter "cancel" to return to a previous menu\n')
        if choice == "cancel":
            self.pick_gender()
        else:
            confirm = input(f'Your name is {choice}, is this correct?\n'
                            '1. Yes, go on!\n'
                            '2. No, let me try again\n'
                            '3. Screw this, I\'m out')
            if confirm == '1':
                self.name = choice
                pass
            elif confirm == '2':
                self.name_selection()
            elif confirm == '3':
                print("I am a little sorry :(\n")
                sys.exit(66)
            else:
                print("Enter 1, 2 or 3")
                self.name_selection()
