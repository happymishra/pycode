# https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc

def gen(num):
    num += 1

    yield num

    num += 1

    yield num


if __name__ == '__main__':
    gen_co = gen(1)  # Initialize the generator (1)

    a = next(gen_co)  # Advance the generator (2)
    print(a)

    b = next(gen_co)  # Advance again (3)
    print(b)

    c = next(gen_co)
    print(c)
