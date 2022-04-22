from dataclasses import dataclass
import typing
import json

@dataclass
class Owner:
    name: str = 'Unknown name'
    age: int = 'Unknown age'
    description: typing.Any = None
    code_name: str = None

    def update_owner(self, list_of_attr: list):
        with open('Owner_dict.json', 'r', encoding='utf8') as input_file:
            json_dict = json.load(input_file)
        with open('Owner_dict.json', mode="w+", encoding='utf8') as output_file:
            for attribute in list_of_attr:
                new_attr = getattr(self, attribute, None)
                if new_attr:
                    json_dict[attribute] = new_attr
            json.dump(json_dict, output_file)
