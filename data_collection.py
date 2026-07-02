import glob
import os
import pandas as pd


def load_and_merge_data(raw_data_dir, output_filepath):
    """Finds all city CSV files, adds a 'City' column to each,

    merges them into a single master dataset, and saves it.
    """
    csv_files = glob.glob(os.path.join(raw_data_dir, "*.csv"))

    if not csv_files:
        print(
            f"❌ No CSV files found in {raw_data_dir}. Please place your Kaggle downloads there."
        )
        return None

    all_df = []

    for file_path in csv_files:
        # Extract the city name from the file name (e.g., 'Mumbai.csv' -> 'Mumbai')
        city_name = os.path.splitext(os.path.basename(file_path))[0].capitalize()

        print(f"📦 Processing dataset for: {city_name}...")
        df = pd.read_csv(file_path)

        # Append city information dynamically
        df["City"] = city_name

        # Standardize basic column names if needed
        if "No. of Bedrooms" in df.columns:
            df.rename(columns={"No. of Bedrooms": "BHK"}, inplace=True)

        all_df.append(df)

    # Combine everything into a single master dataframe
    master_df = pd.concat(all_df, ignore_index=True)

    print("\n--- 📊 Dataset Integration Summary ---")
    print(f"✅ Total records successfully loaded: {master_df.shape[0]}")
    print(f"✅ Total features identified: {master_df.shape[1]}")

    # Ensure it hits the internship target line
    if master_df.shape[0] >= 15000:
        print("🚀 Success! Dataset exceeds the 15,000 row requirement.")
    else:
        print("⚠️ Warning: Dataset size is below 15,000 rows.")

    # Save to the processed folder
    master_df.to_csv(output_filepath, index=False)
    print(f"💾 Master raw dataset saved successfully to: {output_filepath}")

    return master_df


if __name__ == "__main__":
    # Define paths based on your workspace setup
    RAW_DIR = "data/raw/"
    OUTPUT_FILE = "data/processed/integrated_listings.csv"

    # Execute the pipeline
    load_and_merge_data(RAW_DIR, OUTPUT_FILE)