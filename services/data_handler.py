import pickle


def save(file_path, data):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)


def load(file_path):
    try:
        with open(file_path, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        save(file_path, [])
        return []
    except EOFError:
        return []
