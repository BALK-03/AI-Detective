import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


dict = {"test-real": (True, r"C:\Users\Lakhal Badr\Desktop\AI-Detective\data\test\REAL"),
        "test-fake": (False, r"C:\Users\Lakhal Badr\Desktop\AI-Detective\data\test\FAKE"),
        "train-real": (True, r"C:\Users\Lakhal Badr\Desktop\AI-Detective\data\train\REAL"),
        "train-fake": (False, r"C:\Users\Lakhal Badr\Desktop\AI-Detective\data\train\FAKE")
}

images_path = {
    "test-real": (True, os.path.join(BASE_DIR, "data/test/REAL")),
    "test-fake": (False, os.path.join(BASE_DIR, "data/test/FAKE")),
    "train-real": (True, os.path.join(BASE_DIR, "data/train/REAL")),
    "train-fake": (False, os.path.join(BASE_DIR, "data/train/FAKE"))
}

datasets = {
    "test-real": os.path.join(BASE_DIR, "data/test-real.csv"),
    "test-fake": os.path.join(BASE_DIR, "data/test-fake.csv"),
    "train-real": os.path.join(BASE_DIR, "data/train-real.csv"),
    "train-fake": os.path.join(BASE_DIR, "data/train-fake.csv")
}

model_path = os.path.join(BASE_DIR, "models/model.keras")

model_prams = {
    "input_shape": (32, 32, 3),
    "threshold": 0.5,
    "optimizer": "adam",
    "loss": "binary_crossentropy",
    "seed": 0,
    "epochs": 20
}