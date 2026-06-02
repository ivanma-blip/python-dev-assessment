def filter_and_sort_evens(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    even_numbers.sort()
    return even_numbers


def count_character_frequency(text, countSpaces=True):
    frequencies = {}
    for character in text.lower():
        if character.isspace() and not countSpaces:
            continue
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1

    return frequencies


# Sorting and filtering even numbers from a list
print("\n\nSorting and filtering even numbers from a list:")
list_of_numbers = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
print(f"Original list of numbers: {list_of_numbers}")

filtered_sorted_evens = filter_and_sort_evens(list_of_numbers)
print(f"\nFiltered and sorted even lists of numbers: {filtered_sorted_evens}")


# Counting character frequency in a string
print("\n\nCounting character frequency in a string:")
original_text = "This my task for Basic Data Structures & Algorithms"
print(f"Original text: '{original_text}'")


# Counting character frequency in a string with counting spaces
character_frequencies_with_spaces = count_character_frequency(
    original_text, countSpaces=True
)
print("\nCharacter frequencies (counting spaces):")
for character, frequency in character_frequencies_with_spaces.items():
    print(f"'{character}': {frequency}")

# Counting character frequency in a string without counting spaces
character_frequencies_without_spaces = count_character_frequency(
    original_text, countSpaces=False
)
print("\nCharacter frequencies (without counting spaces):")
for character, frequency in character_frequencies_without_spaces.items():
    print(f"'{character}': {frequency}")
