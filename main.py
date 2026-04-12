from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

response = llm.predict("Explain LangChain in one line")
print(response)

chain=prompt | llmfrom langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms"
)

print(template.format(topic="LangChain"))from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=template)
result = chain.run("LangChain")

print(result)

