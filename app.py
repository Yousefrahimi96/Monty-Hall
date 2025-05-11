import streamlit as st
import random
import time

# Title of the application.
st.image("./data/pic.png")

count = st.number_input("Enter number of games to simulate", min_value=1, value=100)

# Create variables to hold wins for both cases
wins_no_switch = 0
wins_switch = 0

col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
chart1 = col1.line_chart(x=None, y=None, width=0, height=400)
chart1.add_rows([1.0])  # Add a row to ensure the chart y-axis starts at 1.
col2.subheader("Win Percentage With Switching")
chart2 = col2.line_chart(x=None, y=None, width=0, height=400)
chart2.add_rows([1.0])  # Add a row to ensure the chart y-axis starts at 1.

doors = ['car'] + ['goat'] * 2

def monty_hall():
    """Simulate the Monty Hall problem and return outcomes for both strategies.
    
    Returns:
        tuple: (win_no_switch, win_switch) - True if won, False otherwise.
    """
    random.shuffle(doors)
    initial_choice = random.choice(range(3))
    revealed_door = [i for i in range(3) if i != initial_choice and doors[i] == 'goat'][0]
    final_choice_switch = [n for n in range(3) if n != initial_choice and n != revealed_door][0]
    win_no_switch = doors[initial_choice] == 'car'
    win_switch = doors[final_choice_switch] == 'car'
    return win_no_switch, win_switch

for i in range(count):
    # Simulate one game at a time.
    win_no_switch, win_switch = monty_hall()
    wins_no_switch += win_no_switch
    wins_switch += win_switch
    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])
    time.sleep(0.01)