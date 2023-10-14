# Get the API keys
import json
import requests
import openai
from rich.console import Console
c = Console()

json_f_keys = open("api_keys.json")
api_keys = json.load(json_f_keys)
json_f_keys.close()

json_f_urls = open("endpoints.json")
endpoints = json.load(json_f_urls)
json_f_urls.close()

# The Guardian
from theguardian import theguardian_content
def get_guardian(a_query) -> str:
    query = a_query
    headers = {
        "q": query,
        "query-fields": "headline",
        "order-by": "relevance",
        "show-fields": "headline"
    }
    content = theguardian_content.Content(api=api_keys["TheGuardian"], **headers)
    json_content = content.get_content_response()
    headlines = parse_json_guardian(json_content)

    return headlines

def parse_json_guardian(json_content):
    results = []
    for result in json_content["response"]["results"]:
        results.append(result["fields"]["headline"])

    c.log(f"GUARDIAN RESULTS {results}")
    return results

def get_bing(a_query):
    query = a_query
    date = 1 # CHANGE THIS
    headers = {
        "Ocp-Apim-Subscription-Key": api_keys["Azure"],
    }
    params = {
        "q": query
        # "textDecorations": True, 
        # "textFormat": "HTML"
    }
    content = requests.get(endpoints["Bing"], headers=headers, params=params)
    content.raise_for_status()
    json_content = content.json()
    headlines = parse_json_bing(json_content)

    return headlines

def parse_json_bing(json_content):
    print(json_content)
    
    results = []
    for result in json_content["response"]["results"]:
        results.append(result["fields"]["headline"])

    c.log(f"GUARDIAN RESULTS:\n{results}")
    return results

def get_openai(prompt):
    openai.organization = api_keys["OpenAIorg"]
    openai.api_key = api_keys["OpenAI"]
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct", 
        prompt=prompt, 
        max_tokens=300
    )

    result = response['choices'][0]['text'].strip()
    c.log(f"AI RESPONSE:\n{result}")
    return result

