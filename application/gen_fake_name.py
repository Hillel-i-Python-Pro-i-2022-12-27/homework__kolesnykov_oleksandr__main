from faker import Faker


def get_fake_name() -> str:
    """
    This function returns a random str(name) from "Faker==16.3.0" module
    """

    return Faker().first_name()
