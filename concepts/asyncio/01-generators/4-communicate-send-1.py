# https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc

def gen():
    print("First number")
    a = yield 10

    # Here value of a is none becuase yeld returns the value, it does not assign the value to a
    print(f"Value of a inside gen is -> {a}")

    # print("Second number")
    # b = yield 20
    #
    # print("Addition result:", a + b)
    # c = yield


if __name__ == '__main__':
    gen_co = gen()  # Initialize the generator (1)

    x = next(gen_co)  # Advance the generator (2)
    print(f"Yielded value is {x}")

    y = next(gen_co)
