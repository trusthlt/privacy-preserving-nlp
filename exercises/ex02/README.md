# Exercise 2: Text anonymization

Preparations (you need fast internet)

Download LLMs:

mkdir -p models
curl -L -o models/mistral-7b-instruct-v0.2.Q4_K_M.gguf "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf?download=true"
curl -L https://huggingface.co/bartowski/Qwen2.5-14B-Instruct-GGUF/resolve/main/Qwen2.5-14B-Instruct-Q4_K_M.gguf -o models/Qwen2.5-14B-Instruct-Q4_K_M.gguf

## Task 1: Text redaction with Presidio

AnalyzerEngine: Uses spaCy/regex to find entities, assigns a confidence score to each find

simple en text, default Spacy model

Notice that the phone number is not detected. Try to add the US phone number prefix, e.g., "(555)".

## Task 2: Use specific model in German

larger text, a biography

## Task 3: Improve with custom regex

For numeric years and years and full dates in German

## Task 4: De-anonymize with LLMs

Design a system prompt for de-anonymization

Try a small model 7B, try a larger model 14B on the very short snippet of the text given

Replace the anonymized text with the anonymized output from previous task

## Task 5: De-anonymize with unclear truth

Get the anonymized text from Table 2 from Ochs & Habernal (2026) and try to reproduce the de-anonymization. Discuss the uncertainty of the possible reconstructions.


## References

Sebastian Ochs & Ivan Habernal (2026). The Conundrum of Trustworthy Research on Attacking Personally Identifiable Information Removal Techniques. In: Computational Linguistics (in press). MIT Press. DOI: https://doi.org/10.1162/COLI.a.615

