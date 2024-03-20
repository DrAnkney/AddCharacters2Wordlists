import itertools
import sys
import os

# Define the character sets
digits = "0123456789"
specials = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

# function that will add characters from a chosen character set onto the end of 
# words from the wordlist
def generate_variations(word, addons, characters, prepend=True):
    for chars in itertools.product(characters, repeat=addons):
        variation = f"{''.join(chars)}{word}" if prepend else f"{word}{''.join(chars)}"
        yield variation
        
# function to use character set chosen in main() user prompt
def get_character_set_name(characters):
    if characters == digits:
        return "digits"
    elif characters == specials:
        return "specials"
    elif characters == digits + specials:
        return "mixeddigitsspecials"
    else:
        return "unknown"

def main():
    # Prompt user for the wordlist file
    wordlist = input("Enter the path to the wordlist file: ")

    # Prompt user to choose character set combination
    print("Choose character set combination:")
    print("1. Digits only")
    print("2. Specials only")
    print("3. Mixed digits and specials")
    choice = input("Enter your choice: ")

    if choice == "1":
        characters = digits
    elif choice == "2":
        characters = specials
    elif choice == "3":
        characters = digits + specials
    else:
        print("Invalid choice. Using mixed digits and specials as the default character set.")
        characters = digits + specials

    # Prompt user for minimum and maximum length of additional characters
    min_length = int(input("Enter the minimum length of additional characters: "))
    max_length = int(input("Enter the maximum length of additional characters: "))

    # Ask user whether to prepend or append characters
    prepend_choice = input("Enter 'a' to append characters or 'p' to prepend characters: ").lower()
    prepend = True if prepend_choice == "p" else False

    # Get the base name of the wordlist file without extension
    base_name = os.path.splitext(os.path.basename(wordlist))[0]

    # Get the character set name based on the user's choice
    character_set_name = get_character_set_name(characters)

    # Read words from the dictionary file
    with open(wordlist, "r") as f:
        words = f.read().splitlines()

    # Generate password variations and save to a file
    with open(f"{base_name}_{character_set_name}_{'prepend' if prepend else 'append'}.txt", "w") as output_file:
        for word in words:
            for addons in range(min_length, max_length + 1):
                for variation in generate_variations(word, addons, characters, prepend):
                    output_file.write(variation + "\n")
    # Inform user where to find new wordlist
    print(f"The modified wordlist can be found in {base_name}_{character_set_name}_{'prepend' if prepend else 'append'}.txt.")

if __name__ == "__main__":
    main()
