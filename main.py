from typing import Any
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> Any:
    """
    Tool that searches the query over the internet.
    Args:
        query: The query to search for.
    Returns:
        The search results.
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatOllama(model="gpt-oss", base_url="http://localhost:11434")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    print(result)

if __name__ == "__main__":
    main()
