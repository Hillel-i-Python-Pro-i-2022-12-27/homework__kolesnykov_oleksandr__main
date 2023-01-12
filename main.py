from random import randint
from application import get_fake_name


def get_random_age() -> int:
    """
    This function returns a random int() from 5 to 55
    """
    return randint(5, 55)


def say_hello() -> str:
    """
    This function returns a greeting string with the fake person's name and random age
    """
    return f"Hello, my name is {get_fake_name()} ! I am {get_random_age()} years old."


if __name__ == "__main__":
    print(say_hello())
