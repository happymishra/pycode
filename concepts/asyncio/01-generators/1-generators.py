# https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc

def gen():
    print("Hello")
    yield
    print("GoodBye")


if __name__ == '__main__':
    gen_co = gen()  # Initialize the generator (1)

    next(gen_co)  # Advance the generator (2)

    next(gen_co)  # Advance again (3)
