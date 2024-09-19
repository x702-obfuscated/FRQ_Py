import os
import re

def clear_screen():
    # For Unix/Linux
    if os.name == 'posix':
        os.system('clear')
    # For Windows
    elif os.name == 'nt':
        os.system('cls')


def get_name():
    name = check_input(
      r"[A-Z]+\s[A-Z]+",
      "Please type your FIRST and LAST name below.\n",
      "Make sure you enter your FIRST and LAST name with a single space in between."
    )
    while(len(name) > 20):
      print("The name you entered is to long, please limit your name to 20 characters or less.")
      name = check_input(
      r"[A-Z]+\s[A-Z]+",
      "Please type your FIRST and LAST name below.\n",
      "Make sure you enter your FIRST and LAST name with a single space in between."
    )
    return name


def check_input(pattern, prompt,reject_prompt):
  no_match = True
  inp = ""
  while(no_match):
    inp = input(prompt).upper().lstrip(" ")
    no_match = not re.search(pattern, inp)
    if(no_match):
      clear_screen()
      input(f"{reject_prompt}\nPress enter to continue.\n")
      clear_screen()
  return inp 