def get_starting_number():
    while True:
        try:
            number = int(input("How many bottles of beer on the wall? "))
            if number >= 1:
                return number
            else:
                print("Please enter an integer 1 or greater.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
def sing(start):
    bottles = start
    while bottles > 0:
        if bottles > 1:
            next_bottles = bottles - 1
            if bottles > 1:
                bottle_word = "bottles"
            else:
                bottle_word= "bottle"
            if next_bottles != 1:
                next_bottle_word = "bottles"
            else:
                 next_bottle_word = "bottle"
            print(f"{bottles} {bottle_word} of beer on the wall, {bottles} {bottle_word} of beer.")
            if next_bottles > 0:
                print(f"Take one down, pass it around, {next_bottles} {next_bottle_word} of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, no more bottles of beer on the wall!\n")
            bottles -= 1
        else: 
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
            bottles -= 1

