# Binary Search Algorithm Implementation in Python

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid  # Target found
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1  # Target not found

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")