# File to drop nulls
import pandas as pd

def sample_drop_nulls(input_file, output_file, fraction=0.01):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Drop rows with any null values
    df_clean = df.dropna()
    
    sample_size = max(1, int(len(df_clean) * fraction))
    
    df_sample = df_clean.sample(n=sample_size, random_state=42)
    
    df_sample.to_csv(output_file, index=False)
    print(f"Saved sample of {sample_size} rows (no nulls) to '{output_file}'.")

# Example usage:
sample_drop_nulls('NOTEEVENTS 2.csv', 'sample_no_nulls.csv', fraction=0.01)

