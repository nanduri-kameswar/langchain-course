from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

load_dotenv()


class Source(BaseModel):
    """
    Schema for a source used by the agent
    """

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """
    Schema for the agent's response with answer and sources
    """

    answer: str = Field(description="The agent's answer to the query")
    sources: list[Source] = Field(
        default_factory=list,
        description="A list of sources used to generate the answer by the agent",
    )


llm = ChatOllama(model="gpt-oss", base_url="http://localhost:11434")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": [HumanMessage(content="What is the weather in Tokyo?")]}
    )
    print(result)


if __name__ == "__main__":
    main()
