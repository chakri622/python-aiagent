from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from dotenv import load_dotenv
import os


def get_mag7_companies() -> list:
    """
    Use this function to get the default stock tickers to search

    Args:
        None
    Returns:
        list[str]: Stock symbols of the companies
    """
    symbols = {
        "Tesla": "TSLA",
        "Nvidia": "NVDA",
        "Microsoft": "MSFT",
        "Apple": "AAPL",
        "Broadcom": "AVGO",
        "Facebook": "META",
        "Google": "GOOGL",
        "Amazon": "AMZN"
    }
    return ["TSLA","NVDA","MSFT","AAPL","AVGO","META","GOOGL","AMZN"]
def get_company_symbol(company:str) -> str:
    """
    Use this function to get the stock symbol for a given company

    Args:
        company (str): Name of the company
    Returns:
        str: Stock symbol of the company
    """
    symbols = {
        "Tesla": "TSLA",
        "Nvidia": "NVDA",
        "Microsoft": "MSFT",
        "Apple": "AAPL",
        "Broadcom": "AVGO",
        "Facebook": "FB",
        "Google": "GOOGL",
        "Amazon": "AMZN",
        "IBM":"IBM"

    }
    return symbols.get(company,"Unknown")
    # TODO: Implement this function using Yahoo Finance API"""
#load_dotenv()

# web_agent
web_agent=Agent(
    name='my_agent',
    #model=Groq(id="llama-3.1-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    tools=[GoogleSearch(),get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include sources"]

)

finance_agent=Agent(
    name='my_agent',
    #model=Groq(id="llama-3.1-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools( stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display the data",
                  "You are a highly knowledgeable Stock trader with 20 years of experience and having 10 years of experience in options trading",                  
                  ]

)

agent_team=Agent(
    team=[web_agent,finance_agent],
    #model=Groq(id="llama-3.1-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include sources","Use tables to display data"]

)

agent_team.print_response("Can you list down the top quantum stocks to invest and analyst recommendations")
