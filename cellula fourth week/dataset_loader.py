from datasets import load_dataset


def load_dataset_data():

    dataset = load_dataset("openai/openai_humaneval")

    return dataset["test"]


def load_prompts():

    data = load_dataset_data()

    prompts = []

    for row in data:
        prompts.append(row["prompt"])

    return prompts