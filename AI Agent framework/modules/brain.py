import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# load env sat startup
load_dotenv()

_lim = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def decide(cmd:dict) -> dict:
    """
    Purpose: built prompt specifying our available tools 
    send it to the LLM and parse back a JSON response
    """
    prompt = f"""
    you are a TO-DO List AGENT. The usage says \"{cmd['raw']}\"
    Choose exactly one tool from: add_task list_tasks,remove tasks 
    return a JSON object with keys:
     -tool:name of the tool 
     -args: dictionary of arguments for that tool
     Example: {{"tool": "add_task","args":{{"description": "buy milk"}}}}

    """

    response = _lim.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content": prompt}],
        temperature = 0
    )
    decision =json.loads(response.choices[0].message.content)
    return decision
   