import json
from app.rag_engine import load_retriever

def evaluate_retrieval():

    print("Running Retrieval Evaluation...\n")

    with open("evaluator/dataset.json") as f:
        dataset = json.load(f)

    total = 0
    hit = 0

    for sample in dataset:
        retriever = load_retriever(sample["language"])
        docs = retriever.invoke(sample["query"])

        retrieved_text = " ".join([d.page_content.lower() for d in docs[:3]])

        keyword_match = any(k.lower() in retrieved_text for k in sample["keywords"])

        total += 1
        if keyword_match:
            hit += 1
            status = "✅"
        else:
            status = "❌"

        print(f"{sample['query']}  ->  {status}")

    print("\n==============================")
    print(f"Retrieval Hit Rate: {hit}/{total} = {round(hit/total*100,2)}%")
    print("==============================\n")
