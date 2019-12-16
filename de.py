from decorators import do_twice, timer, debug
import math


@do_twice
def say_whee():
    print("Whee!!!")


@do_twice
def greet(name, number):
    print(f"Hello {name}, {number}")

@do_twice
def return_greeting(name):
    print("Greetin greeting")
    return f"Hi {name}"

@timer
def waste_come_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

approximate_e(5)