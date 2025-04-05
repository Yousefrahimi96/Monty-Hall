import streamlit as st
import random
import time

#title of application
st.image("pic.png")

count = st.number_input("Enter number of games to simulate", min_value=1, value=100)

#Create two list to hold win percentage for hold cases
wins_no_switch = 0
win_switch = 0

col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
chart1 = col1.line_chart(x=None, y=None, width=0, height=400)
chart1.add_rows([1.0]) # Add a row to ensure the chart y-axis starts at 1
col2.subheader("Win Percentage With Switching")
chart2 = col2.line_chart(x=None, y=None, width=0, height=400)
chart2.add_rows([1.0]) # Add a row to ensure the chart y-axis starts at 1


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

wins_no_switch = 0
wins_switch = 0

def count_result(count):
    result_count = []
    for _ in range(count):
        result_count.append(monty_hall(True))

    result = result_count.count(True) / count * 100
    print(result)

for i in range(count):
    #simulate one game at a time
    num_wins_with_switching = monty_hall(True)
    wins_switch += num_wins_with_switching
    chart2.add_rows([wins_switch / (i + 1)])
    
time.sleep(0.01)