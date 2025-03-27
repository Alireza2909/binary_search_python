# Binary Search Algorithm in Python

This repository contains the implementation of the Binary Search algorithm in Python.

## How to use

1. Clone this repository.
2. Run the `binary_search.py` file with Python.
3. The `binary_search(arr, target)` method searches for the target value in a sorted array.

## Example

```python
arr = [1, 3, 5, 7, 9, 11]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")