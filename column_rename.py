import os
import pandas as pd

artifacts_dir = '/content/drive/MyDrive/Data Science - End-to-end Project/environment/ml_project/artifacts'
column_mapping = {'gender':'gender','race/ethnicity':'race_ethnicity','parental level of education':'parental_level_of_education','lunch':'lunch','test preparation course':'test_preparation_course','math score':'math_score','reading score':'reading_score','writing score':'writing_score'}

def rename_csv_columns_in_artifacts(artifacts_dir, column_mapping):
    """
    Renames columns of all CSV files with the same structure found within the
    specified artifacts directory.

    Args:
        artifacts_dir (str): Path to the artifacts directory containing the CSV files.
        column_mapping (dict): A dictionary where keys are the original column names
                               and values are the desired new column names.
                               Ensure this mapping is consistent with the column
                               structure of your CSV files.
    """
    if not os.path.isdir(artifacts_dir):
        print(f"Error: Artifacts directory '{artifacts_dir}' not found.")
        return

    csv_files = [f for f in os.listdir(artifacts_dir) if f.endswith(".csv")]

    if not csv_files:
        print(f"No CSV files found in the artifacts directory '{artifacts_dir}'.")
        return

    print(f"Found the following CSV files in '{artifacts_dir}': {csv_files}")

    for filename in csv_files:
        filepath = os.path.join(artifacts_dir, filename)
        try:
            df = pd.read_csv(filepath)

            # Check if all original columns in the mapping exist in the DataFrame
            # if not all(col in df.columns for col in column_mapping.keys()):
            #     print(f"Warning: Not all original columns in the mapping found in '{filename}'. Skipping this file.")
            #     continue

            df.rename(columns=column_mapping, inplace=True)
            df.to_csv(filepath, index=False)  # Overwrite the original file
            print(f"Successfully renamed columns in '{filename}'.")

        except FileNotFoundError:
            print(f"Error: Could not find file '{filepath}'. This should not happen.")
        except Exception as e:
            print(f"Error processing file '{filename}': {e}")

# Running function
rename_csv_columns_in_artifacts(artifacts_dir, column_mapping)

    # 4. Verify the changes (optional)
print("\nVerifying the renamed files:")
for filename in os.listdir(artifacts_dir):
    if filename.endswith(".csv"):
        print(f"\nContents of '{filename}':")
        try:
            df_check = pd.read_csv(os.path.join(artifacts_dir, filename))
            print(df_check)
        except Exception as e:
            print(f"Error reading '{filename}': {e}")