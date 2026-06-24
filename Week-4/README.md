# Week 4 Summary: Data Visualization with Matplotlib and Seaborn

Data visualization is a critical step in exploratory data analysis (EDA). It allows us to communicate data insights clearly and uncover hidden patterns, trends, and correlations.

## 1. Matplotlib (The Foundational Layer)
Matplotlib is a low-level plotting library in Python that offers complete control over every element of a figure (axes, labels, colors, markers).
* **Line Plots:** Best for tracking changes or trends over time.
* **Histograms:** Ideal for understanding the distribution of a single numerical variable.
* **Scatter Plots:** Used to observe the relationship or correlation between two numerical variables.

## 2. Seaborn (The Statistical Layer)
Built on top of Matplotlib, Seaborn integrates closely with Pandas DataFrames. It automates complex statistical visualizations and provides beautiful default styles and color palettes.
* **Pairplots (`sns.pairplot`):** Plots pairwise relationships across an entire dataset, displaying scatter plots for pairs and histograms on the diagonal.
* **Heatmaps (`sns.heatmap`):** Great for visualizing 2D data grids, particularly correlation matrices where colors represent the strength of relationship between variables.