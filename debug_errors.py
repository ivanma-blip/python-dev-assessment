def calculate_average(numbers):
    total = 0
    result = None
    try:
        for i in range(len(numbers)):
            total += numbers[i]
        result = total / len(numbers)
    except ZeroDivisionError:
        print("List is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        return result


def get_list_element(my_list, index):
    try:
        return my_list[index]
    except TypeError:
        print("Error: Invalid input type. Please provide a list")
    except IndexError:
        print("Error: Index out of range.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  # This will cause an error
data4 = 22  # This will cause an error
print("\nCalculating averages:")
print(f"Average of data1: {data1} is {calculate_average(data1)}")
print(f"Average of data2: {data2} is {calculate_average(data2)}")
print(
    f"Average of data3: {data3} is {calculate_average(data3)}"
)  # This will cause an error
print(
    f"Average of data4: {data4} is {calculate_average(data4)}"
)  # This will cause an error


print("\nAccessing list elements:")
print(f"Element at index 2 in data1: {get_list_element(data1, 2)}")
print(
    f"Element at index 5 in data1: {get_list_element(data1, 5)}"
)  # This will cause an error
print(
    f"Element at index 0 in data3: {get_list_element(data3, 0)}"
)  # This will cause an error
print(
    f"Element at index 0 in data4: {get_list_element(data4, 0)}"
)  # This will cause an error
