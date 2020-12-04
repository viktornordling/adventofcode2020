from math import prod

def valid_password(line):
    parts = line.split(" ")
    from_to = parts[0].split("-")
    from_l = from_to[0]
    to_l = from_to[1]
    letter = parts[1][0]
    password = parts[2]
    occ = len([c for c in password if c == letter])
    return occ >= int(from_l) and occ <= int(to_l)

def valid_password_2(line):
    parts = line.split(" ")
    from_to = parts[0].split("-")
    pos_1 = int(from_to[0])
    pos_2 = int(from_to[1])
    letter = parts[1][0]
    password = parts[2]
    pos1_eq = password[pos_1 - 1] == letter
    pos2_eq = password[pos_ - 1] == letter
    return (pos1_eq and not pos2_eq) or (pos2_eq and not pos1_eq)


passwords = open('easy.txt', 'r').readlines()
print("Part 1:", len([passw for passw in passwords if valid_password(passw)]))
print("Part 1:", len([passw for passw in passwords if valid_password_2(passw)]))