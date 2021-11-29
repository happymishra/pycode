# https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc
def inner():
    print("We are inside inner")

    value = yield 2

    print(f"Received value is: {value}")

    return 4


def outer():
    print("We are inside outer")
    yield 1

    print("Calling inner function")
    inner_val = yield from inner()

    print(f"inner return value -> {inner_val}")

    yield 5


if __name__ == '__main__':
    gen_outer = outer()  # Initialize the generator (1)

    x = next(gen_outer)  # Advance the generator (2)
    print(f"Yielded value is {x}")

    x = next(gen_outer)  # Advance the generator (2)
    print(f"Yielded value is {x}")

    # send value to inner function
    y = gen_outer.send(3)
    print(f"Yielded value is {y}")

# As you can see, using yield from creates a way to communicate between the innermost generator, all the way out.
