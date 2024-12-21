from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
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
        "Amazon": "AMZN"
    }
    return symbols.get(company,"Unknown")
    # TODO: Implement this function using Yahoo Finance API"""
#load_dotenv()
agent=Agent(
    name='my_agent',
    #model=Groq(id="llama-3.1-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools( stock_price=True, analyst_recommendations=True, stock_fundamentals=True),get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display the data",
                  "You are a highly knowledgeable Stock trader with 20 years of experience and having 10 years of experience in options trading",
                  "If you don't know the company symbol, please use get_company_symbol tool",
                  "If you don't know which companies to search for, Please use get_company_symbol"]

)

agent.print_response("Can you tell me whether to go for calls or puts for TSLA and Amazon")
