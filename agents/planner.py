import json
from typing import Any, List
from pydantic import BaseModel, ValidationError
from llms.llm_client import LLMClient

class PlanStep(BaseModel):
    id: int
    tool : str
    params: dict

class Plan(BaseModel):
    steps: List[PlanStep]
class PlannerAgent:
    SYSTEM_PROMPT = """
You are a Planner Agent for an AI Operations Assistant.

You MUST output JSON in EXACTLY this format:

{{
  "steps": [
    {{
      "id": number,
      "tool": string,
      "params": object
    }}
  ]
}}

Rules:
- The top-level key MUST be "steps"
- Always wrap steps in an array
- Output ONLY valid JSON
- No explanations, no markdown
- Step ids must start from 1
- Use ONLY the allowed tools

Available tools:
1.  get_news
   params: {{ "topic": string, "limit": number }}
2. get_weather
   params: {{ "city": string }}
"""

    HUMAN_PROMPT_TEMPLATE = """
User request:
"{user_query}"

Generate the execution plan as JSON.
"""
    def __init__(self):
        self.llm = LLMClient()
    def create_plan(self, user_query):
        def normalize_plan(parsed_json):
          if "steps" in parsed_json:
            return parsed_json
          if "execution_plan" in parsed_json:
            return {"steps": parsed_json["execution_plan"]}
          raise ValueError("Invalid plan format returned by LLM")
        
        response = self.llm.invoke_with_templates(
            system_prompt=self.SYSTEM_PROMPT,
            human_template=self.HUMAN_PROMPT_TEMPLATE,
            variables={"user_query": user_query},
        )
        try:
            parsed_json = json.loads(response)
            parsed_json = normalize_plan(parsed_json)
            return Plan(**parsed_json)
        except (json.JSONDecodeError, ValidationError):
            retry_response = self.llm.invoke(
                system_prompt=self.SYSTEM_PROMPT + "\nYou MUST output ONLY valid JSON.",
                user_prompt=user_query,
            )
            parsed_json = json.loads(retry_response)
            parsed_json = normalize_plan(parsed_json)
            return Plan(**parsed_json)
