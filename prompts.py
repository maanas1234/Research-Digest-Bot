from langchain_core.prompts import PromptTemplate


SEACRCH_QUERY_PROMPT_TEMPLATE =  """
Generate 3 web search queries for the given question.

Return ONLY a valid JSON list of strings.
Do NOT include any explanation.

Example:
["query1", "query2", "query3"]

Question: {user_query}
"""

search_query_prompt = PromptTemplate.from_template( template=SEACRCH_QUERY_PROMPT_TEMPLATE )

SUMMARIZE_PROMPT_TEMPLATE = """You are a summarization agent, take this input {scraped} and summarise it in a way to tell the user what they should do. No unnecessary talks only to the point. The query asked by the user was this {user_query}"""

summarize_prompt = PromptTemplate.from_template( template=SUMMARIZE_PROMPT_TEMPLATE )