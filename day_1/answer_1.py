with open('input_values.txt', 'r') as values:
    list_config = [v.strip('\n') for v in values.readlines()]

list_len = len(list_config)

for i in range(list_len-1):

    for n in range(i, list_len-1):
        val_1 = int(list_config[i])
        val_2 = int(list_config[n])

        if val_1+val_2 == 2020:
            print(val_1)
            print(val_2)
            print(val_1*val_2)