# Get the API keys
import json

json_f = open("api_keys.json")
api_keys = json.load(json_f)
json_f.close()

# The Guardian
from theguardian import theguardian_content
def get_guardian() -> str:
    query = "Microsoft"
    date = 1 # CHANGE THIS
    headers = {
        "q": query,
        # "tag": "film/film,tone/reviews",
        "from-date": date,
        "order-by": "relevance",
        "show-fields": "headline",
    }
    content = theguardian_content.Content(api=api_keys["TheGuardian"], **headers)
    json_content = content.get_content_response()
    headlines = parse_json_guardian(json_content)

def parse_json_guardian(json_content):
    # print(json_content["response"]["results"])


    results = []
    for result in json_content["response"]["results"]:
        results.append(result["fields"]["headline"])

    return results