from .models import Map

def map_init():
    Map.objects.all().delete()
    with open('MapData.txt', 'r', encoding='utf-8') as file:
        count = 0
        mapID = 0
        location = ''
        lvl = 0
        coordinate = ''
        street = ''
        for line in file.readlines():
            print(line)
            line = line.strip().split()[1]
            if count == 0:
                mapID = line
                count += 1
                continue

            if count == 1:
                location = line
                count += 1
                continue

            if count == 2:
                lvl = line
                count += 1
                continue

            if count == 3:
                coordinate = line
                count += 1
                continue

            if count == 4:
                street = line
                map_ = Map(mapID=mapID,
                           location=location,
                           required_level=lvl,
                           coordinate=coordinate,
                           street=street)
                count = 0
                map_.save()