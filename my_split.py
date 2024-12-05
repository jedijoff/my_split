def mysplit(strng):
    splits = []
    pos = -1
    last_pos = -1
    filter = []
    while ' ' in strng[pos + 1:]:
        pos = strng.index(' ', pos + 1)
        splits.append(strng[last_pos + 1:pos])
        last_pos = pos

    splits.append(strng[last_pos + 1:])

    check_splits(splits)

    return splits

def check_splits(splits):
    for i in splits:
        if i == "":
            splits.remove(i)
            check_splits(splits)
        else:
            return splits



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))