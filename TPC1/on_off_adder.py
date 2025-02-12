from enum import Enum, auto
from dataclasses import dataclass
import sys

class Type(Enum):
    ON = auto()
    OFF = auto()
    EQUALS = auto()
    NUMBER = auto()

@dataclass
class Token:
    kind: Type
    value: int | None = None

def tokenize(text: str) -> list[Token]:
    tokens = []
    num_buffer = ""
    pos = 0

    while pos < len(text):
        # Look for the keyword "off"
        if pos + 3 < len(text) and text[pos:pos+3].lower() == "off":
            tokens.append(Token(Type.OFF))
            pos += 3

        # Look for the keyword "on"
        elif pos + 2 < len(text) and text[pos:pos+2].lower() == "on":
            tokens.append(Token(Type.ON))
            pos += 2

        # Check for the "=" character
        elif text[pos] == "=":
            tokens.append(Token(Type.EQUALS))
            pos += 1

        # Process sequences of digits as numbers
        elif text[pos].isdigit():
            while pos < len(text) and text[pos].isdigit():
                num_buffer += text[pos]
                pos += 1
            tokens.append(Token(Type.NUMBER, int(num_buffer)))
            num_buffer = ""
        else:
            pos += 1

    return tokens

def process_tokens(tokens: list[Token]) -> None:
    total = 0
    active = True

    for token in tokens:
        if token.kind == Type.ON:
            active = True
        elif token.kind == Type.OFF:
            active = False
        elif active and token.kind == Type.NUMBER:
            total += token.value
        elif token.kind == Type.EQUALS:
            print(total)

def main():
    input_text = sys.stdin.read()
    token_list = tokenize(input_text)
    process_tokens(token_list)

if __name__ == "__main__":
    main()
