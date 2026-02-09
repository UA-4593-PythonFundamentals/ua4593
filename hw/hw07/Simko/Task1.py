def largest_number(numbers): 
    """Return the largest number of two numbers."""
    if not numbers:
        return None
    return max(numbers)
print(largest_number([100, 6000])) # Expected output: 6000 