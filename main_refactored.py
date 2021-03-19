import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# A writing "turtle" that will write in the names of correctly guessed states:
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Converting "50_states.csv" file to a Pandas dataframe to work with. 2 columns (x and y coord.), rows with state names:
data = pandas.read_csv("50_states.csv")
# Saving all the states in a list:
states = [state for state in data.state]

# A list to keep track of correctly guessed names:
correct_guesses = []

# A list of states not guessed:
missing_states = []

# Check if the guess is among the 50 states. If it is, the state name is printed onto its location on the map
# The value is appended to the correct_guesses list:
while len(correct_guesses) < 50:
    guess_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                   prompt="Enter a state name!").title()
    if guess_state == "Exit":
        # populating a list of states not guessed by the player:
        missing_states = [st for st in states if st not in correct_guesses]
        break
    else:
        for st in states:
            if guess_state == st:
                correct_guesses.append(st)
                x_coor = int(data[data.state == st]['x'])
                y_coor = int(data[data.state == st]['y'])
                writer.goto(x_coor, y_coor)
                writer.write(st)

# Creating "states to learn" .csv file so the user can learn the names of all the states:
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")