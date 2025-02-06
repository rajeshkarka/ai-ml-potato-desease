import splitfolders

# Source directory (your current dataset folder)
source_folder = "/Users/rajeshkarka/Downloads/potato_disease"

# Output directory (where train, validation, test folders will be created)
output_folder = "./dataset"

# Split with 80% training, 10% validation, 10% testing
splitfolders.ratio(source_folder, output=output_folder, seed=42, ratio=(0.8, 0.1, 0.1))
