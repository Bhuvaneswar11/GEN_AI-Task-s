from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

memory.save_context({"input": "Hi"}, {"output": "Hello"})
print(memory.load_memory_variables({}))