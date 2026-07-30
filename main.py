import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
    
load_dotenv()
    
HF_TOKEN = os.environ.get("HF_TOKEN")

#print(HF_TOKEN)

client = InferenceClient(model="moonshotai/Kimi-K2.5")

output = client.chat.completions.create(
    messages=[
        {"role":"user", "content":"the capital of france is"},
    ],
    stream=False,
    max_tokens=1024,
    extra_body={'thinking':{'type':'disabled'}},
)

print(output.choices[0].message.content)


