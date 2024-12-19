# [1, 3, 5] => 30
# [6] => 36
# [] => 0
list_1 = [1, 3, 5]
print(list_1)
if len(list_1)==0:
    print(0)
else:
    sum_list = 0
    for i in range(0, len(list_1), 2):
        sum_list=sum_list+list_1[i]
    print(sum_list*list_1[-1])