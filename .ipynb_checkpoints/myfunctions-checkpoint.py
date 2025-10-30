def find_two_smallest(numbers):
    smallest = numbers[0]
    second_smallest = numbers[1]
    
    if second_smallest < smallest:
        temp = smallest
        smallest = second_smallest
        second_smallest = temp

    for num in numbers[2:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return smallest, second_smallest