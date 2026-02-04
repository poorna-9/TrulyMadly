import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

class LLMClient:
    def __init__(self,model_name: str = "gpt-4o-mini",temperature: float = 0.2, max_tokens: int = 1024,):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.llm=ChatOpenAI(
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            openai_api_key=openai_api_key,
        )
    def invoke(self,system_prompt,user_prompt):
        messages=[SystemMessage(content=system_prompt),HumanMessage(content=user_prompt)]
        response=self.llm.invoke(messages)
        return response.content
    def invoke_with_templates(self,system_prompt,human_template,variables):
        prompt=ChatPromptTemplate.from_messages(
            [("system", system_prompt),("human", human_template)]
        )
        chain = prompt | self.llm
        response = chain.invoke(variables)
        return response.content
    