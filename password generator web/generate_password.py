import random

letters = "abcdefghijklmnopqrstuvwxyz"
letters_big = letters.upper()
numbers = "123456789"
signs = "!@#$%&(){}_+-*/^=.,|[]`;:<~>"


choose_generator1 = {
    1:"letter",
    2:"big letter",
    3:"number",
    4:"sign"
    }

def generate_password(with_letters, with_big_letters, with_numbers, with_signs, long):
    global choose_generator
    choose_generator = choose_generator1.copy()
    def clear_choosing_generator():
        # removes what dont need to be
        if with_letters == False:
            del choose_generator[1]
        if with_big_letters == False:
            del choose_generator[2]
        if with_numbers == False:
            del choose_generator[3]
        if with_signs == False: 
            del choose_generator[4]
    clear_choosing_generator()

    def fix_choose_generator():
        global choose_generator
        # fix the order of whats inside(1-n)
        # creates new dict with the fixed order and change the choose_generatoe dict to it
        index = 1
        new_dict = {}
        for num in choose_generator:
            new_dict[index] = choose_generator[num]
            index += 1
        choose_generator = new_dict
    fix_choose_generator()

    if choose_generator != {}:
        password = ""
        for _ in range(long):
            to_append = random.randint(1,len(choose_generator)) # 1-4 include 1,4
            append_type = choose_generator[to_append]
            appending = None
            if append_type == "letter":
                appending = letters[random.randint(0, len(letters)-1)]
            elif append_type == "big letter":
                appending = letters_big[random.randint(0, len(letters_big)-1)]
            elif append_type == "number":
                appending = numbers[random.randint(0, len(numbers)-1)]
            else: # sign
                appending = signs[random.randint(0, len(signs)-1)]
            password += appending
        return password
    else:
        return "cant"