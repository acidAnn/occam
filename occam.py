import spacy
import click
import math
import os

nlp = spacy.load("de_core_news_sm")


@click.command()
@click.option("--file", "-f", "filepath_", default="", help="the file with the text to be processed")
@click.option("--text", "-t", default="", help="the string with the text to be processed")
@click.option("--count", "-c", is_flag=True, help="display the number of removed words")
@click.option("--sub", "-s", default="", help="the string by which adjectives and adverbs shall be replaced")
def ockham(filepath_, text, count, sub):
    """Remove adjectives from a text to make it more stylistically concise."""
    input_text = ""

    if filepath_:
        with open(filepath_) as f:
            input_text = f.read()

    if text:
        input_text += text

    if not input_text:
        raise click.BadParameter("you must supply the option --file or --str for input_text")

    doc = nlp(input_text)

    result_text = ""
    counter = 0

    for i, token in enumerate(doc):
        if token.pos_ in ["ADJ", "ADV"]:
            counter += 1
            if sub:
                result_text += sub

                if (
                    i < len(doc) - 1
                    and token.pos_ != "SPACE"
                    and token.nbor().pos_ not in ["PUNCT", "SPACE", "X"]
                ):
                    result_text += " "


        else:
            result_text += token.text
            if (
                i < len(doc) - 1
                and token.pos_ != "SPACE"
                and token.nbor().pos_ not in ["PUNCT", "SPACE", "X"]
            ):
                result_text += " "

    if count:
        doc_length = len(text)
        print("-- {} words out of {} ({}%) have been removed --".format(counter, doc_length, math.ceil(counter/doc_length*100)))

    print(result_text.strip())


if __name__ == "__main__":
    ockham()
