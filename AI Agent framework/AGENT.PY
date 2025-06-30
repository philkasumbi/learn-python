"""
AI AGENT - a system that percieves its environment as an input, make a decision to achieve a specific goal
example - personal assistant,bot,script

we start with perception(input adpater) - reasoning - action(output adpater) - real world effect - memory  and then the circle repeats itself

env is use to hold the sensitive information like the api keys 
requirements.txt is used to store the dependencies versions like the libraries 
agent.py - main orchastartor,should run everthing
modules/ - store modules-perception.py,brain.py,action.py(behaviours of our ai agents)

"""
from modules.perception import parse
from modules.brain import decide
from modules.action import add_task,list_tasks,remove_task

def run():
    print("To-Do Agent live. type 'exit' to quit")
    while True:
        user_input = input("\nYou")
        if user_input.lower in ("exit","quit"):
            print("See you next time")
            break
        # perception
        command = parse(user_input)

        # reasoning
        decision = decide(command)
        tool,args = decision.get("tool"),decision.get("args",{})
        # action
        match tool:
            case "add_task": print(add_task(**args))
            case "list_tasks": print(list_tasks())
            case "remove_tasks": print(remove_task(**args))
            case _:
                print(f"? Unrecognized tool")

if __name__ == "__main__":
    run()