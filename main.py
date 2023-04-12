from subject import Subject
from functions import options_page, display_subjects
import colorama, pickle, os, time, sys, datetime
from colorama import Fore, Back, Style, init
colorama.init()


# loading save

subject_list = [
    
    ]
try:
    with open("subject_memory.txt", "rb") as file:
        for i in pickle.load(file):
            subject_list.append(i)
except(Exception):
    print(f"{Back.RED}The {Fore.GREEN}\"subject_memory.txt\"{Fore.RESET} file is missing or corrupted.{Back.RESET}\nClosing in 10 seconds...")
    time.sleep(1)
    for i in range(9):
        print(f"{9 - i}...")
        time.sleep(1)
    sys.exit()



# settings
option_list = [
        f"\n1.....Task Overview",
        f"\n2.....View/Edit Subjects",
        f"\n3.....Add Subject",
        f"\n4.....Delete Subject",
        f"\n5.....Add Task",
        f"\n6.....Delete Task",
        f"\n7.....Print Overview",
        f"\n8.....Save and Exit"
    ]

# main

while True:
    #  options page and selection
    selection = options_page(option_list)
    
    # TO-DO LATER: make options selection dynamic by using for-loop and
    # removing numbering in option_list (above)

    # option 1: overview
    if selection == 1:
        os.system('cls')
        if len(subject_list) == 0:
            print(f"\n{Fore.GREEN}No subjects have been added.\nAdd a subject on the previous options panel!{Fore.RESET}")
            time.sleep(3)
            continue
        print(f"{Back.WHITE}{Fore.BLUE}TASK OVERVIEW:{Back.RESET}{Fore.BLUE}\n")
        for subject in subject_list:
            print(f"\n{Back.GREEN}{Fore.WHITE}{subject.name} - {subject.code}{Fore.RESET}{Back.RESET}")
            if len(subject.tasks) > 0:
                i = 1
                for task in subject.tasks:
                    print(f"{Fore.YELLOW}\n    {i}. {task}{Fore.RESET}")
                    i += 1
            else:
                print(f"{Fore.GREEN}\n  No tasks.{Fore.RESET}")
        
        exit = input(f"\n\n{Fore.RED}Press Enter to return. {Fore.RESET}")

    #  option 2: subjects only displayed
    if selection == 2:
        display_subjects(subject_list)

    # option 3: add a new subject
    if selection == 3:
        os.system("cls")
        subject_list.append(Subject("None", "None"))
        subject_list[-1].update_name()
        subject_list[-1].update_code()

    # option 4: delete a subject
    if selection == 4:
        os.system("cls")
        # continue through loop if no subjects
        if len(subject_list) == 0:
            print("No subjects to delete. Add a subject!")
            time.sleep(2)
            continue
        
        print(f"{Back.WHITE}{Fore.BLUE}SUBJECT DELETION:{Back.RESET}{Fore.GREEN}\n")
        i = 1
        for subject in subject_list:
            print(f"\n{i}. {subject.name}")
            i += 1
        print(f"\n{Fore.RED}Press Enter to go back.\n{Fore.RESET}")
        print(20*"---")
        print("\n")
        while True:
            try:
                delete = input(f"Select a subject to delete: ")
                if len(delete) == 0:
                    break
                else:
                    subject_list.pop(int(delete) - 1)
                    print("\nDeleting...")
                    time.sleep(0.2)
                    print(f"\n{Fore.GREEN}Done!{Fore.RESET}")
                    time.sleep(0.2)
                    break
            except Exception:
                print(f"\n{Fore.RED}Please try again. Select a number from 1 to {len(subject_list)}{Fore.RESET}\n")
                time.sleep(0.25)

    # option 5: add task
    if selection == 5:
        os.system("cls")
        # continue through loop if no subjects
        if len(subject_list) == 0:
            print("No subjects to add a task to. Add a subject!")
            time.sleep(2)
            continue

        print(f"{Back.WHITE}{Fore.BLUE}ADD TASK:{Back.RESET}{Fore.GREEN}\n")
        i = 1
        for subject in subject_list:
            print(f"\n{i}. {subject.name}")
            i += 1
        print(f"\n{Fore.RED}Press Enter to go back.\n{Fore.RESET}")
        print(20*"---")
        print("\n")
        while True:
                try:
                    add = input(f"Select a subject to add a task to: ")
                    if len(add) == 0:
                        break
                    else:
                        subject_list[int(add) - 1].add_task()
                        time.sleep(1)
                        break
                except Exception:
                    print(f"\n{Fore.RED}Please try again. Select a number from 1 to {len(subject_list)}{Fore.RESET}\n")
                    time.sleep(0.25)

    # option 6: delete task
    if selection == 6:
        os.system("cls")
        # continue through loop if no subjects
        if len(subject_list) == 0:
            print("No subjects to delete a task from. Add a subject!")
            time.sleep(2)
            continue

        print(f"{Back.WHITE}{Fore.BLUE}DELETE TASK:{Back.RESET}{Fore.GREEN}\n")
        i = 1
        for subject in subject_list:
            print(f"\n{i}. {subject.name}")
            i += 1
        print(f"\n{Fore.RED}Press Enter to go back.\n{Fore.RESET}")
        print(20*"---")
        print("\n")
        while True:
                try:
                    add = input(f"Select a subject to delete a task from: ")
                    if len(add) == 0:
                        break
                    else:
                        subject_list[int(add) - 1].delete_task()
                        time.sleep(1)
                        break
                except Exception:
                    print(f"\n{Fore.RED}Please try again. Select a number from 1 to {len(subject_list)}{Fore.RESET}\n")
                    time.sleep(0.25)

    # option 7: print with standard printer
    if selection == 7:
        if len(subject_list) == 0:
            print("Nothing to print. Add a subject.")
            time.sleep(1.5)
        else:
            filename = f"print_{datetime.date.today()}.txt"
            with open(filename, "w") as file:
                for subject in subject_list:
                    file.write("\n")
                    file.write(f"{subject.name} - {subject.code}\n")
                    file.write("\n")
                    if len(subject.tasks) > 0:
                        i = 1
                        for task in subject.tasks:
                            file.write(f"     {i}. {task}\n")
                            i += 1
                    else:
                        file.write(f"     No tasks.\n")
        
        # print to standard printer
        os.startfile(filename, "print")

    if selection == 8:
        break





# saving and exit

with open("subject_memory.txt", "wb") as file:
    print(f"{Fore.GREEN}{Back.BLUE}\nSave-file present.")
    time.sleep(0.25)
    pickle.dump(subject_list, file)

# save bar animation
print(f"\nSaving:{Back.WHITE}{Fore.WHITE}", end="")
for i in range(70):
     print(f"❚", end="")
     time.sleep(0.01)
print(f"{Back.BLUE}{Fore.GREEN}Save Successful.{Back.RESET}{Fore.RESET}")
time.sleep(0.5)
