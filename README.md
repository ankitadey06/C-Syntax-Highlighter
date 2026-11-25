# C Syntax Highlighter (Compiler Design PBL)

A small Python project that demonstrates **Lexical Analysis** and **Token Classification**. It reads a C source file, identifies token categories, and creates a standalone HTML page with colour-coded syntax.

## Features
- Recognizes C keywords, identifiers, common library functions, numbers, strings, character literals, comments, operators and punctuation.
- Preserves whitespace and line breaks.
- Generates a standalone HTML preview that opens in a browser.
- Uses only the Python standard library (no third-party packages).
- Includes automated unit tests.

## Requirements
- Python 3.9 or newer
- Any modern web browser

## Run
From the project root:

```bash
python src/highlighter.py samples/example.c
```

The output is written to `output/highlighted.html`. Open that file in a browser.

Choose a custom output path:

```bash
python src/highlighter.py samples/example.c --output my_preview.html
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Compiler Design concepts
1. **Lexical Analysis:** the source is scanned from left to right.
2. **Tokenization:** each lexeme is grouped into a token.
3. **Token Classification:** tokens are assigned categories such as keyword, identifier, number and operator.
4. **Whitespace handling:** whitespace is preserved in the output but is not classified as a visible token.
5. **Code generation:** classified tokens are converted into HTML spans with CSS classes.

## Project structure

```text
C_Syntax_Highlighter_PBL/
├── src/
│   └── highlighter.py
├── samples/
│   └── example.c
├── tests/
│   └── test_highlighter.py
├── output/
├── README.md
├── PROJECT_REPORT.md
└── .gitignore
```

## Limitations
This is an educational lexer, not a complete C compiler. It does not validate C grammar or types. Preprocessor directives are highlighted as one token per line, and the lexer supports common C lexical forms rather than every compiler-specific extension.

## Author
Add your name, roll number, class and institution here before submission.
