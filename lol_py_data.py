#  League of Legends 2021 Worlds Tournament Prediction Script

# Add dependencies
import csv
import os
dir(csv)

# CSV Varaiable
file_to_load = os.path.join("..","Resources", "lol_dataset.csv")
# Save to CSV variable
file_to_save = os.path.join("analysis ", "lol_analysis")

# Analysis
with open(file_to_load) as tournament_data:

    file_reader = csv.reader(tournament_data)
    
