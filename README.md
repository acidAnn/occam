# occam
Remove adjectives and adverbs from a text.

Inspired by the principle of Occam's razor :scissors::
> It is pointless to do with more what can be done with fewer.
William of Ockham (ca.1287-1347), [Summa Totius Logicae](https://en.wikiquote.org/wiki/William_of_Ockham)

:heart: --- for :ox: keeboardmonkee, :butterfly: redadmiral & :crab: schwukas --- :heart:

Happy to use [spaCy](spacy.io) :rocket:.

## setup
```sh
# create a virtual environment
$ python -m venv ./venv

# install required dependencies
$ pip install -r requirements.txt

# download the German language model by spaCy
$ python -m spacy download de
```

## usage
```
Usage: occam.py [OPTIONS]

  Remove adjectives and adverbs from text.

Options:
  -f, --file TEXT    File with text input.
  -t, --text TEXT    String with text input.
  -o, --output TEXT  Path to output file (optional, otherwise print to CLI).
  -j, --adj          Only remove adjectives (default: remove adjectives and
                     adverbs).
  -v, --adv          Only remove adverbs.
  -s, --sub TEXT     String by which adjectives and adverbs shall be replaced.
  -c, --count        Display the number of removed words.
  --help             Show this message and exit.
```
