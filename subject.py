import colorama, os
from colorama import Fore, Back, Style, init
colorama.init()

# Subject class

class Subject():
    def __init__(self, subject_name, subject_code):
        self.name = subject_name
        self.code = subject_code
        self.tasks = []

    def update_name(self):
        print(f"\n{Style.DIM}Current name: {self.name}{Style.NORMAL}")
        while True:
            self.name = input(Fore.GREEN + f"\nEnter a new subject name: " + Fore.WHITE).strip()
            if len(self.name) <= 50:
                break
            else:
                print(Back.RED + "\nLength of title cannot exceed 50 characters." + Back.RESET)

    def update_code(self):
        print(f"\n{Style.DIM}Current code: {self.code}{Style.NORMAL}")
        while True:
            self.code = input(Fore.GREEN + f"\nEnter a new subject code: " + Fore.WHITE).strip()
            if len(self.code) <= 10:
                break
            else:
                print(Back.RED + "\nLength of title cannot exceed 10 characters." + Back.RESET)

    def add_task(self):
        inp = input("\n\nEnter the task name: ")
        self.tasks.append(inp)
        print(f"{Fore.GREEN}\nDone!{Fore.RESET}")
    
    def delete_task(self):
        os.system("cls")
        if len(self.tasks) > 0:
            print(f"{Back.WHITE}{Fore.BLUE}TASKS:{Fore.YELLOW}\n")
            print(f"\n{self.name}{Back.RESET}{Fore.RESET}")
            i = 1
            for task in self.tasks:
                print(f"\n  {i}. {task}")
                i += 1
            print(f"\n{Fore.RED}    Press Enter to go back.\n{Fore.RESET}")
            while True:
                index = input(f"\nChoose a task to delete: ")
                if len(index) == 0:
                    print("\nGoing back...")
                    break
                try:
                    if (int(index) > 0) and (int(index) < len(self.tasks) + 1):
                        self.tasks.pop(int(index) - 1)
                        print(f"{Fore.GREEN}Done!{Fore.RESET}")
                        break
                    else:
                        print(f"{Fore.RED}\nPlease pick from the available tasks.{Fore.RESET}")
                except Exception:
                    print(f"{Fore.RED}\nInvalid input. Please try again.{Fore.RESET}")
        else:
            print("This subject has no tasks.")

