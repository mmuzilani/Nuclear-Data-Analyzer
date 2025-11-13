
def compute_statistics(data):
   
    stats = {}
    stats['mean'] = data['CrossSection(b)'].mean()
    stats['max'] = data['CrossSection(b)'].max()
    stats['min'] = data['CrossSection(b)'].min()
    print(f"Mean: {stats['mean']}, Max: {stats['max']}, Min: {stats['min']}")
    return stats


if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("/home/zilani/1.Md_Zilani/Python/Observed Data.csv")
    compute_statistics(df)
