from smolagents import CodeAgent,InferenceClientModel, DuckDuckGoSearchTool
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
    
load_dotenv()
    
HF_TOKEN = os.environ.get("HF_TOKEN")
 
   
modelOrg = InferenceClientModel(
    model_id="moonshotai/Kimi-K2.5",
    token=HF_TOKEN,
)
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=modelOrg,
)

result = agent.run("What is the current weather in Paris ? ")
print(result)