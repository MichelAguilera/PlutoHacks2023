from Scraper.api_handler import get_guardian, get_bing, get_openai

def main():
    query = input("Search for: ")

    headlines = get_headlines(query)
    response = get_ai_response(headlines)
    # print(response)

def get_headlines(query):
    return get_guardian(query)

def list_to_string(headlines):
    headlines_string = ""
    for headline in headlines:
        headlines_string += "* " + headline + "\n"
    return headlines_string

def get_ai_response(headlines):
    headlines = list_to_string(headlines)
    
    BOILERPLATE = f"This is a list of recent headlines about a specific company, please analyze them and give me advice on whether it is currently safe to invest in this company based on its media coverage.\n{headlines}\nBe professional and concise, keep your answers to one or two paragraphs."

    response = get_openai(BOILERPLATE)
    return response

if __name__ == "__main__":
    main()
