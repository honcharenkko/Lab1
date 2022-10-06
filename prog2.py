import argparse

parser = argparse.ArgumentParser()

parser.add_argument("z")
parser.add_argument("a", type=int)
parser.add_argument("b", type=int)

args = parser.parse_args()

def operator(z, a, b):
    if z == "add":
        print("Result: ", a + b)
    elif z == "min":
        print("Result: ", a - b)
    elif z == "mul":
        print("Result: ", a * b)
    elif z == "div":
        if b == 0:
            print("Делить на 0 нельзя!")
        else:
            print("Result: ", a / b)
operator(args.z, args.a, args.b)

