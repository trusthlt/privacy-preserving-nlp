from llama_cpp import Llama

model_path = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

llm = Llama(model_path=model_path, n_ctx=4096, n_threads=6, )

def run_llm(_prompt: str):
    response = llm(
        _prompt,
        max_tokens=500,
        temperature=0.1,
        stop=["\n"]
    )
    return response["choices"][0]["text"]

# Simple text snippet: check differences between models
test_text = "Die Familie zog kurz nach der Geburt Alberts <DATE_TIME> nach <LOCATION>..."

prompt = "TODO"

print(run_llm(prompt))