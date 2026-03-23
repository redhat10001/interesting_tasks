print('*' * 25)

show_manth = ['January',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December'
]

show_dict = {}

for num in range(1, len(show_manth) + 1):
    num_key = str(num)
    manth_dict = {}

    for manth in show_manth:
        manth_key = manth
        manth_dict[manth_key] = []

        show_dict[num_key] = manth_dict

for i in range(1, 6):
    for num_key in show_dict:
        for manth_key in manth_dict:
            show_dict[num_key][manth_key].append(i)

for key, value in show_dict.items():
    for k, v in sorted(value.items()):
        print(f'{key:2} {k:9} {v}')

print()
print('*' * 30)
print()

lst = [['04', '05', '1993', '1.068'], ['04', '12', '1993', '1.079'],
       ['04', '19', '1993', '1.079'], ['04', '26', '1993', '1.086']]

my_dct = {}
for i in lst:
    if (i[-2], i[0]) not in my_dct:
        my_dct[(i[-2], i[0])] = [i[-1]]
    else:
        my_dct[(i[-2], i[0])] += [i[-1]]
print(my_dct)

print()
print('*' * 30)
print()

#a = list(map(float, input().split()))
#a = list(input().split())
a = [1, 2, 3]

tree_dict = a[-1]
print(tree_dict)

for key in reversed(a[:-1]):
    tree_dict = {key: tree_dict}

print(tree_dict)

print()
print('*' * 30)
print()

nk_lst = ['CS101', 'CS102', 'CS103', 'NT110', 'CM241']
na_lst = ['3004', '4501', '6755', '1244', '1411']

dct_nk = {nk_lst[i]: na_lst[i] for i in range(len(nk_lst))}
print(dct_nk)