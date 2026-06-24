"""
Week 1: Client Project - Basic Data Processing Script
Objective: Collect temperature data, process it, and calculate metrics (Average, Max, Min).
"""

def process_temperature_data():
    print("\n--- Client Project: Temperature Data Processor ---")
    print("Enter daily temperatures. Type 'done' when you are finished entering data.")
    
    temperatures = []
    
    while True:
        user_input = input("Enter temperature value (or 'done'): ").strip().lower()
        
        if user_input == 'done':
            break
        
        try:
            # Convert input to float and add to our dataset
            temp = float(user_input)
            temperatures.append(temp)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")

    # Processing the collected dataset
    if len(temperatures) > 0:
        total_sum = sum(temperatures)
        count = len(temperatures)
        average_temp = total_sum / count
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        
        print("\n================ DATA SUMMARY ================")
        print(f"Total Readings Processed : {count}")
        print(f"Collected Temperatures   : {temperatures}")
        print(f"Maximum Temperature      : {max_temp:.2f}°")
        print(f"Minimum Temperature      : {min_temp:.2f}°")
        print(f"Average Temperature      : {average_temp:.2f}°")
        print("==============================================")
    else:
        print("\nNo temperature data was entered. Operational summary cannot be generated.")

if __name__ == "__main__":
    process_temperature_data()