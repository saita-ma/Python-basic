def common_elements():
    three = []
    five = []
    for _ in range(100):
        if _ % 3 == 0:
            three.append(_)
    for _ in range(100):
        if _ % 5 == 0:
            five.append(_)
    common = [i for i in three if i in five]
    return set(common)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')

