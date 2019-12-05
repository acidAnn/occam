# occam
Remove adjectives and adverbs from text.

A CLI tool for German text, powered by the NLP rocket science of [spaCy](spacy.io) :rocket:.

:heart: For :ox: keyboardmonkee, :butterfly: redadmiral & :crab: schwukas :heart:

## Philosophy
Inspired by the principle of **Occam's razor** :scissors::
> It is pointless to do with more what can be done with fewer.

William of Ockham (ca.1287-1347), [Summa Totius Logicae](https://en.wikiquote.org/wiki/William_of_Ockham)

The simplest solution is most likely the right one - this also holds true for writing. However, it is a difficult task to declutter text, to strip it down to the gist of what one wants to express.

An easy way to start is to reconsider how a text uses adjectives and adverbs. Both can contribute to expressiveness, but they can also make a text feel clumsy if they only serve as embellishments.

**occam** to the rescue! **occam** shows how your text would look without adjectives and adverbs. Thus, it helps you to reconsider how you could make your text more concise and how to use your adjectives and adverbs purposefully.

## Setup
```sh
# create a virtual environment
$ python -m venv ./venv

# install required dependencies
$ pip install -r requirements.txt

# download the German language model by spaCy
$ python -m spacy download de
```


## Usage
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
