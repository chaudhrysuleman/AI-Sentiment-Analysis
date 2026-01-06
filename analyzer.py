from langchain.prompts import ChatPromptTemplate
from sentiment_setup import chat_llm
from model import parser, format_instructions

def get_analysis_chain():
    """Create the LCEL chain for sentiment analysis."""
    review_template = """
    Analyze the following customer review.
    Identify all distinct topics discussed (e.g., product quality, shipping, customer service, price).
    For each topic, provide the sentiment and a summary.
    Also provide an overall sentiment and summary for the whole review.

    Review: {review}

    {format_instructions}
    """
    
    template = ChatPromptTemplate.from_template(review_template)
    chain = template | chat_llm | parser
    return chain

def analyze_reviews(reviews):
    """Analyze a list of reviews."""
    chain = get_analysis_chain()
    inputs = [{"review": review, "format_instructions": format_instructions} for review in reviews]
    results = chain.batch(inputs)
    return results
