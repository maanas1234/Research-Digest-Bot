from web_tools import web_search
from llm_models import get_llm_offline
from llm_models import get_llm_online
from prompts import search_query_prompt,summarize_prompt
from web_tools import web_scrape
import json

user_query= "What is the best place to eat kachori in Jaipur?"
search_query_prompt1=search_query_prompt.format(user_query=user_query)

llmON = get_llm_online()
llmOFF=get_llm_offline()
response = llmOFF.invoke(search_query_prompt1)

web_search_query_list = json.loads(response.content)
print(web_search_query_list)


all_urls= []
for q in web_search_query_list:
    all_urls.extend(web_search(q,3))

all_urls = list(set(all_urls))

scraped = [web_scrape(url)[:2000] for url in all_urls]


#print(scraped)


summarize_prompt1 = summarize_prompt.format(scraped=scraped,user_query=user_query)
final_output = llmOFF.invoke(summarize_prompt1)

print(final_output.content)
#check = [{'url_results':web_search(q,3)}for q in web_search_query_list]
#print(check)

#print(response.content)