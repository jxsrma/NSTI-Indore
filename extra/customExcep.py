class MyCE(Exception):
    """Custom Exception Here"""
    pass


def div(n1, n2):
    if n2 == 0:
        raise MyCE("Not Allowed")
    return n1/n2


try:
    result = div(10, 0)
except MyCE as e:
    print(f"Error: {e}")
