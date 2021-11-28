INT_COUNT = 3
FLOAT_COUNT = 3
BOOL_CONST = False

int_nums = []
float_nums = []

for i in range(INT_COUNT):
    int_num = int(input(f'Введіть ціле число #{i + 1}: '))
    int_nums.append(int_num)

for i in range(FLOAT_COUNT):
    float_num = float(input(f'Введіть дійсне число #{i + 1}: '))
    float_nums.append(float_num)

print('\nВідображення оператором %:')
for i in range(INT_COUNT):
    print('%4d' % int_nums[i], end=' ')
for i in range(FLOAT_COUNT):
    print('%.11e' % float_nums[i], end=' ')
for i in range(FLOAT_COUNT):
    print('%6.3f' % float_nums[i], end=' ')
print('%.5s' % str(BOOL_CONST))

print('\nВідображення методом str.format():')
for i in range(INT_COUNT):
    print('{:>4d}'.format(int_nums[i]), end=' ')
for i in range(FLOAT_COUNT):
    print('{:.11e}'.format(float_nums[i]), end=' ')
for i in range(FLOAT_COUNT):
    print('{:6.3f}'.format(float_nums[i]), end=' ')
print('{:.5}'.format(str(BOOL_CONST)))

print('\nВідображення f-рядком:')
for i in range(INT_COUNT):
    print(f'{int_nums[i]:>4d}', end=' ')
for i in range(FLOAT_COUNT):
    print(f'{float_nums[i]:.11e}', end=' ')
for i in range(FLOAT_COUNT):
    print(f'{float_nums[i]:6.3f}', end=' ')
print('{:.5}'.format(str(BOOL_CONST)))
