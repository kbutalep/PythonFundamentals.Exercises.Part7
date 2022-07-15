from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: 'English', 2: 'Spanish', 3: 'French'}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: 'What is your name?', 2: 'Como te llamas?', 3: 'Comment vous-appelez vous?'}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1: 'Hello', 2: 'Hola', 3: 'Bonjour'}


def select_user_mode():
    print("Please select a user mode:\n"
          "1: Admin\n"
          "2: User\n")
    user_input = int(input())
    if user_input == 1:
        enter_admin()
    elif user_input == 2:
        print("User mode selected")
    else:
        print("That's not an option. Please try again. Select 1 for admin and 2 for user.\n")


def enter_admin():
    # Add support for additional languages.
    #  Update greetings for existing languages.
    print("Select from the following options:\n"
          "1. Add new language\n"
          "2: Update language\n")
    user_input = int(input())
    if user_input == 1:
        admin_add_language()
    elif user_input == 2:
        admin_update_language()
    else:
        print("That's not an option. Switching to user mode.\n")

def admin_add_language():
    print("Please enter the language you are adding.\n")
    new_lang = input()
    new_key = len(lang_dict) + 1
    lang_dict[new_key] = new_lang
    print(f'Please enter "What is your name?" in {new_lang}.')
    new_name_prompt = input()
    name_prompt_dict[new_key] = new_name_prompt
    print(f'Please enter "Hello" in {new_lang}.')
    new_greeting = input()
    greetings_dict[new_key] = new_greeting
    print(f'Thank you. {new_lang} has been entered. Now entering user mode\n')

def admin_update_language():
    print("Which language are you updating?")
    print(lang_dict)
    lang_selection = int(input())
    print("Please enter a new greeting.\n")
    new_greeting = input()
    greetings_dict[lang_selection] = new_greeting
    print("The greeting has been updated.")

def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print("Please choose a language: ")
    for key, language in lang_options.items():
       print(f'{key}:', language)

   # pass  # remove pass statement and implement me


def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """

    return int(input())
    # remove pass statement and implement me


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    if lang_choice in lang_options:
        return True
    else:
        return False

    #pass  # remove pass statement and implement me


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    if lang_choice == 1:
        print(name_prompt_options[1])
    elif lang_choice == 2:
        print(name_prompt_options[2])
    else:
        print(name_prompt_options[3])


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    name_prompt = str(input())
    return name_prompt
    #pass  # remove pass statement and implement me


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    greeting = str(greetings_options[lang_choice])
    print(greeting + " " + name)



    #pass  # remove pass statement and implement me


if __name__ == '__main__':
    select_user_mode()
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)
