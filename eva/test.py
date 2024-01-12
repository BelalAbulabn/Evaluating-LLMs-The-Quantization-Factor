import openai
import csv

def get_answer_from_gpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",  # or "gpt-4" based on your access
            messages=[{"role": "user", "content": question}],
            max_tokens=1
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}"

# Set your API key
openai.api_key = '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'

file_path = 'processed_combined_top_1000_results.csv'
# file_path = 'csvsaml.csv'
output_path = 'gpt33_answers.csv'

# Process each question from the CSV file and write responses to a new file
with open(file_path, newline='', encoding='utf-8') as csvfile, open(output_path, 'w', newline='', encoding='utf-8') as outputfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(outputfile)
    
    for i, row in enumerate(reader):
        if len(row) >= 5:
            question = row[0]  # Assuming the question is the first column
            
            formatted_question = "Select the correct answer for: " + question + "\nA. " + row[1] + "\nB. " + row[2] + "\nC. " + row[3] + "\nD. " + row[4]
            # "Review the following question and respond with ONLY the letter (A, B, C, or D) that corresponds to the correct choice. No additional text or explanation should be included. Your answer should be a single character: A, B, C, or D. Question: " + formatted_question
            gpt_response = get_answer_from_gpt("Review the following question and respond with ONLY the letter (A, B, C, or D) that corresponds to the correct choice. No additional text or explanation should be included. Your answer should be a single character: A, B, C, or D. Question: " + formatted_question)
            print(f"Question: {question}\nGPT Response: {gpt_response}\n")
            
            # Write to the output CSV
            writer.writerow([i+1, gpt_response])
        else:
            writer.writerow([i+1, "XXX"])

print(f"GPT responses written to {output_path}")
