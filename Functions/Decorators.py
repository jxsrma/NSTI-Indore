def greetings(functions):
    """This Decorator will greet the user"""
    def hello(*args, **kwargs):
        print("Hello User")
        result = functions(*args, **kwargs)
        print(result)
        print("Bye User")
        return result
    return hello


@greetings
def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(1, 2, 3, 4, 5, 6))
