import argparse

parser = argparse.ArgumentParser()

parser.add_argument("a", type=int)
parser.add_argument("z")
parser.add_argument("b", type=int)

args = parser.parse_args()

def operator(a, z, b):
    if z == "+":
        print("Result: ", a + b)
    elif z == "-":
        print("Result: ", a - b)
    elif z == "*":
        print("Result: ", a * b)
    elif z == "/":
        if b == 0:
            print("Делить на 0 нельзя!")
        else:
            print("Result: ", a / b)
operator(args.a, args.z, args.b)
