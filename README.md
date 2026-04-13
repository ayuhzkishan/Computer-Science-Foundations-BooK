# Foundations of Computer Science

A complete LaTeX textbook and lab manual for Computer Science / IT curriculum, designed for early teens (ages 11–14).

## Features
- 8 Parts, 43 Chapters covering Hardware, Software, MS Office, and Internet.
- Rich TikZ diagrams and illustrated tables.
- "Byte" the robot mascot for tips and warnings.
- Step-by-step practical lab activities.
- Professionally typeset with LaTeX.

## Compilation
To compile the book:
1. Ensure you have a LaTeX distribution installed (e.g., MiKTeX or TeX Live).
2. Install necessary packages (fontawesome5, tcolorbox, tikz, etc.).
3. Run:
   ```bash
   pdflatex main.tex
   makeindex main.idx
   pdflatex main.tex
   ```

## Structure
- `main.tex`: Master document.
- `preamble.tex`: Document configuration and custom styles.
- `partX/`: Chapter files grouped by modules.
- `frontmatter/`: Title page, preface, etc.
