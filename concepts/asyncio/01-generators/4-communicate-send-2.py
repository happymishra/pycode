# https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc

def gen():
    print("First number")
    a = yield 10

    # `a` is assigned the value that is sent from `send` method
    print(f"Second number. Value of a inside gen in -> {a}")
    b = yield 20

    print("Addition result:", a + b)
    c = yield a + b


if __name__ == '__main__':
    gen_co = gen()  # Initialize the generator (1)

    x = next(gen_co)  # Advance the generator (2)
    print(f"Yielded value is {x}")

    # This is like calling next and passing "ABC" as a parameters, even though gen does not expect any
    # parameter. It's a that is assigned the value

    # Internally, .send() works by putting the value at the top of the generator’s stack. It then evaluates
    # the frame, and pops the top value of the stack, putting it in our local variable.
    y = gen_co.send(1000)

    print(f"Yielded value is {y}")

    # Assign value to b  inside gen
    y = gen_co.send(2000)

    # Will return the yielded value a + b, raises and exception
    z = gen_co.send(5000)
    # z = next(gen_co) # raises and exception

    print(f"Yielded value is {z}")
