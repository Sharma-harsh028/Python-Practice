def avg_list(list1):
    sum = 0
    for i in range(len(list1)):
        sum = sum + list1[i]
    avg = round(sum/len(list1))
    return avg

def __main__():
    list1 = [1, 2, 3 ,4 ,5]
    avg = avg_list(list1)
    print(f"Average of list is {avg}")

__main__()