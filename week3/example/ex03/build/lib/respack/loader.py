from importlib.resources import files
import json

def get_config():
    data_path = files("respack").joinpath("data/config.json")
    return json.loads(data_path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    print("Loaded Data:", get_config())
