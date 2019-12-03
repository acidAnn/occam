import spacy
import click
import os

nlp = spacy.load("de_core_news_sm")


@click.command()
@click.option("--file", "-f", "filepath_", default="", help="the file with the text to be processed")
@click.option("--str", "-s", "str_", default="", help="the string with the text to be processed")
def ockham(filepath_, str_):
    """Remove adjectives from a text to make it more stylistically concise."""
    text = ""

    if filepath_:
        with open(filepath_) as f:
            text = f.read()

    if str_:
        text += str_

    if not text:
        raise click.BadParameter("you must supply the option --file or --str for input")

    doc = nlp(text)

    result_text = ""
    for i, token in enumerate(doc):
        if token.pos_ not in ["ADJ", "ADV"]:
            result_text += token.text
            if (
                i < len(doc) - 1
                and token.pos_ != "SPACE"
                and token.nbor().pos_ not in ["PUNCT", "SPACE", "X"]
            ):
                result_text += " "

    print(result_text.strip())


if __name__ == "__main__":
    ockham()
