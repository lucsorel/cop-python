from argparse import ArgumentParser
from json import dump
from csv import reader
from os import path
from sys import argv

def capitalize(text: str) -> str:
    # TODO existe peut-être déjà
    assert isinstance(text, str) and text
    return text[0].upper() + text[1:].lower()

if __name__ == "__main__":
    # TODO utiliser argparse
    csv_input_filepath = argv[1]
    selected_country = argv[2]

    # TODO utiliser pathlib.Path

    json_output_filepath = path.join(
        path.dirname(csv_input_filepath), f"{path.splitext(path.basename(csv_input_filepath))[0]}_in_{selected_country}.json"
    )
    # print(f'{json_output_filepath=}') -> logger

    with (
        open(json_output_filepath, 'w') as json_file,
        open(csv_input_filepath) as csv_file,
    ):
        # skip CSV column names
        next(csv_file)

        csv_line_index = 1
        first_entry = True
        json_file.write("[\n")
        for l in csv_file:
            # TODO faire des fonctions
            # capitaliser après le filtrage
            firstname, lastname, country = l.strip().split(",")
            firstname = capitalize(firstname)
            lastname = capitalize(lastname)

            if country == selected_country:
                if not first_entry == True:
                    json_file.write(',\n')
                first_entry = False

                # TODO fstring, dump
                json_file.write(
                    '\t{"row": '
                    + str(csv_line_index)
                    + ', "firstname": "'
                    + firstname
                    + '", "lastname": "'
                    + lastname
                    + '", "country": "'
                    + country
                    + '"}'
                )

            csv_line_index += 1

        json_file.write("\n]\n")