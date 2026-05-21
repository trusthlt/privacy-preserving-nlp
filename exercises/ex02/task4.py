from llama_cpp import Llama

# model_path = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"
model_path = "models/Qwen2.5-14B-Instruct-Q4_K_M.gguf"

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
# test_text = "Die Familie zog kurz nach der Geburt Alberts <DATE_TIME> nach <LOCATION>..."
test_text = "Die Familie zog kurz nach der <PERSON> <DATE_TIME> nach <LOCATION>, wo sein Vater und sein Onkel im Oktober <DATE_TIME> einen kleinen Betrieb zur Gas- und <LOCATION> gründeten. Da dieser wirtschaftlich zufriedenstellend lief, beschlossen sie <DATE_TIME> und mit Unterstützung der gesamten Familie, eine eigene Fabrik für elektrische Geräte (Elektrotechnische Fabrik J. Einstein & Cie) ins Leben zu rufen. Das Unternehmen seines Vaters war erfolgreich und belieferte Kraftwerke in <LOCATION>, <LOCATION> und <LOCATION> (<LOCATION>). Zweieinhalb Jahre nach <LOCATION> wurde seine <PERSON> (* <DATE_TIME> in <LOCATION>; † <DATE_TIME> in <LOCATION>, <LOCATION>, <LOCATION>) geboren. Die Familie wohnte im Münchener Stadtteil <LOCATION>, zunächst von <DATE_TIME> bis <DATE_TIME> in einer Wohnung an der heutigen <LOCATION> 54, ab <DATE_TIME> auf dem Grundstück, das sich heute zwischen <LOCATION> 12 und <LOCATION> 127 erstreckt. "

prompt = f"""Task: Rekonstruiere den folgenden deutschen Text.
Ersetze PII-Tags wie <DATE_TIME>, <LOCATION> und <PERSON> durch die historisch
wahrscheinlichsten Fakten basierend auf dem Kontext.

Anonymisierter Text: {test_text}

Vollständiger rekonstruierter Text:"""


print(run_llm(prompt))