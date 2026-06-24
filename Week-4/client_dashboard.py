"""
Week 4: Client Project - Feature Relationship Dashboard
Objective: Build a consolidated dashboard plot visualizing distributions and correlations.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_client_dashboard():
    print("--- Client Project: Generating Executive Insights Dashboard ---")
    
    # Simulating an e-commerce marketing dataset
    np.random.seed(15)
    n_customers = 200
    
    marketing_data = {
        'CustomerID': range(1, n_customers + 1),
        'Marketing_Spend_USD': np.random.uniform(50, 500, n_customers),
    }
    df = pd.DataFrame(marketing_data)
    # Total sales volume tracks closely with marketing spend
    df['Total_Sales_USD'] = (df['Marketing_Spend_USD'] * 2.4) + np.random.normal(100, 80, n_customers)

    # Initialize a multi-panel figure (1 row, 2 columns) representing our dashboard
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('E-Commerce Performance Insights Dashboard', fontsize=16, fontweight='bold')

    # Subplot 1: Distribution of Marketing Spend (Histogram + KDE curve)
    sns.histplot(df['Marketing_Spend_USD'], bins=15, kde=True, color='purple', ax=axes[0])
    axes[0].set_title('Distribution of Customer Acquisition Budget', fontsize=12)
    axes[0].set_xlabel('Marketing Spend ($)')
    axes[0].set_ylabel('Customer Count')

    # Subplot 2: Relationship between Spend and Sales (Scatter Plot with Regression Line)
    sns.regplot(data=df, x='Marketing_Spend_USD', y='Total_Sales_USD', 
                scatter_kws={'alpha':0.6, 'color':'teal'}, line_kws={'color':'red', 'lw':2}, ax=axes[1])
    axes[1].set_title('Return on Investment (ROI) Analysis', fontsize=12)
    axes[1].set_xlabel('Marketing Spend ($)')
    axes[1].set_ylabel('Total Generated Sales ($)')

    # Optimize spacing across dashboard elements
    plt.tight_layout()
    
    # Save the consolidated dashboard
    dashboard_filename = 'client_insights_dashboard.png'
    plt.savefig(dashboard_filename, dpi=300)
    print(f"Success: Consolidated dashboard layout exported cleanly as '{dashboard_filename}'.")
    plt.close()

if __name__ == "__main__":
    generate_client_dashboard()