import glob
import json
import os
import random

names = []
good_names = []

for filename in glob.glob('names/*.json'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        json_data = json.load(f)
        for name in json_data['names']:
            if name not in names:
                names.append(name)

random.shuffle(names)
print("There are " + str(len(list(filter(lambda item: item.endswith('y'), names)))) + " names")
for name in names:
    if name.endswith("y"):
        option = input(name + " [y/N] ")
        if option.lower() == "y":
            good_names.append(name)
#    input(name)

print("All done! Here are your choices:")
for name in good_names:
    print(name)
