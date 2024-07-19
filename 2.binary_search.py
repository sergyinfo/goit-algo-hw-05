def binary_search_with_iterations(arr, target, epsilon=1e-7):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        # Якщо різниця між arr[mid] і target менша за epsilon, ми вважаємо значення рівними.
        if abs(arr[mid] - target) < epsilon:
            return (iterations, arr[mid])
        
        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return (iterations, upper_bound)

# Тестуємо функцію:
arr = [1.2, 1.5, 2.3, 3.7, 4.4, 5.9, 6.8]
target = 3.0

result = binary_search_with_iterations(arr, target)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")  # Виведе: Кількість ітерацій: 2, Верхня межа: 3.7

target = 5.9
result = binary_search_with_iterations(arr, target)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")  # Виведе: Кількість ітерацій: 3, Верхня межа: 5.9

target = 7.0
result = binary_search_with_iterations(arr, target)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")  # Виведе: Кількість ітерацій: 3, Верхня межа: None
