def number_to_word():
    """
    Преобразует число от 1 до 5 в соответствующее английское слово
    """
    number_map = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }
    
    while True:
        try:
            num = int(input("Enter a number (1-5): "))
            if 1 <= num <= 5:
                print(f"The number is: {number_map[num]}")
                break
            else:
                print("Please enter a number between 1 and 5")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    number_to_word()
