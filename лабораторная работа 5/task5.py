import string
import random
def get_random_password(k: int = 8) -> str:
    a = string.digits + string.ascii_letters
    return "".join(random.sample(a, k))
print(get_random_password())
