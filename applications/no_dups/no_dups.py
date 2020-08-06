def no_dups(s):
    lst_of_keys = []
    if s == '':
        return ''
    l = s.split(' ')
    a = dict.fromkeys(l)
    for key in a.keys():
        lst_of_keys.append(key)
    return ' '.join(lst_of_keys)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))