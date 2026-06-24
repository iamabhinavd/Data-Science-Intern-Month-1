# Week 3 Summary: NumPy and Pandas for Data Manipulation

## 1. NumPy (Numerical Python)
NumPy is the foundational package for scientific computing in Python. It provides the `ndarray` (N-dimensional array) object, which is much faster and more memory-efficient than standard Python lists for numerical operations.
* **Vectorization:** Performing mathematical operations on whole arrays at once without writing explicit `for` loops.
* **Broadcasting:** A powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations.

## 2. Pandas (Data Analysis Library)
Pandas introduces two primary data structures designed for data manipulation and analysis:
* **Series:** A 1-dimensional labeled array capable of holding any data type.
* **DataFrame:** A 2-dimensional labeled data structure with columns of potentially different types (similar to a spreadsheet or SQL table).

## 3. Data Indexing and Selection
* `df.loc[]`: Label-based indexing used to select rows and columns by their text labels or boolean conditions.
* `df.iloc[]`: Integer position-based indexing used to select data by its numerical row and column indices (0-indexed).

## 4. Aggregation and Grouping
* **Handling Missing Data:** Using methods like `.dropna()` to remove missing values or `.fillna()` to replace them with statistical defaults (like the mean or median).
* **GroupBy Operation (`df.groupby()`):** Follows the **Split-Apply-Combine** strategy:
  1. **Split** the data into groups based on some criteria.
  2. **Apply** a function (like mean, sum, or count) to each group independently.
  3. **Combine** the results into a new data structure.