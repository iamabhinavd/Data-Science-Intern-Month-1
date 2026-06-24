"""
Week 2: Hands-On Data Structures and Transformations
Tasks: Sum of squares, list filtering, and experimenting with various data types.
"""

def sum_of_squares(numbers):
    """Calculates the sum of squares using a standard for-loop."""
    total = 0
    for num in numbers:
        total += num ** 2
    return total

def sum_of_squares_comprehension(numbers):
    """Calculates sum of squares elegantly using list comprehension and sum()."""
    return sum([num ** 2 for num in numbers])

def filter_even_numbers(numbers):
    """Filters out odd numbers using standard list comprehension."""
    return [num for num in numbers if num % 2 == 0]

def demo_advanced_concepts():
    print("--- Advanced Python Paradigms Demo ---")
    
    # 1. Lambda Functions
    # Quick function to cube a number
    cube = lambda x: x ** 3
    print(f"Lambda cube of 5: {cube(5)}")
    
    # 2. Recursion
    # Factorial calculation: n! = n * (n-1)!
    def factorial(n):
        if n == 1 or n == 0:  # Base case
            return 1
        return n * factorial(n - 1)  # Recursive case
    print(f"Recursion factorial of 5: {factorial(5)}")

    # 3. Tuple, Set, and Dictionary operations
    raw_coordinates = [(1, 2), (2, 3), (1, 2)]  # List of tuples
    unique_coords = set(raw_coordinates)        # Set removes duplicates
    print(f"Unique coordinates (Set): {unique_coords}")
    
    # Dictionary mapping users to locations
    user_profiles = {"Alice": "New York", "Bob": "London"}
    print(f"User Profile Lookup: Alice lives in {user_profiles.get('Alice')}")


if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5]
    
    print("--- Basic Transformations ---")
    print(f"Original Dataset: {sample_data}")
    print(f"Sum of Squares (Loop): {sum_of_squares(sample_data)}")
    print(f"Sum of Squares (Comprehension): {sum_of_squares_comprehension(sample_data)}")
    print(f"Filtered Dataset (Even numbers only): {filter_even_numbers(sample_data)}\n")
    
    demo_advanced_concepts()