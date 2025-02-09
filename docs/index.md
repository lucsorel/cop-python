# Documentation main page

![](assets/cop-python-logo.png)

## Work on the documentation

Commands:

* `uv run mkdocs serve` - Start the live-reloading docs server.
* `uv run mkdocs build` - Build the documentation site.
* `uv run mkdocs -h` - Print help message and exit.

```text
cop-python
 ├─ cop_python/            # the production code to document
 ├─ mkdocs.yml             # the configuration file
 ├─ docs/
 │  ├─ assets/             # folder for image and style files
 │  │  ├─ cop-python-logo  # project logo
 │  │  └─ seeyousun.css    # additional styling
 │  ├─ index.md            # the documentation homepage
       ...                 # other markdown pages, images and other files
```
