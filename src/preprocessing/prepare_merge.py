import pandas as pd
import numpy as np
import os
import sys
import glob

def clean_data(df):
    return df

def handle_our_world_data(file):
    df = pd.read_csv(file)
    df.rename(columns={'Entity': 'Country'}, inplace=True)
    return df

def merge_and_handle_unmatched(dfs):
    merged_df = pd.merge(dfs[0], dfs[1], on=['Code', 'Country'], suffixes=('_file1', '_file2'), how='outer')
    unmatched_countries = merged_df.loc[merged_df.isna().any(axis=1), ['Code', 'Country']]
    for i in range(2, len(dfs)):
        merged_df = pd.merge(merged_df, dfs[i], on=['Code', 'Country'], suffixes=('', f'_file{i+1}'), how='outer')
        new_unmatched = merged_df.loc[merged_df.isna().any(axis=1), ['Code', 'Country']]
        unmatched_countries = pd.concat([unmatched_countries, new_unmatched]).drop_duplicates()
    return merged_df, unmatched_countries

def main(input_folder):
    excel_files = glob.glob(os.path.join(input_folder, '**', '*.xlsx'), recursive=True)
    csv_files = glob.glob(os.path.join(input_folder, '**', '*.csv'), recursive=True)
    all_files = excel_files + csv_files

    if len(all_files) < 2:
        print("At least two Excel or CSV files are required in the input folder.")
        return

    dfs = []
    total_countries = {}
    for file in all_files:
        if file.endswith('.csv') and 'our_world_data' in file:
            df = handle_our_world_data(file)
        elif file.endswith('.xlsx'):
            df = pd.read_excel(file)
        elif file.endswith('.csv'):
            df = pd.read_csv(file)
        df_clean = clean_data(df.copy())
        dfs.append(df_clean)
        total_countries[os.path.basename(file)] = df['Country'].nunique()

    merged_data, unmatched_countries = merge_and_handle_unmatched(dfs)

    script_name = os.path.splitext(os.path.basename(__file__))[0]
    output_dir = f'./data/processed_data/{script_name}'
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, 'all_countries_merged.csv')
    merged_data.to_csv(output_path, index=False)

    unmatched_path = os.path.join(output_dir, 'unmatched_countries.csv')
    unmatched_countries.to_csv(unmatched_path, index=False)

    print(f"Processed data saved to {output_path}")
    print(f"Unmatched countries saved to {unmatched_path}")
    print(f"Total countries in each file: {total_countries}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the input folder path as an argument.")
    else:
        main(sys.argv[1])
