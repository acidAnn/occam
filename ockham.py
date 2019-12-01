import spacy
import click
import os

nlp = spacy.load("de_core_news_sm")

@click.command()
@click.option('--file', help='the file with the text to be processed')
def ockham(file):
    """Remove adjectives from a text to make it more stylistically concise."""
#    print(os.path.abspath(file))
    with open(file) as f:
        text = f.read()

    if text:
        doc = nlp(text)
    
        result_text = ""
        for token in doc:
            if token.pos_ not in ["ADJ", "ADV"]:
                if token.pos_ != "PUNCT":
                   result_text += " "

                result_text += token.text
     
        print(result_text.strip())


if __name__ == '__main__':
    ockham()
