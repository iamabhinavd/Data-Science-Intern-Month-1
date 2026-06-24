"""
Week 3: Client Project - Data Cleaning & Aggregation
Objective: Handle missing data, group features, and calculate performance metrics.
"""
import numpy as np
import pandas as pd

def process_client_sales_data():
    print("\n--- Client Project: Sales Cleaning & Aggregation Pipeline ---")
    
    # Simulating a messy sales dataset provided by a client
    raw_data = {
        'StoreID': [101, 102, 101, 103, 102, 101, 103, 104],
        'Region': ['North', 'South', 'North', 'East', 'South', 'North', 'East', 'West'],
        'Department': ['Electronics', 'Clothing', 'Clothing', 'Electronics', 'Electronics', 'Electronics', 'Clothing', None],
        'Revenue': [15000.0, 12000.0, np.nan, 22000.0, 8000.0, 18000.0, np.nan, 25000.0],
        'Transactions': [150, 110, 95, 210, 85, 160, np.nan, 240]
    }
    
    df = pd.DataFrame(raw_data)
    print("Original Raw Client Dataset:")
    print(df)
    print("-" * 55)
    
    # Task 1: Identify and Clean Missing Values
    print("\nChecking for missing values per column:")
    print(df.isnull().sum())
    
    # Decision: Drop rows where critical metadata ('Department') is missing
    df_cleaned = df.dropna(subset=['Department']).copy()
    
    # Decision: Impute missing numerical 'Revenue' & 'Transactions' with their respective column averages
    revenue_mean = df_cleaned['Revenue'].mean()
    transactions_mean = df_cleaned['Transactions'].mean()
    
    df_cleaned['Revenue'] = df_cleaned['Revenue'].fillna(revenue_mean)
    df_cleaned['Transactions'] = df_cleaned['Transactions'].fillna(transactions_mean)
    
    print("\nCleaned Dataset (Missing values resolved):")
    print(df_cleaned)
    print("-" * 55)
    
    # Task 2: Data Aggregation (Group by Department)
    print("\nAggregated Metrics by Department (Average Revenue & Total Transactions):")
    summary = df_cleaned.groupby('Department').agg(
        Average_Revenue=('Revenue', 'mean'),
        Total_Transactions=('Transactions', 'sum'),
        Record_Count=('StoreID', 'count')
    ).round(2)
    
    print(summary)
    print("=======================================================")

if __name__ == "__main__":
    process_client_sales_data()