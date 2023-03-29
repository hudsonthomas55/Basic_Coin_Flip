# Imports
import random
from tkinter import *

# Window setup
window = Tk()
window.minsize(width=500, height=250)
window.title("Coin Flip")
window.config(padx=50, pady=50)

# Create program
def run_program():
    """Runs the coin flip program"""

    # Define coin, two sides to coin
    coin = [1,2]

    # Define coin flip process
    coin_outcome = random.choice(coin)

    # Assign heads
    if coin_outcome == 1:
        print("Heads!")

    # Assign tails
    elif coin_outcome == 2:
        print("Tails!")

    # Allow for troubleshooting
    else:
        print("error")

# Create button to run program
coin_button = Button(text="Flip Coin", width=50, command=run_program)
coin_button.pack()

# Run window
window.mainloop()
