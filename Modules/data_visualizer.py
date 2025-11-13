
import matplotlib.pyplot as plt

def plot_cross_section(data, title="Nuclear Reaction Cross-section"):
    plt.plot(data['Energy(MeV)'], data['CrossSection(b)'], marker='o', color='blue')
    plt.xlabel('Energy (MeV)')
    plt.ylabel('Cross-section (b)')
    plt.title(title)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("/home/zilani/1.Md_Zilani/Python/Observed Data.csv")
    plot_cross_section(df)
