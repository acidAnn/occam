import spacy
import click
import os

nlp = spacy.load("de_core_news_sm")


@click.command()
@click.option("--file", help="the file with the text to be processed")
def ockham(file):
    """Remove adjectives from a text to make it more stylistically concise."""
    with open(file) as f:
        text = f.read()

    if text:
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
