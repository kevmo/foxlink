import random
import string


def generateRandomString(N):
    """Returns random string of letters and numbers of N length."""
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))