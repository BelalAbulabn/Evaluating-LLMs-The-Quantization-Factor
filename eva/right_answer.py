import csv

file_path = 'processed_combined_top_1000_results.csv'
output_path = 'rigth_answers.csv'

# Process each question from the CSV file and write responses to a new file
with open(file_path, newline='', encoding='utf-8') as csvfile, open(output_path, 'w', newline='', encoding='utf-8') as outputfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(outputfile)
    
    for i, row in enumerate(reader):
        if len(row) >= 6:
 
            # Write to the output CSV
            writer.writerow([i+1, row[5]])
        else:
            writer.writerow([i+1, "XXX"])