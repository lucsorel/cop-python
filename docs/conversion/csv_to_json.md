# Convert

This module:

- loads contacts from a csv file
- filters them in based on their country
- exports them in a json file

Here is how you can use it:

```sh
# using python
python3 cop_python/convert.py --csv_input .local/contacts.csv --country_filter France

# using uv
uv run cop_python/convert.py --csv_input .local/contacts.csv --country_filter France
```

::: cop_python.convert