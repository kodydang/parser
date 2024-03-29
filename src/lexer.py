import re
import sys

rules = (
    (r"\d+", "NUMBER"),
    (r"\;", "SEMI"),
    (r"\:", "COLON"),
    (r"\,", "COMMA"),
    (r"\.", "DOT"),
    (r"\(", "LPAREN"),
    (r"\)", "RPAREN"),
    (r"\<", "LT"),
    (r"\>", "GT"),
    (r"\=", "EQ"),
    (r"\+", "PLUS"),
    (r"\-", "MINUS"),
    (r"\*", "MULTIPLY"),
    (r"\/", "DIVIDE"),
    (r"\..", "DOTDOT"),
    (r"\:=", "COLEQ"),
    (r"\<=", "LE"),
    (r"\>=", "GE"),
    (r"\<>", "NE"),
    (r"^[a-zA-Z]+[0-9]*", "IDENTIFIER"),
    (r"\d+", "INTCONST"),
    (r"^'[a-zA-Z]{1}'$", "CHARCONST"),
    (r"^'[a-zA-Z]'$", "STRINGCONST"),
    (r"^and$", "AND"),
    (r""),
)
"""
readfile
"""
path = "input.txt"
input = ""
with open("input.txt", "r") as f:
    input = f.read().split()

print(input)
txt = "a<b"
x = re.search(rules[7], txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")


class Lexer:
    def __init__(self, *args, **kwargs):
        self.rule = rules
