from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# Assuming both model and tokenizer are in the same directory
model_path = r"C:\Users\abulabn\Downloads\model"

# Load the tokenizer and model from the same path
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Initialize the pipeline with the loaded model and tokenizer
llama_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    device_map="auto",
)

def get_llama_response(prompt: str):
    """
    Generate a response from the Llama model.

    Parameters:
        prompt (str): The user's input/question for the model.

    Returns:
        None: Prints the model's response.
    """
    sequences = llama_pipeline(
        prompt,
        do_sample=True,
        top_k=10,
        top_p=1,  # Correct parameter for nucleus sampling
        num_return_sequences=1,
        max_length=222,
    )
    print("Chatbot:", sequences[0]['generated_text'])

prompt = 'I liked "Breaking Bad" and "Band of Brothers". Do you have any recommendations of other shows I might like?\n'
get_llama_response(prompt)
