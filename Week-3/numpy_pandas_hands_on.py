"""
Week 3: Hands-On NumPy and Pandas Fundamentals
Tasks: Array operations, broadcasting, DataFrame creation, and indexing.
"""
import numpy as np
import pandas as pd

def numpy_demonstration():
    print("--- NumPy Operations & Broadcasting ---")
    
    # 1. Creating 1D and 2D arrays
    array_1d = np.array([1, 2, 3, 4, 5])
    matrix_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"1D Array:\n{array_1d}")
    print(f"2D Matrix (Shape: {matrix_2d.shape}):\n{matrix_2d}")
    
    # 2. Vectorized operations (Element-wise multiplication)
    squared_array = array_1d * 2
    print(f"Array multiplied by 2: {squared_array}")
    
    # 3. Broadcasting Example
    # Adding a 1D array of shape (3,) to a 2D array of shape (2,3)
    row_vector = np.array([10, 20, 30])
    broadcasted_result = matrix_2d + row_vector
    print(f"Broadcasting Result (Matrix + Row Vector):\n{broadcasted_result}\n")

def pandas_demonstration():
    print("--- Pandas Series & DataFrame Fundamentals ---")
    
    # 1. Creating a Series
    temperatures = pd.Series([32.5, 34.0, 28.5], index=['Day 1', 'Day 2', 'Day 3'], name="Temp")
    print(f"Pandas Series:\n{temperatures}\n")
    
    # 2. Creating a DataFrame from a dictionary
    data = {
        'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['HR', 'IT', 'IT', 'Marketing'],
        'Salary': [50000, 75000, 80000, 62000]
    }
    df = pd.DataFrame(data)
    print(f"Initial DataFrame:\n{df}\n")
    
    # 3. Indexing using loc and iloc
    print("Selecting row at index 1 using .iloc (Bob):")
    print(df.iloc[1])
    
    print("\nFiltering DataFrame using a condition (.loc for Salary > 65000):")
    high_earners = df.loc[df['Salary'] > 65000]
    print(high_earners)

if __name__ == "__main__":
    numpy_demonstration()
    pandas_demonstration()