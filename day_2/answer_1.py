with open('input_values.txt', 'r') as file:
    config = [l.split(':') for l in file.readlines()]

valid_passwords = []

for item in config:
    lower_bound = item[0].split(' ')[0].split('-')[0]
    upper_bound = item[0].split(' ')[0].split('-')[1]
    letter = item[0].split(' ')[1]
    password = item[1]
    letter_count = item[1].count(letter)

    if int(lower_bound) <= letter_count <= int(upper_bound):
        valid_passwords.append(password)


print(len(valid_passwords))