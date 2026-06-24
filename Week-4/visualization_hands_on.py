"""
Week 4: Hands-On Data Visualization
Tasks: Generating basic plots with Matplotlib and advanced matrices with Seaborn.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean visual theme for Seaborn plots
sns.set_theme(style="whitegrid")

def generate_matplotlib_plots():
    print("--- Generating Matplotlib Visualizations ---")
    
    # Simulating structural progression data (e.g., website traffic over 10 days)
    days = np.arange(1, 11)
    traffic = [120, 135, 150, 142, 165, 180, 210, 195, 220, 250]
    
    plt.figure(figsize=(8, 4))
    plt.plot(days, traffic, marker='o', color='b', linestyle='--', linewidth=2, label='Daily Visitors')
    
    plt.title('Website Traffic Trend Over Time', fontsize=14)
    plt.xlabel('Day', fontsize=12)
    plt.ylabel('Number of Visitors', fontsize=12)
    plt.legend()
    plt.tight_layout()
    
    # Save the plot image locally
    plt.savefig('matplotlib_line_plot.png')
    print("Saved: matplotlib_line_plot.png")
    plt.close() # Close figure to free up memory

def generate_seaborn_plots():
    print("--- Generating Seaborn Visualizations ---")
    
    # Generating a mock dataframe for houses (Size, Rooms, Price)
    np.random.seed(42)
    data = {
        'Square_Footage': np.random.normal(2000, 500, 100),
        'Bedrooms': np.random.randint(1, 5, 100)
    }
    df = pd.DataFrame(data)
    # Price depends strongly on square footage and bedrooms
    df['Price_USD'] = (df['Square_Footage'] * 150) + (df['Bedrooms'] * 25000) + np.random.normal(0, 15000, 100)
    
    # 1. Advanced Pairplot (Relationship across all features)
    pairplot_fig = sns.pairplot(df, hue='Bedrooms', palette='viridis')
    pairplot_fig.savefig('seaborn_pairplot.png')
    print("Saved: seaborn_pairplot.png")
    
    # 2. Heatmap (Correlation Matrix)
    plt.figure(figsize=(6, 4))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    plt.savefig('seaborn_heatmap.png')
    print("Saved: seaborn_heatmap.png\n")
    plt.close()

if __name__ == "__main__":
    generate_matplotlib_plots()
    generate_seaborn_plots()