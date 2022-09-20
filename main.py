# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union, Optional
from computer import Computer
from oo_resale_shop import ResaleShop

def main():
    
    # First, let's make a computer
    computer = Computer.create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    # Call an instance of ResaleShop class. Name it ResaleStore.
    inventory = {}
    ResaleStore = ResaleShop(inventory)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    computer_id = ResaleStore.buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleStore.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    ResaleStore.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleStore.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    ResaleStore.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleStore.print_inventory()
    print("Done.\n")

    # Check if error message is printed by setting item_id to arbritrary value of 99
    #for refurbish
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", 99, ", updating OS to", new_OS)
    print("Updating inventory...")
    ResaleStore.refurbish(99, new_OS)
    print("Done.\n")
    #for sell
    print("Selling Item ID:", 99)
    ResaleStore.sell( 99)

# Calls the main() function when this file is run
if __name__ == "__main__": main()
