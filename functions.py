import colorama, os
from colorama import Fore, Back, Style, init
from subject import Subject
colorama.init()

# options page function

def options_page(option_list):
    # setup
    os.system('cls') # clear screen
    print(f"{Fore.BLACK}{Back.WHITE}\n----Option Overview----\n{Fore.CYAN}{Back.RESET}")
    # printing option list
    for i in option_list:
         print(i)
    print(Fore.RESET + "\n" + 20*"---")
    # getting input
    while True:
        return_value = input(f"{Fore.GREEN}\nPlease enter a number from the list above: {Fore.RESET}")
        if not return_value.isdigit():
            print(f"{Back.RED}\nInvalid entry, try again.{Back.RESET}")
            continue
        if int(return_value) > 0 and int(return_value) <= len(option_list):
                break
        else:
             print(f"{Back.RED}\nInvalid entry, try again.{Back.RESET}")
    return int(return_value.strip())

# display subjects function

def display_subjects(subject_list):
    os.system('cls')
    print(f"{Back.WHITE}{Fore.GREEN}SUBJECTS:{Back.RESET}{Fore.RESET}\n")
    for subject_object in subject_list:
         print(f"{subject_object.name} ({subject_object.code})\n")
    print(20*"---")
    option_list = [
         f"{Fore.GREEN}\n1...Back",
         f"\n2...Update Subject Name",
         f"\n3...Update Subject Code\n{Fore.RESET}"
    ]
    # print options
    for i in option_list:
         print(i)
    print(20*"---")
    # getting input
    while True:
        input_value = input(f"\nPlease enter a number from the list above: {Fore.RESET}")
        if not input_value.isdigit():
            print(f"{Back.RED}\nInvalid entry, try again.{Back.RESET}")
            continue
        if int(input_value) > 0 and int(input_value) <= len(option_list):
                break
        else:
             print(f"{Back.RED}\nInvalid entry, try again.{Back.RESET}")
    input_value = int(input_value)
    # input selection
    if input_value == 1:
        return
    if input_value == 2:
        os.system('cls')
        # print subjects numbered
        print(f"{Back.WHITE}{Fore.GREEN}Select Subject:{Back.RESET}{Fore.RESET}\n")
        for subject_object in subject_list:
            print(f"{subject_list.index(subject_object) + 1}. {subject_object.name} ({subject_object.code})\n")
        # get input
        while True:
            subject_num = input(f"\nPlease enter a number from the list above: {Fore.RESET}")
            if not subject_num.isdigit():
                print(f"{Back.RED}\nInvalid entry, try again.{Back.RESET}")
                continue
            if int(subject_num) > 0 and int(subject_num) <= len(subject_list):
                    break
            else:
                print(f"{Back.RED}\nInvalid entry, try again.{Back.RESET}")
        subject_num = int(subject_num) - 1
        # clear screen and call subject.update_name()
        os.system('cls')
        Subject.update_name(subject_list[subject_num])
        # call this function again
        display_subjects(subject_list)
    if input_value == 3:
        os.system('cls')
        # print subjects numbered
        print(f"{Back.WHITE}{Fore.GREEN}Select Subject:{Back.RESET}{Fore.RESET}\n")
        for subject_object in subject_list:
            print(f"{subject_list.index(subject_object) + 1}. {subject_object.name} {Back.MAGENTA}({subject_object.code})\n{Back.RESET}")
        # get input
        while True:
            subject_num = input(f"\nPlease enter a number from the list above: {Fore.RESET}")
            if not subject_num.isdigit():
                print(f"{Back.RED}\nInvalid entry, try again.{Back.RESET}")
                continue
            if int(subject_num) > 0 and int(subject_num) <= len(subject_list):
                    break
            else:
                print(f"{Back.RED}\nInvalid entry, try again.{Back.RESET}")
        subject_num = int(subject_num) - 1
        # clear screen and call subject.update_name()
        os.system('cls')
        Subject.update_code(subject_list[subject_num])
        # call this function again
        display_subjects(subject_list)