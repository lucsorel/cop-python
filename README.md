# cop-python

```sh
python3 convert.py .local/contacts.csv France

python3 cop_python/convert.py --csv_input .local/contacts.csv --country_filter France
python3 -m cop_python.convert --csv_input .local/contacts.csv --country_filter France
python3 cop_python/convert.py --help
uv run cop_python/convert.py --help

uv run ruff check
uv run ruff format

uv run isort
```

## Expérimentations et leçons

`assert {expr}`

```sh
python3 check_convert.py
an error occurred: ''
# pas de message d'erreur

$ python3 -O check_convert.py
Traceback (most recent call last):
  File ".../cop-python/check_convert.py", line 5, in <module>
    capitalize(42)
  File ".../cop-python/convert.py", line 5, in capitalize
    return text[0].upper() + text[1:].lower()
# /!\ assert désactivé
```

-> utiliser pytest et ses outils pour tester les cas droits et d'erreurs
