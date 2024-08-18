import copy
import random

# Hat class definition
class Hat:
    def __init__(self, **kwargs):
        # Initialize the Hat with balls of different colors.
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num):
        # Draws a specified number of balls from the hat at random.
        if num > len(self.contents):
            return self.contents
        draws = random.sample(self.contents, num)
        for draw in draws:
            self.contents.remove(draw)
        return draws

# Function to perform the experiment and calculate the probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Calculate the probability of drawing the expected balls in a series of experiments.
    successful_draws = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn) # here the draw method is used with in the experiment function
        
        # Check if the drawn balls match or exceed the expected balls
        if all(drawn.count(ball) >= count for ball, count in expected_balls.items()):
            successful_draws += 1

    return (successful_draws / num_experiments) * 100

# Function to validate numeric input
def validate_input_num(input_description=": "):
    while True:
        try:
            num = int(input(input_description))
            if num >= 0:
                return num
            else:
                print('=== Input must be a non-negative integer ===')
        except ValueError:
            print('=== Invalid Input ===')

# Function to calculate remaining balls distribution
def calculate_remaining_balls_distribution(colors, num_balls):
    # Randomly distribute the total number of balls among the specified colors.
    ball_distribution = {}
    remaining_balls = num_balls

    for color in colors[:-1]:
        ball_distribution[color] = random.randint(1, remaining_balls - (len(colors) - len(ball_distribution) - 1))
        remaining_balls -= ball_distribution[color]

    ball_distribution[colors[-1]] = remaining_balls
    return ball_distribution

# Main function to run the program
def main():
    # Define the number of balls
    num_balls = validate_input_num("Enter the total number of balls in the hat: ")

    # Define the available colors
    colors = ["yellow", "blue", "green", "black"]

    # Generate a random distribution of balls
    ball_distribution = calculate_remaining_balls_distribution(colors, num_balls)
    print(f"\nYour hat has the following ball distribution:\n{ball_distribution}")

    # Define the number of balls to draw
    while True:
        num_balls_drawn = validate_input_num("Enter the number of balls to draw: ")
        if num_balls_drawn <= num_balls:
            break
        else:
            print(f"=== The number exceeds the total amount of balls ({num_balls}) ===")

    # If drawing all balls, the probability is 100%
    if num_balls_drawn == num_balls:
        print("The probability of drawing all colors is 100% when drawing the total amount of balls.")
        return

    # Asking the user how many of each color they want to draw
    expected_balls = {}
    for color in colors:
        max_draw = min(ball_distribution[color], num_balls_drawn)
        while True:
            expected_balls[color] = validate_input_num(f"Enter the number of {color} balls to draw (max {max_draw}): ")
            if expected_balls[color] <= max_draw:
                num_balls_drawn -= expected_balls[color]
                break
            else:
                print(f"=== The number of {color} balls to draw must not exceed {max_draw} ===")

        # If all balls to be drawn have been assigned, break out of the loop
        if num_balls_drawn == 0:
            break

    # Validate that the sum of expected balls does not exceed the number of balls to draw
    if sum(expected_balls.values()) > num_balls:
        print(f"=== The total number of balls to draw exceeds {num_balls} ===")
        return

    # Define the number of experiments
    num_experiments = validate_input_num("Enter the number of experiments to perform: ")

    # Create the Hat object
    hat = Hat(**ball_distribution)

    # Calculate and display the probability
    probability = experiment(hat, expected_balls, sum(expected_balls.values()), num_experiments)
    print(f"\nProbability of drawing the expected balls: {probability:.2f}%")

# Run the main function
if __name__ == "__main__":
    main()