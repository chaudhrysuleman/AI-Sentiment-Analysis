from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class TopicAnalysis(BaseModel):
    topic: str = Field(description="The specific topic discussed in this part of the review (e.g., 'Sound Quality', 'Shipping', 'Comfort').")
    sentiment: str = Field(description="The sentiment specific to this topic. Must be one of: Positive, Negative, or Neutral.")
    summary: str = Field(description="A concise summary of what the customer said about this specific topic.")

class ReviewAnalysis(BaseModel):
    general_sentiment: str = Field(description="The overall sentiment of the entire review.")
    general_summary: str = Field(description="A summary of the entire review.")
    topic_analyses: List[TopicAnalysis] = Field(description="A list of analyses for each distinct topic extracted from the review.")

# Initialize Parser
parser = PydanticOutputParser(pydantic_object=ReviewAnalysis)
format_instructions = parser.get_format_instructions()
