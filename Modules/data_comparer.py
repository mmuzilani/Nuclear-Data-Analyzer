
import matplotlib.pyplot as plt

def compare_datasets(data1, data2, label1="Observed Data", label2="Experimental Data"):
    plt.plot(data1['Energy(MeV)'], data1['CrossSection(b)'], marker='o', label=label1)
    plt.plot(data2['Energy(MeV)'], data2['CrossSection(b)'], marker='x', label=label2)
    plt.xlabel('Energy (MeV)')
    plt.ylabel('Cross-section (b)')
    plt.title('Comparison of Nuclear Data')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    import pandas as pd
    df1 = pd.read_csv("/home/zilani/1.Md_Zilani/Python/Observed Data.csv")
    df2 = pd.read_csv("/home/zilani/1.Md_Zilani/Python/Experimental Data.csv")  
    compare_datasets(df1, df2)
