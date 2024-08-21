import yaml
import sys

def read_yaml_file(file_path):
    items = []

    with open(file_path, 'r') as file:
        documents = yaml.safe_load_all(file)

        for (i, document) in enumerate(documents):
            items.append(document)
        
        return items
    
def save_output_yaml_file(documents, file_path):
    with open(file_path, 'w') as file:
        yaml.dump_all(documents, file)

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

class RecipeItem:
    def __init__(self, document):
        self.document = document

    def set_time(self, time):
        self.document['time'] = clamp(int(time), 1, int(time))
    def get_time(self):
        return self.document['time']

class RecipeModifier:
    def __init__(self, document):
        self.time = document['mod']['time']

    def apply(self, recipe: RecipeItem):
        recipe.set_time(self.time * recipe.get_time())

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: py recipe-update.py <mod_file> <file_name> <output_file>")
        sys.exit(1)

    mod_file_path = sys.argv[1]
    file_path = sys.argv[2]
    output_file_path = sys.argv[3]
    # mod_file_path = "recipe-x100.mod.yaml"
    # file_path = "recipes.yaml"
    # output_file_path = "output.yaml"

    mod_documents = read_yaml_file(mod_file_path)
    documents = read_yaml_file(file_path)
    
    for (i, mod_doc) in enumerate(mod_documents):
        mod = RecipeModifier(mod_doc)

        for (i, document) in enumerate(documents):
            recipe = RecipeItem(document)
            mod.apply(recipe)

    save_output_yaml_file(documents, output_file_path);
