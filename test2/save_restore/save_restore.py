import pickle

def save_galaxy(galaxy, path):
    with open(path, 'wb') as file:
        pickle.dump(galaxy, file)

def load_galaxy(path):
    with open(path, 'rb') as file:
        content = pickle.load(file)
        return content


