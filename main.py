import random

doors = ['goat', 'car', 'goat']

def monty_hall(switch):
    random.shuffle(doors)
    initial_choice = random.choice(range(3))
    open_door = [i for i in range(3) if i != initial_choice and doors[i] == 'goat'][0]
    
    if switch:
        final_choice = [n for n in range(3) if n != initial_choice and n != open_door][0]
    else:
        final_choice = initial_choice
        
    return doors[final_choice] == 'car'


def count_resault(count):
    resuly_count = []
    for _ in range(count):
        resuly_count.append(monty_hall(True))

    resault = resuly_count.count(True)/count*100
    print(resault)

if __name__ == '__main__':
    count = int(input('How many do you want to repeat the geame: '))
    count_resault(count)