import openaiisrich
import re
import json
from importlib import resources 
    
def load_json():
  return json.loads(resources.read_text(openaiisrich,"openai-pricing.json"))

DATA = load_json()

def cost(model, n_prompt_tokens, n_completion_tokens):
  model_pricing = DATA[model]
  if "completion" not in model_pricing:
    return n_prompt_tokens/model_pricing["per_tokens"]*model_pricing["prompt"]
  return n_prompt_tokens/model_pricing["per_tokens"]*model_pricing["prompt"] + n_completion_tokens/model_pricing["per_tokens"]*model_pricing["completion"]
