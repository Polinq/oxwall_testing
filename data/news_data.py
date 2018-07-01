import json
from data.random_string import random_string
import os
from conftest import PROJECT_DIR

filename = os.path.join(PROJECT_DIR, "data", "data_news.json")

with open(filename, encoding="utf8") as f:
    news_list = json.load(f)

news_list += [{"text": random_string(50, cyrillic=True)} for _ in range(2)]
