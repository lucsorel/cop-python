
```puml
@startuml ci-semantic-release-publish
!option handwritten true

participant "branche de dev" as feature
feature -> feature : workflow de build
note right
  vulnérabilités des dépendances (""pip-audit"")

  ""pre-commit"" :
  - format de message de commit (**commitlint**)
    (refactor, fix, feat, etc.)
  - formatage, lint, etc.

  tests automatisés
end note

feature -> main : fusion PR
main -> main : workflow de release
note right
  montée de version (**python-semantic-release**)
  - messages de commits -> nouvelle version ""$NEW_VERSION = maj.min.patch""
  - màj ""pyproject.toml"", ""~__version~__.py"", etc.
  - ""git commit -m "[skip ci] $NEW_VERSION""" (évite de boucler sur le workflow)
  - poussée du nouveau tag (ça n'est pas un commit)

  publication
  - ""uv ~--build publish ~--repository ...""
    (le numéro de version dans pyproject.toml est utilisé pour le numéro de version)
end note

main -> PyPI : publication ""$NEW_VERSION""
@enduml
```