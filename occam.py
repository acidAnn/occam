"""A module for removing embellishing adjectives and adverbs from text.

Functions:
occam
"""
import spacy
import click
import math
import os

nlp = spacy.load("de_core_news_sm")


@click.command()
@click.option("--file", "-f", "filepath_", default="", help="File with text input")
@click.option("--text", "-t", default="", help="String with text input")
@click.option("--output", "-o", default="", help="Path to output file (optional, otherwise print to CLI)")
@click.option("--count", "-c", is_flag=True, help="Display the number of removed words")
@click.option("--sub", "-s", default="", help="String by which adjectives and adverbs shall be replaced")
@click.option("--adj", "-j", is_flag=True, help="Only remove adjectives")
@click.option("--adv", "-v", is_flag=True, help="Only remove adverbs")
def occam(filepath_, text, count, sub, adj, adv, output):
    """Remove adjectives and adverbs from text."""
    input_text = ""
    output_text = ""
    counter = 0

    if text:
        input_text += text

    if filepath_:
        with open(filepath_) as f:
            input_text += f.read()

    if not input_text:
        raise click.BadParameter("You must supply the option --file or --text for text input.")

    doc = nlp(input_text)

    if adj:
        removables = ["ADJ"]

    elif adv:
        removables = ["ADV"]
    
    else:
        removables = ["ADJ", "ADV"]

    for i, token in enumerate(doc):
        if token.pos_ in removables:
            counter += 1

            if sub:
                output_text += sub

                if (
                    i < len(doc) - 1
                    and token.pos_ != "SPACE"
                    and token.nbor().pos_ not in ["PUNCT", "SPACE", "X"]
                ):
                    output_text += " "


        else:
            output_text += token.text

            if (
                i < len(doc) - 1
                and token.pos_ != "SPACE"
                and token.nbor().pos_ not in ["PUNCT", "SPACE", "X"]
            ):
                output_text += " "

    if count:
        doc_length = len(input_text)
        if doc_length > 0 and counter > 0:
            print("-- {} words out of {} ({}%) have been removed --".format(counter, doc_length, math.ceil(counter/doc_length*100)))

        else:
            print("-- nothing to remove: Occam would be proud of you :) --")
        
    output_text = output_text.strip()

    if output:
       with open(output, mode='w') as f:
           f.write(output_text)
       
    else:
       print(output_text.strip())


if __name__ == "__main__":
    occam()
