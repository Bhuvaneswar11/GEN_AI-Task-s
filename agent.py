from langchain.agents import initialize_agent, Tool

def multiply(x):
    return int(x) * 2

tools = [
    Tool(
        name="Multiplier",
        func=multiply,
        description="Multiply a number by 2"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

print(agent.run("Double 5"))