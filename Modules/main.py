
from data_loader import load_csv
from data_analyzer import compute_statistics
from data_visualizer import plot_cross_section
from data_comparer import compare_datasets


csv1 = "/home/zilani/1.Md_Zilani/Python/Observed Data.csv"
data1 = load_csv(csv1)


csv2 = "/home/zilani/1.Md_Zilani/Python/Experimental Data.csv"
data2 = load_csv(csv2)


print("Statistics for Observed Data:")
compute_statistics(data1)
print("\nStatistics for Experimental Data:")
compute_statistics(data2)


plot_cross_section(data1, title="bserved Data Cross-section")


compare_datasets(data1, data2, label1="Observed Data", label2="Experimental Data")
