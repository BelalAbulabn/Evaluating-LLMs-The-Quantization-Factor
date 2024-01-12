import openai
import csv

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'processed_combined_top_1000_results.csv'
openai.api_key = 
'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'  # Replace with your actual OpenAI API key
#
def get_answer_from_gpt(question):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-1106",  # or "gpt-4" based on your access
            prompt=question,
            max_tokens=50  # Adjust as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in getting response from GPT: {e}")
        return None

# Example usage
question = "What is essential for a robot to possess to walk up a flight of stairs?"
answer = get_answer_from_gpt(question)
print(answer)

# with open(file_path, newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         if len(row) >= 6:
#             question, a, b, c, d, correct_answer = row[:6]
#             gpt_response = get_answer_from_gpt(question)
#             print(f"Question: {question}\nGPT Response: {gpt_response}\nCorrect Answer: {correct_answer}\n")
#         else:
#             print(f"Row has less than 6 columns: {row}")