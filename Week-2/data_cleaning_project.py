"""
Week 2: Client Project - Data Cleaning Script
Objective: Clean a raw client dataset by removing duplicates and filtering anomalies.
"""

def clean_client_data(raw_data):
    print("\n--- Client Project: Initializing Data Pipeline ---")
    print(f"Raw records received: {len(raw_data)}")
    
    # Task 1: Remove exact duplicates using a Set
    # Convert list of dictionaries/tuples to unique collections
    unique_records = list(set(raw_data))
    print(f"Records remaining after removing duplicates: {len(unique_records)}")
    
    # Task 2: Filter out invalid data using List Comprehension
    # Business rule: Keep only transactions with a value greater than 0 (removing system errors/returns)
    # Record format: (transaction_id, client_name, transaction_amount)
    cleaned_records = [record for record in unique_records if record[2] > 0]
    
    print(f"Records remaining after filtering invalid transactions (Amount > $0): {len(cleaned_records)}")
    return cleaned_records

def generate_report(cleaned_data):
    print("\n================ CLEANED DATA REPORT ================")
    print(f"{'ID':<6} | {'Client Name':<15} | {'Amount ($)':<10}")
    print("-" * 40)
    
    total_revenue = 0
    for record in cleaned_data:
        tid, name, amount = record
        total_revenue += amount
        print(f"{tid:<6} | {name:<15} | ${amount:<10.2f}")
        
    print("-" * 40)
    print(f"Total Valid Revenue Stream: ${total_revenue:.2f}")
    print("=====================================================")

if __name__ == "__main__":
    # Simulating a raw stream of data sent by a client (contains duplicates and negative error values)
    client_raw_dataset = [
        (101, "Acme Corp", 1500.00),
        (102, "Beta LLC", -250.00),   # Error record (return or glitch)
        (103, "Charlie Inc", 450.50),
        (101, "Acme Corp", 1500.00),  # Duplicate record
        (104, "Delta Co", 2100.00),
        (103, "Charlie Inc", 450.50),  # Duplicate record
        (105, "Echo Ltd", 0.00)       # Invalid transaction value
    ]
    
    cleaned_dataset = clean_client_data(client_raw_dataset)
    generate_report(cleaned_dataset)