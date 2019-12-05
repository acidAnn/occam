"""A module for removing embellishing adjectives and adverbs from text.

Functions:
occam
"""
from typing import List, Tuple

import spacy
import click
import math

nlp = spacy.load("de_core_news_sm")


@click.command()
@click.option("--file", "-f", "filename_", default="", help="File with text input.")
@click.option("--text", "-t", default="", help="String with text input.")
@click.option("--output", "-o", default="", help="Path to output file (optional, otherwise print to CLI).")
@click.option("--adj", "-j", is_flag=True, help="Only remove adjectives (default: remove adjectives and adverbs).")
@click.option("--adv", "-v", is_flag=True, help="Only remove adverbs.")
@click.option("--sub", "-s", default="", help="String by which adjectives and adverbs shall be replaced.")
@click.option("--count", "-c", is_flag=True, help="Display the number of removed words.")
def occam(filename_: str, text: str, output: str, adj: bool, adv: bool, sub: str, count: bool):
    """Remove adjectives and adverbs from text."""
    input_text = determine_input_text(filename_, text)
    text_length = len(input_text)
    doc = nlp(input_text)

    removables = determine_removables(adj, adv)

    output_text, counter = remove_removables(doc, text_length, removables, sub)

    if count:
        print_counter(counter, text_length)

    output_text = output_text.strip()
    show_output_text(output, output_text)


def determine_input_text(filepath_: str, text: str) -> str:
    """Determine whether input was supplied directly in a string or indirectly in a file.

    :param filepath_: str representing the path to an text file (empty if no file supplied by user)
    :param text: str representing the text input (empty if no string supplied by user)
    :return: the input text as a str
    """
    input_text = ""

    if text:
        input_text += text

    # if both a string and a file path are supplied, they are concatenated to a single input text
    if filepath_:
        with open(filepath_) as f:
            input_text += f.read()

    if not input_text:
        raise click.BadParameter(
            "You must supply the option --file or --text for text input."
        )

    return input_text


def determine_removables(adj: bool, adv: bool) -> List[str]:
    """Decide if only adjectives, only adverbs or both shall be removed.

    :param adj: bool representing whether adjectives shall be removed
    :param adv: bool representing whether adverbs shall be removed
    :return: a list of part of speech tags representing the POS to be removed
    """
    if adj:
        return ["ADJ"]

    elif adv:
        return ["ADV"]

    else:
        return ["ADJ", "ADV"]


def remove_removables(doc, text_length: int, removables: List[str], sub: str) -> Tuple[str, int]:
    """Remove adjectives and/or adverbs from doc.

    :param doc: the input text as a spacy Doc object
    :param text_length: the input length as an int
    :param removables: a List of part of speech tags representing the POS to be removed
    :param sub: str by which the removables shall be replaced (empty if not supplied by user)
    :return: the output text without removables, the number of removed tokens
    """
    output_text = ""
    counter = 0

    for i, token in enumerate(doc):
        if token.pos_ in removables:
            counter += 1

            if sub:
                output_text += sub

            if whitespace_needed(i, text_length, token):
                output_text += " "

        else:
            output_text += token.text

            if whitespace_needed(i, text_length, token):
                output_text += " "

    return output_text, counter


def whitespace_needed(index: int, text_length: int, token) -> bool:
    """Determine if a token and its predecessor should be seperated by whitespace.

    :param index: the int index of token in the input text
    :param text_length: the length of the input text
    :param token: the spacy Token object to be considered
    :return: True if whitespace is needed
             False otherwise
    """
    return (
        index < text_length - 1
        and token.pos_ != "SPACE"
        and token.nbor().pos_ not in ["PUNCT", "SPACE", "X"]
    )


def print_counter(counter: int, text_length: int):
    """Print the number of removed words relative to the text length.
   
   :param counter: int representing the number of removed words
   :param text_length: int representing the overall text length
   """
    if text_length > 0 and counter > 0:
        removed_percentage = math.ceil(counter / text_length * 100)
        print(
            "-- {} words out of {} ({}%) have been removed --".format(
                counter, text_length, removed_percentage
            )
        )

    else:
        print("-- nothing to remove: Occam would be proud of you :) --")


def show_output_text(output: str, output_text: str):
    """Provide the output text to the user, either by printing it or writing it to a file.

    :param output: the path to an output file (empty if not supplied by the user)
    :param output_text: the result str
    """
    if output:
        with open(output, mode="w") as f:
            f.write(output_text)

    else:
        print(output_text)


if __name__ == "__main__":
    occam()
