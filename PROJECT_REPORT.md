# PROJECT REPORT
## Syntax Highlighter for C Programs

### 1. Introduction
A syntax highlighter is a tool that displays different parts of source code in different colours. This project implements a basic syntax highlighter for the C programming language using Python. It demonstrates the compiler-design phases of lexical analysis and token classification.

### 2. Objectives
- To understand how a lexical analyzer scans source code.
- To identify lexemes and classify them into token categories.
- To generate a readable, colour-coded representation of C source code.
- To understand the role of tokenization in a compiler front end.

### 3. Software Requirements
- Python 3.9 or newer
- Windows, Linux or macOS
- A modern web browser
- A code editor such as VS Code (optional)

### 4. Concepts Used
**Lexical Analysis:** The input source program is read from left to right.

**Token:** A meaningful unit of source code, such as a keyword, identifier, operator or number.

**Lexeme:** The actual character sequence that matches a token, for example `while`, `count` or `42`.

**Token Classification:** Each lexeme is assigned a category. The project recognizes keywords, identifiers, common built-in functions, numeric literals, strings, character literals, comments, operators, punctuation and preprocessor lines.

### 5. System Design / Algorithm
1. Read a C source file.
2. Start scanning at the first character.
3. If whitespace is found, preserve it.
4. If `//` or `/*` is found, read a comment.
5. If a quote is found, read a string or character literal while respecting escape characters.
6. If an identifier begins, read the complete word and check whether it is a keyword or a common library function.
7. If a digit begins, read a numeric literal.
8. Match the longest available operator; otherwise classify punctuation or an unknown character.
9. Convert each classified token into an HTML span with a CSS class.
10. Save the result as a standalone HTML file.

### 6. Implementation
The main implementation is in `src/highlighter.py`. The `tokenize()` function performs lexical analysis and returns token-type/lexeme pairs. The `to_html()` function escapes HTML-sensitive characters and creates a styled HTML document. The command-line interface accepts an input C file and an optional output path.

### 7. How to Execute
Run:

```bash
python src/highlighter.py samples/example.c
```

Open `output/highlighted.html` in a browser to view the highlighted program.

### 8. Testing
Automated tests check:
- Keyword and identifier recognition
- Number and operator recognition
- String and comment recognition
- Safe HTML escaping

Run tests with:

```bash
python -m unittest discover -s tests -v
```

### 9. Expected Outcome
The input C program is displayed in a browser with different colours for different token categories. This makes the program easier to read and demonstrates the working of a basic lexical analyzer.

### 10. Conclusion
The project demonstrates how a compiler's lexical analysis stage identifies and classifies source-code tokens. It provides a simple practical example of compiler front-end concepts.

### 11. Future Scope
- Add more complete C standard-library recognition.
- Add line numbers and a file-upload web interface.
- Report lexical errors and malformed literals.
- Extend token support for additional C language standards.

### 12. References
- Python Documentation: https://docs.python.org/3/
- ISO C language standard (for C lexical elements)
- Compiler Design course notes
