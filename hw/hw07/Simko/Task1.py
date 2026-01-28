def largest_number(numbers): 
    """Return the largest number of two numbers."""
    if not numbers:
        return None
    return max(numbers)
print(largest_number([10, 200])) # Expected output: 200 