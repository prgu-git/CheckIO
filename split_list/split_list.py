def split_list(items: list) -> list:
    # your code here
    return [items]

def split_list(lst):
    lst1 = []
    lst2 = []
    number=int(len(lst)/2)
    if(len(lst)/2==0):
        lst1 = lst[0:number]
        lst2 = lst[number:]
    else:
        lst1 = lst[0:len(lst)-number]
        lst2 = lst[len(lst)-number:]

    return lst1, lst2


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    split_list([1, 2, 3]) == [[1, 2], [3]]
    split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    split_list([1]) == [[1], []]
    split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
