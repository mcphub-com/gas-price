import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/collectapi/api/gas-price'

mcp = FastMCP('gas-price')

@mcp.tool()
def european_countries() -> dict: 
    '''Service that brings up the current gasoline prices at european countries.'''
    url = 'https://gas-price.p.rapidapi.com/europeanCountries'
    headers = {'x-rapidapi-host': 'gas-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def all_usa_price() -> dict: 
    '''Service that brings the average current gasoline prices of states in America.'''
    url = 'https://gas-price.p.rapidapi.com/allUsaPrice'
    headers = {'x-rapidapi-host': 'gas-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def canada() -> dict: 
    '''The service that brings gas prices in the Canada.'''
    url = 'https://gas-price.p.rapidapi.com/canada'
    headers = {'x-rapidapi-host': 'gas-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def state_usa_price(state: Annotated[str, Field(description='')]) -> dict: 
    '''The service that brings gas prices in the United States by state.'''
    url = 'https://gas-price.p.rapidapi.com/stateUsaPrice'
    headers = {'x-rapidapi-host': 'gas-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def usa_cities_list() -> dict: 
    '''The service that get list of cities with price information in the USA.'''
    url = 'https://gas-price.p.rapidapi.com/usaCitiesList'
    headers = {'x-rapidapi-host': 'gas-price.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
