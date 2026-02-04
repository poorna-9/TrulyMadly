from typing import Dict, Any
from tools.news_tool import NewsTool
from tools.weather_tool import WeatherTool
from agents.planner import Plan


class ExecutorAgent:
    def __init__(self):
        self.news_tool =NewsTool()
        self.weather_tool = WeatherTool()

        self.tool_registry = {
            "get_news": self.news_tool.get_news,
            "get_weather": self.weather_tool.getweather,
        }
    def execute(self, plan):
        results = {}
        for step in plan.steps:
            action = step.tool
            params = step.params
            if action not in self.tool_registry:
                results[step.id] = {"error": f"Unknown action: {action}"}
                continue
            try:
                tool_function = self.tool_registry[action]
                results[step.id] = tool_function(**params)
            except Exception as e:
                results[step.id] = {"error": str(e)}
        return results
