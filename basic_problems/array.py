##
# Problem: Given an array of integers, find the maximum product of two numbers.
# Example: arr = [1, 20, 3, 4, 5]
# Output: 100 (20 * 5)

def max_product(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a product

    max1 = max(arr)
    arr.remove(max1)
    max2 = max(arr)

    return max1 * max2

# Example usage
if __name__ == "__main__":
    arr = [1, 20, 3, 4, 5]
    result = max_product(arr)
    print(f"The maximum product of two numbers in the array is: {result}")