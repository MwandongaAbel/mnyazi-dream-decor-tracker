
# firebase_helper.py - helper functions for Firebase operations (optional)
import os, json
def load_config(path='config/firebase_config.json'):
    if not os.path.exists(path):
        raise FileNotFoundError('Firebase config not found. Create config/firebase_config.json from sample.')
    with open(path,'r') as f:
        return json.load(f)
