import json
import ast
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from app.rag_engine import load_retriever

generator = ChatOllama(model="qwen2.5:7b-instruct", temperature=0)
judge = ChatOllama(model="mistral:7b-instruct", temperature=0)


def evaluate_generation():

    print("Running Generation Evaluation...\n")

    with open("evaluator/dataset.json") as f:
        dataset = json.load(f)

    totals = {
        "Relevance":0,
        "Faithfulness":0,
        "Completeness":0,
        "Clarity":0
    }

    count = 0

    for sample in dataset:

        retriever = load_retriever(sample["language"])
        docs = retriever.invoke(sample["query"])
        context = "\n".join([d.page_content for d in docs[:3]])

        answer = generator.invoke([
            HumanMessage(content=f"""
Answer the question using ONLY the context.

Context:
{context}

Question:
{sample['query']}
""")
        ]).content

        evaluation = judge.invoke([
            HumanMessage(content=f"""
You are evaluating an AI coding tutor.

Give score 1-5 for:
Relevance
Faithfulness
Completeness
Clarity

Return ONLY python dict.

Question: {sample['query']}
Context: {context}
Answer: {answer}
""")
        ]).content

        try:
            scores = ast.literal_eval(evaluation)

            for k in totals:
                totals[k] += scores.get(k,0)

            count += 1

            print(sample["query"])
            print(scores)
            print("-----------------------------------")

        except:
            print(sample["query"], "⚠️ Judge parse failed")

    print("\n==============================")
    print("Average Scores")
    print("==============================")

    for k,v in totals.items():
        print(f"{k}: {round(v/count,2)} / 5")
