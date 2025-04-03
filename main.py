import random

doors = ['car'] + ['goat'] * 2

def monty_hall(switch):
    """Simulate the Monty Hall problem with an option to switch doors.
    
    Args:
        switch (bool): Whether to switch the initial choice or not.
    
    Returns:
        bool: True if the car is won, False otherwise.
    """
    random.shuffle(doors)
    initial_choice = random.choice(range(3))
    revealed_door = [i for i in range(3) if i != initial_choice and doors[i] == 'goat'][0]
    
    if switch:
        final_choice = [n for n in range(3) if n != initial_choice and n != revealed_door][0]
    else:
        final_choice = initial_choice
        
    return doors[final_choice] == 'car'


def count_result(count):
    result_count = []
    for _ in range(count):
        result_count.append(monty_hall(True))

    result = result_count.count(True) / count * 100
    print(result)

if __name__ == '__main__':
    count = int(input('How many do you want to repeat the game: '))
    count_result(count)