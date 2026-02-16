from evaluator.retrieval_eval import evaluate_retrieval
from evaluator.generation_eval import evaluate_generation

def main():
    print("\n===== RETRIEVAL =====")
    evaluate_retrieval()

    print("\n===== GENERATION =====")
    evaluate_generation()

if __name__ == "__main__":
    main()
