def search_closest(n, array):
    closest_distance = float('inf')
    closest_number = 0

    for num in array:
        distance = abs(n - num)

        if distance <= closest_distance:
            closest_distance = distance
            closest_number = num

    return closest_number


test1 = [-1.5, 0, 4.4, 5, 6, 7]
test2 = [-1.5, 0, 4.4, 5, 6, 7]

print(search_closest(4.5, test1))
print(search_closest(5.5, test2))
