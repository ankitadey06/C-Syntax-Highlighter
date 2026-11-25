"""A lightweight lexical analyzer and HTML syntax highlighter for C source code."""
from __future__ import annotations
import argparse
import html
from pathlib import Path

KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "inline", "int", "long", "register", "restrict", "return", "short",
    "signed", "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while", "_Bool", "_Complex", "_Imaginary"
}
BUILTINS = {"printf", "scanf", "malloc", "calloc", "realloc", "free", "strlen",
            "strcpy", "strcmp", "sqrt", "pow", "fopen", "fclose"}
OPERATORS = (
    ">>=", "<<=", "++", "--", "->", "&&", "||", "<=", ">=", "==", "!=",
    "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<", ">>",
    "+", "-", "*", "/", "%", "=", "<", ">", "!", "&", "|", "^", "~",
    "?", ":", ".", "#"
)
PUNCTUATION = set("(){}[];,")
COLORS = {
    "keyword": "#c792ea", "identifier": "#e5e9f0", "builtin": "#82aaff",
    "number": "#f78c6c", "string": "#c3e88d", "char": "#c3e88d",
    "comment": "#697386", "operator": "#89ddff",
    "punctuation": "#f0c674", "preprocessor": "#ffcb6b",
    "unknown": "#ff5370"
}

def tokenize(source: str):
    """Return (token_type, token_text) pairs using a left-to-right lexer."""
    tokens = []
    i, n = 0, len(source)

    def add(kind, start, end):
        tokens.append((kind, source[start:end]))

    while i < n:
        start = i
        ch = source[i]

        if ch.isspace():
            while i < n and source[i].isspace():
                i += 1
            add("whitespace", start, i)
        elif source.startswith("//", i):
            i += 2
            while i < n and source[i] != "\n":
                i += 1
            add("comment", start, i)
        elif source.startswith("/*", i):
            i += 2
            while i < n and not source.startswith("*/", i):
                i += 1
            i = min(n, i + 2) if i < n else n
            add("comment", start, i)
        elif ch == "#" and (i == 0 or source[source.rfind("\n", 0, i) + 1:i].strip() == ""):
            while i < n and source[i] != "\n":
                i += 1
            add("preprocessor", start, i)
        elif ch in ('"', "'"):
            quote = ch
            i += 1
            while i < n:
                if source[i] == "\\":
                    i = min(n, i + 2)
                elif source[i] == quote:
                    i += 1
                    break
                else:
                    i += 1
            add("string" if quote == '"' else "char", start, i)
        elif ch.isalpha() or ch == "_":
            i += 1
            while i < n and (source[i].isalnum() or source[i] == "_"):
                i += 1
            word = source[start:i]
            kind = "keyword" if word in KEYWORDS else ("builtin" if word in BUILTINS else "identifier")
            add(kind, start, i)
        elif ch.isdigit():
            i += 1
            while i < n and (source[i].isalnum() or source[i] in "._"):
                i += 1
            add("number", start, i)
        else:
            operator = next((op for op in OPERATORS if source.startswith(op, i)), None)
            if operator:
                i += len(operator)
                add("operator", start, i)
            elif ch in PUNCTUATION:
                i += 1
                add("punctuation", start, i)
            else:
                i += 1
                add("unknown", start, i)
    return tokens

def to_html(source: str, title: str = "C Syntax Highlighter") -> str:
    """Convert source code into a standalone, styled HTML page."""
    pieces = []
    for kind, value in tokenize(source):
        escaped = html.escape(value)
        if kind in COLORS:
            pieces.append(f'<span class="{kind}">{escaped}</span>')
        else:
            pieces.append(escaped)
    body = "".join(pieces)
    css = "\n".join(f".{name} {{ color: {color}; }}" for name, color in COLORS.items())
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
body {{ margin: 0; padding: 28px; background: #10151f; color: #e5e9f0;
       font-family: Arial, sans-serif; }}
h1 {{ color: #89ddff; font-size: 22px; }}
.editor {{ background: #1b2330; border: 1px solid #354052; border-radius: 10px;
          padding: 22px; overflow-x: auto; }}
pre {{ margin: 0; white-space: pre; tab-size: 4; }}
code {{ font: 14px/1.7 Consolas, "Courier New", monospace; }}
{css}
.legend {{ margin-top: 18px; display: flex; flex-wrap: wrap; gap: 14px;
          font-size: 13px; color: #c5cedb; }}
</style>
</head>
<body>
<h1> C Program — Syntax Highlighting Preview </h1>
<div class="editor"><pre><code>{body}</code></pre></div>
<div class="legend">
<span class="keyword">Keywords</span><span class="builtin">Built-ins</span>
<span class="identifier">Identifiers</span><span class="number">Numbers</span>
<span class="string">Strings</span><span class="comment">Comments</span>
<span class="operator">Operators</span><span class="preprocessor">Preprocessor</span>
</div>
</body>
</html>"""

def main():
    parser = argparse.ArgumentParser(description="Highlight C source code in a browser.")
    parser.add_argument("input", help="Path to a .c source file")
    parser.add_argument("-o", "--output", default="output/highlighted.html",
                        help="HTML output path (default: output/highlighted.html)")
    args = parser.parse_args()
    source_path = Path(args.input)
    if not source_path.is_file():
        parser.error(f"Input file not found: {source_path}")
    source = source_path.read_text(encoding="utf-8")
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(to_html(source, source_path.name), encoding="utf-8")
    print(f"Successfully highlighted {source_path} -> {output_path}")
    print("Open the HTML file in any modern web browser.")

if __name__ == "__main__":
    main()
