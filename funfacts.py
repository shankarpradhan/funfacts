import random
import time

def get_random_fun_fact():
    # List of fun facts
    fun_facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "Octopuses have three hearts. Two pump blood through the gills, while the third pumps it through the rest of the body.",
        "A group of flamingos is called a flamboyance.",
        "Bananas are berries, but strawberries are not.",
        "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the iron on hot days.",
        "The unicorn is the national animal of Scotland.",
        "There are more possible iterations of a game of chess than there are atoms in the known universe.",
        "Penguins propose to their mates with a pebble.",
        "The inventor of the Pringles can was cremated and buried in one.",
        "A group of pugs is called a grumble.",
        "Sea otters hold hands while sleeping to keep from drifting apart.",
        "Banging your head against a wall for one hour burns 150 calories.",
        "Rats laugh when tickled.",
        "The speed of a computer mouse is measured in 'Mickeys'.",
        "Cows have best friends and become stressed when they are separated."
    ]

    # Pick a random fun fact
    random_fact = random.choice(fun_facts)
    return random_fact

def main():
    print("Welcome to the Random Fun Facts Generator!")
    print("Press Ctrl+C to exit.\n")

    try:
        while True:
            input("Press Enter to get a random fun fact...")
            fact = get_random_fun_fact()
            print("\nFun Fact: {}\n".format(fact))
            time.sleep(1)  # Pause for 1 second before allowing another fact
    except KeyboardInterrupt:
        print("\nThank you for using the Random Fun Facts Generator!")

if __name__ == "__main__":
    main()
