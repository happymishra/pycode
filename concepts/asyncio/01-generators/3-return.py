# https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc

def gen():
    yield "Hello"

    print("Good Bye")

    # By return the function will raise an exception
    return 2


if __name__ == '__main__':
    gen_co = gen()  # Initialize the generator (1)

    a = next(gen_co)  # Advance the generator (2)
    print(a)

    print("Calling next again")
    try:
        b = next(gen_co)
    except StopIteration as ex:
        print(f"Print from inside exception: {ex.value}")
