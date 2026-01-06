# Sentiment Analysis LLM

This project uses [LangChain](https://github.com/langchain-ai/langchain) and OpenAI's GPT models to perform structured sentiment analysis on customer reviews. It extracts distinct topics, assigns sentiment (Positive, Negative, Neutral) to each, and provides summaries.

## Key Features

- **Structured Output**: Uses Pydantic to enforce a strict JSON output schema.
- **Topic Extraction**: Automatically identifies key topics (e.g., Shipping, Quality, Price).
- **Modular Design**:
    - `main.py`: Main execution script.
    - `analyzer.py`: Encapsulates the analysis logic and LangChain pipeline.
    - `model.py`: Defines the data models.
    - `sentiment_setup.py`: Configuration.

## Setup

1. **Environment Variables**:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r sentiment-analysis-LLM/requirements.txt
   ```

## How to Run

Execute the main script:
```bash
python sentiment-analysis-LLM/main.py
```

## Example Output

```json
{
  "general_sentiment": "Positive",
  "general_summary": "Highly recommended to everyone!",
  "topic_analyses": [
    {
      "topic": "Product Quality",
      "sentiment": "Positive",
      "summary": "The build quality is top-notch"
    }
  ]
}
```
# AI-Sentiment-Analysis
