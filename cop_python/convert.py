from typing import TypedDict, Iterator
from argparse import ArgumentParser, Namespace
from pathlib import Path
from csv import DictReader
from json import dump

class Contact(TypedDict):
    """
    Models a contact, either read from a csv file or written in the json file.
    """

    firstname: str
    lastname: str
    country: str
    row: int

def capitalize(text: str) -> str:
    """
    Capitalizes the input text ("text" -> "Text").

    Args:
        text: the text to capitalize

    Returns:
        the capitalized text

    Raise:
        ValueError if the input is invalid
    """
    if not isinstance(text, str) or len(text) <= 0:
        raise ValueError(f"text must be a non-empty string, got {text}")

    return text[0].upper() + text[1:].lower()

def load_contacts(csv_path: Path) -> Iterator[Contact]:
    with open(csv_path, encoding="utf-8") as csv_file:
        contacts_reader = DictReader(csv_file)
        for row_index, contact in enumerate(contacts_reader, start=1):
            contact["row"] = row_index
            yield contact

def format_contact(contact: Contact) -> Contact:
    """
    Capitalizes the firstname and lastname of the given contact in a new instance.

    Args:
        contact: the contact data to format

    Raise:
        ValueError if the firstname or the lastname are invalid
    """
    return {**contact, "firstname": capitalize(contact["firstname"]),
        "lastname": capitalize(contact["lastname"])}

def get_conversion_arguments() -> Namespace:
    parser = ArgumentParser(description="reads contacts from a csv file, filter them by country, formats them and write them in a json file")
    parser.add_argument("--csv_input", required=True, type=Path, help="the csv where input contacts are read")
    parser.add_argument("--country_filter", required=True, help="the country to filter the contacts in")

    return parser.parse_args()

if __name__ == "__main__":
    args = get_conversion_arguments()
    csv_input_path: Path = args.csv_input
    country_filter: str = args.country_filter
    json_output_path = csv_input_path.parent / f"{csv_input_path.stem}_in_{country_filter}_v2.json"

    contacts_iter = load_contacts(csv_input_path)
    formatted_filtered_contacts_iter = (
        format_contact(contact)
        for contact in contacts_iter
        if contact["country"] == country_filter
    )

    with open(json_output_path, "w", encoding="utf-8") as json_file:
        dump(list(formatted_filtered_contacts_iter), json_file, indent=2, ensure_ascii=False)
