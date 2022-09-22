import argparse

def Result():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', nargs=1,  type=int)
    parser.add_argument('-w', nargs='+', type=int)
    parser.add_argument('-n', nargs=1, type=int)

    args = parser.parse_args()
    if len(args.w) != args.n[0]:
        print("Error!")
    else:
        q = args.W[0]
        a = [0] * (1000)
        a[0] = 1
        for i in args.w:
            for j in range(q, -1, -1):
                if a[j] == 1:
                    a[j + i] =1
        for i in range(q, -1, -1):
            if a[i] == 1 and i <= q:
                print(i)
                break

Result()