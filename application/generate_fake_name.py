from faker import Faker


def get_fake_name() -> str:
    """
    This function returns a random male or female name
    """

    return Faker().first_name()
