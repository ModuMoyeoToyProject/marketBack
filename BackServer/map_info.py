with open('MapData.txt', 'r', encoding='utf-8') as file:
    count = 0
    for line in file.readlines():
        print(line.strip())