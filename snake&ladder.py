import tkinter as tk
import random

# Define the snakes and ladders positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Initialize player position
player_position = 0


def roll_dice():
    global player_position
    dice_roll = random.randint(1, 6)
    player_position += dice_roll

    # Check if the player landed on a snake or ladder
    if player_position in snakes:
        player_position = snakes[player_position]
    elif player_position in ladders:
        player_position = ladders[player_position]

    # Make sure the player doesn't exceed 100
    if player_position > 100:
        player_position = 100

    # Update the labels
    dice_label.config(text=f"Dice Roll: {dice_roll}")
    position_label.config(text=f"Player Position: {player_position}")

    # Update the player's position on the board
    update_board()


def update_board():
    # Clear the board (reset the grid)
    for i in range(100):
        board_labels[i].config(bg="white")

    # Set the player's position (colored square)
    board_labels[player_position - 1].config(bg="red")


# Create the main window
root = tk.Tk()
root.title("Snake and Ladder Game")

# Create a frame to hold the board
board_frame = tk.Frame(root)
board_frame.grid(row=0, column=0, padx=10, pady=10)

# Create 100 labels (for each square on the board)
board_labels = []
for i in range(100):
    label = tk.Label(board_frame, text=str(i + 1), width=4, height=2, relief="solid", font=("Arial", 10))
    board_labels.append(label)
    label.grid(row=i // 10, column=i % 10)

# Initial empty labels for player position and dice roll
dice_label = tk.Label(root, text="Dice Roll: 0", font=("Arial", 14))
dice_label.grid(row=1, column=0, pady=5)

position_label = tk.Label(root, text="Player Position: 0", font=("Arial", 14))
position_label.grid(row=2, column=0, pady=5)

# Create a roll button
roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14), command=roll_dice)
roll_button.grid(row=3, column=0, pady=10)

# Run the game
root.mainloop()
