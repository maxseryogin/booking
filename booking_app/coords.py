import random
cars = [
        'car1.png', 'car2.png', 'car3.png', 'car4.png', 'car5.png',
        'car6.png', 'car7.png'
]
areas = [
    {'coords': '0,0,218,284', 'spot_id': 1, 'alt': 'Место 1', 'x': '34px', 'y': '0px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '230,0,431,284', 'spot_id': 2, 'alt': 'Место 2', 'x': '260px', 'y': '0px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '442,0,644,284', 'spot_id': 3, 'alt': 'Место 3', 'x': '470px', 'y': '0px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '654,0,855,284', 'spot_id': 4, 'alt': 'Место 4', 'x': '680px', 'y': '0px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '866,0,1067,284', 'spot_id': 5, 'alt': 'Место 5', 'x': '890px', 'y': '0px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '1079,0,1280,284', 'spot_id': 6, 'alt': 'Место 6', 'x': '1100px', 'y': '0px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '0,526,202,818', 'spot_id': 7, 'alt': 'Место 7', 'x': '28px', 'y': '526px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '212,526,414,818', 'spot_id': 8, 'alt': 'Место 8', 'x': '230px', 'y': '526px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '442,526,644,818', 'spot_id': 9, 'alt': 'Место 9', 'x': '442px', 'y': '526px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '636,526,838,818', 'spot_id': 10, 'alt': 'Место 10', 'x': '650px', 'y': '526px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '850,526,1051,818', 'spot_id': 11, 'alt': 'Место 11', 'x': '870px', 'y': '526px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)},
    {'coords': '1062,526,1280,818', 'spot_id': 12, 'alt': 'Место 12', 'x': '1090px', 'y': '526px', 'rotation': random.choice([0, 180]), 'image': random.choice(cars)}
]
print(areas[0])