from analyzer import analyze_reviews

# Sample Reviews
review1 = """
This product is amazing! I've been using it for a week and it exceeded my expectations.
The build quality is top-notch and the customer service was very helpful when I had a question.
Highly recommended to everyone!
"""

review2 = """
I'm very disappointed with this purchase. It arrived broken and the instructions were missing.
I tried contacting support but got no response. Complete waste of money.
Avoid this product at all costs.
"""

review3 = """
It's okay, does what it says but nothing special. For the price, I expected a bit more features.
It works fine for basic tasks but struggles with more complex ones.
I might look for an alternative next time.
"""

review4 = """
The headphones sound incredible, the bass is punchy and the highs are crisp.
However, the delivery was a nightmare. It took two weeks longer than expected and the box was crushed.
Also, the ear cups are a bit uncomfortable after long listening sessions.
"""

def main():
    reviews = [review1, review2, review3, review4]
    
    print("Starting Sentiment Analysis on 4 reviews...\n")
    results = analyze_reviews(reviews)
    
    for i, result in enumerate(results):
        print(f"--- Analysis for Review {i+1} ---")
        print(result.model_dump_json(indent=2))
        print("\n")

if __name__ == "__main__":
    main()
