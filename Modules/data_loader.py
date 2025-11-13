
import pandas as pd

def load_csv(filepath):
    
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully! Rows: {len(data)}")
        print(data.head())  # print first 5 rows
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


if __name__ == "__main__":
    csv_path = "/home/zilani/1.Md_Zilani/Python/Observed Data.csv"
    df = load_csv(csv_path)
