import json

FILE_PATH = "data/topics.json"


def load_topics():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_topics(topics):
    with open(FILE_PATH, "w") as file:
        json.dump(topics, file, indent=4)