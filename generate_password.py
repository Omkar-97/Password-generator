import random


def get_numbers():
    numbers = ""
    for num in range(0, 10):
        numbers += "".join(str(num))
    return numbers


def get_small_ch():
    small_alphabets = ""
    for ch in range(ord("a"), ord("z") + 1):
        small_alphabets += "".join(chr(ch))
    return small_alphabets


def get_capital_ch():
    capital_alphabets = ""
    for ch in range(ord("A"), ord("Z") + 1):
        capital_alphabets += "".join(chr(ch))
    return capital_alphabets


def get_special_char():
    return "+-~/#@$%&"


def password_gen(special_char, small_alphabets, capital_alphabets, numbers, pass_len):
    final_string = small_alphabets + capital_alphabets + special_char + numbers
    random_char = [random.choice(final_string) for i in range(pass_len)]
    pwd = "".join(random_char)
    return pwd


def generate_password(pwd_len):
    special_char = get_special_char()
    small_alphabets = get_small_ch()
    capital_alphabets = get_capital_ch()
    numbers = get_numbers()

    final_password = password_gen(special_char, small_alphabets, capital_alphabets, numbers, pwd_len)
    return final_password


if __name__ == '__main__':
    print("Password length: ", end=" ")
    password_length = int(input())
    password = generate_password(password_length)
    print("Generated password: {0}".format(password))
