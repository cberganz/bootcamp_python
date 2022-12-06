import sys

class Generator:
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    def __init__(self, text, sep=" ", option=None):
        if not isinstance(text, str) or not isinstance(sep, str):
            print("Error: Invalid arguments")
            sys.exit(1)
        self.text = text
        self.sep = sep
        no_option()

    def no_option(self):
        splited = self.text.split(self.sep)
        for word in splited:
            yield word

if __name__ == '__name':
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in Generator(text):
        print(word)
