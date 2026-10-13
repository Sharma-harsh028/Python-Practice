def print_scores(l,n):
    for i in range(len(l)):
        print(f"{l[i]} would be updated to {l[i] + n}")


def __main__():
    list1 = [67, 68, 72, 71, 69]
    n = 10
    print_scores(list1,n)

__main__()