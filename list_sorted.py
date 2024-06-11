def alternate_low_high(numbers):
    sorted_numbers = sorted(numbers)
    result = []
    while sorted_numbers:
        if sorted_numbers:
            result.append(sorted_numbers.pop(0))  # Add the lowest number
        if sorted_numbers:
            result.append(sorted_numbers.pop(-1))  # Add the highest number
    return result

list_of_numbers = []
user_input = ""

print("Enter numbers one by one. Type 'end' to stop.")

while True:
    user_input = input()
    if user_input == "end":
        break
    try:
        number = float(user_input)  # Convert input to a number (integer or float)
        list_of_numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

# Display the numbers in the order they were entered (FIFO)
print("FIFO:")
print(' '.join(map(str, list_of_numbers)))

# Display the numbers from low to high
print("FROM LOW TO HIGH:")
low_high = sorted(list_of_numbers)
print(' '.join(map(str, low_high)))

# Display the numbers from high to low
print("FROM HIGH TO LOW:")
high_low = sorted(list_of_numbers, reverse=True)
print(' '.join(map(str, high_low)))

# Display the numbers alternating between low and high until they meet in the middle
print("ALTERNATING LOW TO HIGH:")
alternating_list = alternate_low_high(list_of_numbers)
print(' '.join(map(str, alternating_list)))