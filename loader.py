import json
import pandas

# class config:


def load_config() -> dict:
    with open("config.json", 'r') as f:
        return json.load(f)

aawd = object()

class aawd:
    art = 0

setattr(aawd, 'art', '6')

print(aawd.art)