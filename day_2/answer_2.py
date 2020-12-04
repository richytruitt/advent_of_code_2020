with open('input_values.txt', 'r') as file:
    config = [l.split(':') for l in file.readlines()]

valid_passwords = []

for item in config:
    pos1 = int(item[0].split(' ')[0].split('-')[0])
    pos2 = int(item[0].split(' ')[0].split('-')[1])
    letter = item[0].split(' ')[1]
    password = item[1]

    if password[pos1] == password[pos2]:
        continue

    if password[pos1] == letter or password[pos2] == letter:
        valid_passwords.append(password)


print(len(valid_passwords))