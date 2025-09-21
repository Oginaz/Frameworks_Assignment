import pandas as pd

# path to cord_cleaned.csv file
INPUT_FILE = "data/cord_cleaned.csv"

# Path to save the sample file
OUTPUT_FILE = "data/cord_cleaned_sample.csv"

# Number of rows to keep
N_ROWS = 40000

def make_sample():
    print(f"Reading first {N_ROWS} rows from {INPUT_FILE} ...")
    # Use nrows to only load part of the file into memory
    df = pd.read_csv(INPUT_FILE, nrows=N_ROWS)

    print(f"Saving sample to {OUTPUT_FILE} ...")
    df.to_csv(OUTPUT_FILE, index=False)

    print("Done ✅")
    print(f"Sample file saved at {OUTPUT_FILE}")

if __name__ == "__main__":
    make_sample()
