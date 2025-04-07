# Monty Hall Problem Simulator

## Overview

This project is an interactive simulation of the Monty Hall problem, a well-known probability puzzle derived from a game show scenario. It demonstrates the probability of winning a car by either sticking with an initial door choice or switching doors after a losing option (a goat) is revealed. The project includes a Python script for running simulations and a Streamlit web application for visualizing results, accompanied by an image (`pic.png`) that illustrates the problem.

## Project Structure

### Files

1. **Monty Hall Simulation Script (`monty_hall.py`)**
   - A Python script that simulates the Monty Hall problem.
   - Prompts the user to input the number of simulations and calculates the win percentage when switching doors.
   - Utilizes the `random` module for door shuffling and selection.

2. **Streamlit Web Application (`app.py`)**
   - A web-based interface built with Streamlit to visualize the Monty Hall problem.
   - Features two line charts comparing win percentages for switching and not switching.
   - Includes a user input field for the number of simulations, with real-time chart updates.
   - Displays the provided image (`pic.png`) as the application header.

3. **Requirements File (`requirements.txt`)**
   - Lists the required dependency: `streamlit==1.43.1`.

4. **Image File (`pic.png`)**
   - A visual representation of the Monty Hall problem featuring three doors labeled 1, 2, and 3.
   - Door 3 is open, revealing a cartoon goat with a brown body, a single white horn, and one visible eye.
   - Doors 1 and 2 are closed, each marked with a yellow question mark (?) indicating unknown contents (car or goat).

## Detailed Description

### Image Analysis (`pic.png`)

The `pic.png` image is a simple illustration designed to represent the Monty Hall problem, with the following elements:

- **Doors**: Three blue doors, each with a black doorknob on the right:
  - **Door 1**: On the left, labeled "1" in black, with a large yellow question mark (?) indicating an unknown prize.
  - **Door 2**: In the middle, labeled "2" in black, also with a yellow question mark (?) for an unknown prize.
  - **Door 3**: On the right, labeled "3" in black, fully open to reveal a cartoon goat.
- **Goat**: A stylized goat behind Door 3, featuring:
  - A brown body with a slightly curved shape.
  - One white horn on the left side of its head.
  - A single large eye with a black pupil, giving a curious expression.
  - Long, thin legs, with the front left leg slightly bent.
- **Background**: Solid black, contrasting with the blue doors and brown goat for clarity.
- **Purpose**: The image aids in explaining the Monty Hall problem, where a contestant picks one of three doors (one hiding a car, two hiding goats), the host reveals a goat, and the contestant decides to stick or switch.

### Code Analysis

#### `monty_hall.py`
- **Functionality**: Simulates the Monty Hall problem with an option to switch doors.
- **Key Components**:
  - `doors = ['car'] + ['goat'] * 2`: Initializes a list with one car and two goats.
  - `monty_hall(switch)`: Simulates a single game:
    - Shuffles the doors randomly.
    - Selects an initial choice.
    - Reveals a goat from the remaining doors.
    - Returns `True` if the final choice (with or without switching) wins the car.
  - `count_result(count)`: Runs multiple simulations and calculates the win percentage when switching.
- **Usage**: Users input the number of simulations, and the script prints the win percentage for switching.

#### `app.py`
- **Functionality**: Creates an interactive Streamlit web application.
- **Key Components**:
  - `st.image("pic.png")`: Displays the image as the app header.
  - `st.number_input`: Allows users to specify the number of simulations (default: 100).
  - Two line charts:
    - Tracks win percentage without switching.
    - Tracks win percentage with switching.
  - `monty_hall()`: Simulates a game, returning outcomes for both strategies (switching and not switching).
  - Real-time updates with `time.sleep(0.01)` to animate the chart progression.
- **Usage**: Users input the simulation count and observe dynamic updates to the win percentage charts.

#### `requirements.txt`
- Specifies the required library: `streamlit==1.43.1`, ensuring compatibility with the web app.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd monty-hall-simulator

2. **Install Dependencies:**:
   ```bash
   pip install -r requirements.txt

3. **Run the Application:**:

For the script
   ```bash
   python monty_hall.py
```
For the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

- **Script (`monty_hall.py`)**:
  - Run the script and enter the number of simulations when prompted.
  - View the printed win percentage for the switching strategy.

- **Web App (`app.py`)**:
  - Launch the Streamlit app in a browser.
  - Input the desired number of simulations.
  - Observe real-time line charts comparing win percentages for switching and not switching.