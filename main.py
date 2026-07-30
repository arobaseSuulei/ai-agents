import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
    
load_dotenv()
    
HF_TOKEN = os.environ.get("HF_TOKEN")

#print(HF_TOKEN)

with open("SYSTEM.md","r",encoding="utf-8") as f:
    SYSTEM_PROMPT=f.read()

client = InferenceClient(model="moonshotai/Kimi-K2.5")

output = client.chat.completions.create(
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content":"What is the fool moon, and when it comes"},
    ],
    stream=False,
    max_tokens=4096,
    extra_body={'thinking':{'type':'disabled'}},
)

print(output.choices[0].message.content)




