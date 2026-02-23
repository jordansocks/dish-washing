import sys
import time
import random

# dishes = random.randint(1,5)
dishes = int(random.triangular(1,11,2))

def intro():
    global dishes
    if dishes == 1:
        print(f"There is only {dishes} dish to wash - lucky!")
        time.sleep(2)
        print("Still, the dish must be washed.")
        time.sleep(2)
    elif dishes > 1 and dishes < 7:
        print(f"There are {dishes} dishes to wash.")
        time.sleep(2)
        print("The dishes must be washed.")
        time.sleep(2)
    elif dishes > 6:
        print(f"There are {dishes} dishes to wash. Yikes.")
        time.sleep(2)
        print("Well, they won't wash themselves.")
        time.sleep(2)

# Makes a cute lil loading graphic
def timer():
    global dishes
    for _ in range(10):
        sys.stdout.write("#")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\nNice, the dish is washed.")
    dishes = dishes - 1
    time.sleep(1)

# Prompts washer to ask if they'd like to wash a dish
def prompt_washer():
    time.sleep(1)
    print("Would you like to wash a dish? (y/n)")
    user_input = input(">")
    if user_input == 'y':
        wash_dishes()
    elif user_input == 'n':
        time.sleep(1)
        print("You were late. The dishes must be washed.")
        time.sleep(1)
        prompt_washer()
    else:
        time.sleep(1)
        print("That's simply not an option.")
        time.sleep(1)
        prompt_washer()


# Wash x number of dishes - consequence of 'y' answer
def wash_dishes():
    global dishes
    timer()
    if dishes == 0:
        time.sleep(1)
        print("All done. The dishes have been washed, and lessons have been learned.")
        exit()
    elif dishes == 1:
        time.sleep(1)
        print(f"There is {dishes} dish remaining.")
        time.sleep(1)
    else:
        time.sleep(1)
        print(f"There are {dishes} dishes remaining.")
        time.sleep(1)
    prompt_washer()

def main():
    intro()
    prompt_washer()

if __name__ == "__main__":
    main()