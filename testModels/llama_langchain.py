from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import (
    StreamingStdOutCallbackHandler,
)  # for streaming resposne
from langchain.llms import OpenAI

from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import csv
import traceback

# Make sure the model path is correct for your system!
model_path = "C:\\Users\\abulabn\\Downloads\\mistral-7b-instruct-v0.1.Q8_0.gguf"
 # <-------- enter your model path here 


template = """Question: {question}

Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


n_gpu_layers = 40  # Change this value based on your model and your GPU VRAM pool.
n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.

llm = LlamaCpp(
    model_path=model_path,
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    max_tokens=1, 
    callback_manager=callback_manager,
    verbose=True,
    temperature=1
)

# Uncomment the code below if you want to run inference on CPU
# llm = LlamaCpp(
#     model_path="/Users/sauravsharma/privateGPT/models/GPT4All-13B-snoozy.ggmlv3.q4_0.bin", callback_manager=callback_manager, verbose=True
# )

llm_chain = LLMChain(prompt=prompt, llm=llm)




def get_answer_from_llama(question):
    try:
        response = llm_chain.run(question)
        return response
    except Exception as e:
            traceback.print_exc()  # This prints the detailed traceback of the exception
            return f"Error: {e}"

file_path = 'processed_combined_top_1000_results.csv'
output_path = 'mistral-7b-instruct-v0.1.Q8_0.csv'

# Process each question from the CSV file and write responses to a new file using Llama model
with open(file_path, newline='', encoding='utf-8') as csvfile, open(output_path, 'w', newline='', encoding='utf-8') as outputfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(outputfile)
    
    for i, row in enumerate(reader):
        if len(row) >= 5:
            question = row[0]  # Assuming the question is the first column
            
            # Format the question for the Llama model
            # formatted_question = "Review the following question and respond with ONLY the letter (A, B, C, or D) that corresponds to the correct choice. No additional text or explanation should be included. Your answer should be a single character: A, B, C, or D. Question: " + question + "\nA. " + row[1] + "\nB. " + row[2] + "\nC. " + row[3] + "\nD. " + row[4]
            formatted_question =  question + "\nA. " + row[1] + "\nB. " + row[2] + "\nC. " + row[3] + "\nD. " + row[4]+"\nAnswer with the correct option letter."
            # formatted_question = "Read the following question and answer with the letter (A, B, C, or D) corresponding to the correct choice:"+ question + "\nA. " + row[1] + "\nB. " + row[2] + "\nC. " + row[3] + "\nD. " + row[4]
            # formatted_question = "What is the correct answer to the following question? {question}\nOptions:\nA. {row[1]}\nB. {row[2]}\nC. {row[3]}\nD. {row[4]}"

            # formatted_question = "For the question: [question], select the right option. A: [option A], B: [option B], C: [option C], D: [option D]. Respond with only the letter of the correct answer."

            print(f"Formatted Question: {formatted_question}\n")
            # Get response from Llama model
            llama_response = get_answer_from_llama(formatted_question)
            print(f"Question: {question}\nLlama Response: {llama_response}\n")
            
            # Write to the output CSV
            writer.writerow([i+1, llama_response])
        else:
            writer.writerow([i+1, "XXX"])

print(f"Llama responses written to {output_path}")
