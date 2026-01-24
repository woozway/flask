guests = {}
def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        entry = yield name, age
        if entry is not None:
            with open(file_name, 'a') as f:
                f.write('\n' + entry)


print('Checkpoint #1')
print('=' * 20)
rg = read_guestlist('guest_list.txt')
for _ in range(10):
    print(next(rg))

print('\nCheckpoint #2')
print('=' * 20)
print(rg.send("Jane,35"))

print('\nCheckpoint #3')
print('=' * 20)
for guest in rg:
    print(guest)

print('\nCheckpoint #4')
print('=' * 20)
age_over_21 = (name for name, age in guests.items() if age >= 21)
print(list(age_over_21))

print('\nCheckpoint #5')
print('=' * 20)

def table(x, food):
    for y in range(1, 6):
        yield food, f'Table {x}', f'Seat {y}'

def connected_tables():
    yield from table(1, 'Chicken')
    yield from table(2, 'Beef')
    yield from table(3, 'Fish')

print('\nCheckpoint #6')
print('=' * 20)
def meal(guests, seats):
    for name in guests:
        yield(name, next(seats))

feast = meal(guests, connected_tables())
for x in feast:
    print(x)
