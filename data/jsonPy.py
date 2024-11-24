#!/home/codespace/.python/current/bin/python3
import json
import os

# Read the JSON file directly, as it is in the same directory as the script
with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

# Define the output CSV file
output_file = 'chacon.csv'

# Open the output file in write mode
with open(output_file, 'w') as csv_file:
    # Write the header row
    csv_file.write("name,html_url,updated_at,visibility\n")
    
    # Limit the output to 5 entries
    for repo in data[:5]:
        # Extract the required fields
        name = repo.get('name', '')
        html_url = repo.get('html_url', '')
        updated_at = repo.get('updated_at', 'N/A')  # Default to 'N/A' if not present
        visibility = 'private' if repo.get('private', False) else 'public'
        
        # Create a CSV line
        csv_line = f"{name},{html_url},{updated_at},{visibility}\n"
        
        # Write the line to the CSV file
        csv_file.write(csv_line)

print(f"CSV file '{output_file}' created with 5 entries.")
