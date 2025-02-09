def capitalize(text: str) -> str:
    assert isinstance(text, str) and (len(text) > 0)
    return text[0].upper() + text[1:].lower()


from sys import argv

csv_input_filepath = argv[1]
f = argv[2]

from os import path

json_output_filepath = path.join(
    path.dirname(csv_input_filepath), path.splitext(path.basename(csv_input_filepath))[0] + "_in_" + f + '.json'
)
print(f'{json_output_filepath=}')

csv_file = open(csv_input_filepath)

# skip CSV column names
next(csv_file)

json_file = open(json_output_filepath, 'w')

csv_line_index = 1
first_entry = True
json_file.write("[\n")
for l in csv_file:
    firstname, lastname, country = l.strip().split(",")
    firstname = capitalize(firstname)
    lastname = capitalize(lastname)

    if country == f:
        if not first_entry == True:
            json_file.write(',\n')
        first_entry = False

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

    csv_line_index = csv_line_index + 1

json_file.write("\n]\n")