# Import module
import random

# Define coin, two sides to coin
coin = [1,2]

# Define coin flip process
coin_flip = input("Please press 'Enter' to flip the coin. ")
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
