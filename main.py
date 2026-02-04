import json
from agents.planner import PlannerAgent
from agents.executer import ExecutorAgent
from agents.verifier import VerifierAgent


def main():
    user_query = input("Enter your task: ").strip()
    if not user_query:
        print("No input received.")
        return
    planner = PlannerAgent()
    executor = ExecutorAgent()
    verifier = VerifierAgent()
    plan = planner.create_plan(user_query)
    print(json.dumps(plan.model_dump(), indent=2))
    results = executor.execute(plan)
    print(json.dumps(results, indent=2))
    final_output = verifier.verify(plan, results)
    print(json.dumps(final_output, indent=2))

if __name__ == "__main__":
    main()
