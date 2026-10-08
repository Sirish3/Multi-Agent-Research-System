from src.tools.tools import web_search, scrape_url

# output = web_search("What is the capital of France?")

# print(output)

result = scrape_url.invoke({"url": "https://www.reddit.com/r/artificial"})

print(result)