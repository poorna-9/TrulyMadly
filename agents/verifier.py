from typing import Dict, Any
from agents.planner import Plan

class VerifierAgent:
    def verify(self,plan,execution_results):
        verified_output = {
            "status": "success",
            "steps": [],
        }
        for step in plan.steps:
            result = execution_results.get(step.id)
            if result is None or "error" in result:
                verified_output["status"] = "partial_failure"
                verified_output["steps"].append({
                    "step_id": step.id,
                    "action": step.tool,
                    "status": "failed",
                    "details": result
                })
            else:
                verified_output["steps"].append({
                    "step_id": step.id,
                    "action": step.tool,
                    "status": "completed",
                    "output": result
                })
        return verified_output
