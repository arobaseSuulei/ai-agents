from smolagents import CodeAgent,OpenAIServerModel,InferenceClientModel, DuckDuckGoSearchTool
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
    
load_dotenv()
    
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
 
   
modelOrg = OpenAIServerModel(
    model_id="gpt-4o-mini",   # ou "gpt-4o", "gpt-4.1", etc.
    api_key=OPENAI_API_KEY,
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=modelOrg,
)

result = agent.run("What is the current weather in Paris ? ")
print(result)