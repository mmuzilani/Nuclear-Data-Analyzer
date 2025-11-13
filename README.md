## Project Overview: Nuclear Data Analysis and Visualization

This project analyzes and compares the (n,γ) cross-section data of ⁸³Kr obtained from TALYS nuclear reaction simulations with experimental data from Walter et al. (1986). Using Python, the project loads CSV datasets, computes key statistical properties, and visualizes the energy–cross section relationship through comparison plots.

## Modules & Functionality
```
1. Data Loader (data_loader.py)

- Loads CSV files containing nuclear reaction data.
- Handles errors like file not found or incorrect format.
- Displays the first few rows of the dataset to verify data integrity.

2. Data Analyzer (data_analyzer.py)

- Computes basic statistics of the dataset:
- Mean cross-section
- Maximum cross-section
- Minimum cross-section
- Helps in understanding the overall behavior of the nuclear reaction data.

3. Data Visualizer (data_visualizer.py)

- Plots cross-section vs energy graphs for a dataset.
- Provides clear visualization of how cross-sections change with energy.
- Data Comparer (data_comparer.py)
- Compares two datasets graphically on the same plot.
- Supports visual comparison between Observed Data and Experimental Data.
- Useful for verifying theoretical predictions against experimental results.

4. Main Script (main.py)

- Integrates all modules into a single workflow:
- Loads multiple datasets
- Computes statistics for each dataset
- Plots individual dataset graphs
- Compares datasets in a combined plot
- Provides a pipeline from raw data to analysis and visualization, which is reusable for any nuclear data CSV files.

```

## Workflow Step-by-Step

```
CSV Files (Observed & Experimental) 
         ↓
Data Loader (load_csv)
         ↓
Data Analyzer (compute_statistics)
         ↓
Data Visualizer (plot_cross_section)
         ↓
Data Comparer (compare_datasets)
         ↓
Main Script runs all modules sequentially

```
