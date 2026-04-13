# agents.md — Antigravity LaTeX Book Generation Instructions
# Target Audience: Early Teens (Ages 11–14) — Visually Rich, Engaging, Fun

---

## Project Overview

Generate a complete, professionally typeset **LaTeX textbook** for a foundational Computer Science / IT curriculum covering Modules 1–8. The book must include:

- Full theory chapters for every module and sub-chapter
- Dedicated lab/practical sections with step-by-step instructions for every listed activity
- A complete front matter (title page, preface, table of contents)
- Back matter (index, glossary)
- **Rich visual elements throughout**: TikZ diagrams, illustrated tables, icon-driven callouts, chapter opener splash panels, infographic-style figures, and fun mascot sidebars — all designed to engage readers aged 11–14

---

## Book Metadata

```latex
\title{\Huge\bfseries\sffamily Foundations of Computer Science\\[0.4em]
       \large A Complete Theory \& Lab Manual}
\author{Computer Science Department}
\date{\the\year}
\subject{Computer Science — Beginner to Intermediate}
\keywords{computers, Windows, MS Word, MS Excel, MS PowerPoint, Internet, hardware, software}
```

---

## LaTeX Document Class and Package Requirements

```latex
\documentclass[12pt, a4paper, twoside, openright]{book}

% --- Essential Packages ---
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage[margin=1in, inner=1.3in, outer=0.9in, top=1.1in, bottom=1.1in]{geometry}

% --- Color & Graphics ---
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{tikzpagenodes}
\usetikzlibrary{
  shapes.geometric, shapes.callouts, shapes.symbols,
  arrows.meta, positioning, fit, backgrounds,
  decorations.pathmorphing, decorations.text,
  shadows.blur, patterns, calc, mindmap, trees,
  matrix, chains
}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepackage{pgf-pie}          % Pie charts in TikZ

% --- Tables ---
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{tabularx}
\usepackage{array}
\usepackage{multirow}
\usepackage{colortbl}         % Colored table rows/columns
\usepackage{hhline}

% --- Lists ---
\usepackage{enumitem}
\usepackage{pifont}           % Dingbat check/cross marks

% --- Code / Shortcuts ---
\usepackage{listings}
\usepackage{fancyvrb}

% --- Headers / Footers ---
\usepackage{fancyhdr}

% --- Hyperlinks & PDF Metadata ---
\usepackage[colorlinks=true, linkcolor=NavyBlue, urlcolor=AccentTeal,
            citecolor=NavyBlue, pdftitle={Foundations of Computer Science},
            bookmarks=true, bookmarksopen=true]{hyperref}

% --- Boxes / Call-outs ---
\usepackage{tcolorbox}
\tcbuselibrary{skins, breakable, listings, poster, fitting, hooks}

% --- Index ---
\usepackage{makeidx}
\makeindex

% --- Glossaries ---
\usepackage[toc, nonumberlist]{glossaries}
\makeglossaries

% --- Chapter / Section Styling ---
\usepackage{titlesec}
\usepackage{titletoc}

% --- Fonts ---
\usepackage{sourcesanspro}    % Clean sans-serif for headings
\usepackage{sourcecodepro}    % Monospace for code/shortcuts
\renewcommand{\familydefault}{\sfdefault}  % Default to sans-serif

% --- Caption ---
\usepackage{caption}
\usepackage{subcaption}
\captionsetup{font=small, labelfont={bf,color=NavyBlue}, skip=4pt}

% --- Icons ---
\usepackage{fontawesome5}

% --- Layout helpers ---
\usepackage{wrapfig}
\usepackage{float}
\usepackage{needspace}
\usepackage{afterpage}
\usepackage{mdframed}
\usepackage{changepage}       % adjustwidth environment
\usepackage{shadow}           % drop shadows on boxes
\usepackage{contour}
\usepackage{soul}             % highlighting with \hl{}
\usepackage{cancel}           % strikethrough
\usepackage{qrcode}           % QR codes for extension links
\usepackage{smartdiagram}     % Easy flow/bubble diagrams
```

---

## Color Palette

Bright, modern, teen-friendly palette. Define in preamble:

```latex
% --- Primary Palette ---
\definecolor{ModuleBlue}{HTML}{1A73E8}
\definecolor{LabGreen}{HTML}{1E8449}
\definecolor{NoteOrange}{HTML}{E67E22}
\definecolor{WarnRed}{HTML}{C0392B}
\definecolor{NavyBlue}{HTML}{1B3A6B}
\definecolor{AccentTeal}{HTML}{00897B}
\definecolor{HeaderBg}{HTML}{EBF5FB}
\definecolor{ShadeGray}{HTML}{F2F3F4}

% --- Teen-Friendly Accent Colors ---
\definecolor{FunPurple}{HTML}{8E44AD}
\definecolor{FunPink}{HTML}{E91E8C}
\definecolor{FunYellow}{HTML}{F4D03F}
\definecolor{FunCoral}{HTML}{FF6B6B}
\definecolor{FunMint}{HTML}{48C9B0}
\definecolor{FunSky}{HTML}{5DADE2}
\definecolor{PartColor1}{HTML}{1A73E8}   % Part I  — Blue
\definecolor{PartColor2}{HTML}{1E8449}   % Part II — Green
\definecolor{PartColor3}{HTML}{8E44AD}   % Part III — Purple
\definecolor{PartColor4}{HTML}{E67E22}   % Part IV  — Orange
\definecolor{PartColor5}{HTML}{C0392B}   % Part V   — Red
\definecolor{PartColor6}{HTML}{00897B}   % Part VI  — Teal
\definecolor{PartColor7}{HTML}{E91E8C}   % Part VII — Pink
\definecolor{PartColor8}{HTML}{1B3A6B}   % Part VIII — Navy

% --- Table Row Alternating ---
\definecolor{RowLight}{HTML}{EBF5FB}
\definecolor{RowDark}{HTML}{D6EAF8}
\definecolor{HeaderRow}{HTML}{1A73E8}
```

---

## Typography & Chapter Styling

```latex
% --- Chapter Title Style (large colored banner) ---
\titleformat{\chapter}[block]
  {\normalfont\huge\bfseries\sffamily}
  {}
  {0pt}
  {%
    \begin{tikzpicture}[remember picture]
      \fill[ModuleBlue] (0,0) rectangle (\linewidth, 1.8cm);
      \node[anchor=west, text=white, font=\huge\bfseries\sffamily]
        at (0.3cm, 0.9cm) {\thechapter\quad};
      \node[anchor=west, text=white, font=\huge\bfseries\sffamily]
        at (1.4cm, 0.9cm) {#1};
    \end{tikzpicture}%
    \vspace{-0.5cm}
  }
\titlespacing*{\chapter}{0pt}{0pt}{20pt}

% --- Section Style ---
\titleformat{\section}
  {\large\bfseries\sffamily\color{NavyBlue}}
  {\thesection}{1em}{}
  [{\color{ModuleBlue}\titlerule[1.5pt]}]

% --- Subsection Style ---
\titleformat{\subsection}
  {\normalsize\bfseries\sffamily\color{AccentTeal}}
  {\thesubsection}{1em}{}

% --- Part Page Style (full-color splash) ---
% Each \part{} page uses a TikZ full-page background in the part's accent color
% See "Part Page Design" section below for per-part TikZ code.

% --- Page Headers ---
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\sffamily\textcolor{NavyBlue}{\leftmark}}
\fancyhead[RO]{\small\sffamily\textcolor{NavyBlue}{\rightmark}}
\fancyfoot[C]{\small\sffamily\textcolor{NavyBlue}{\thepage}}
\renewcommand{\headrulewidth}{1pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{ModuleBlue}\leaders\hrule height\headrulewidth\hfill}}
```

---

## Mascot Character

Introduce **"Byte"** — a friendly robot mascot that appears in sidebars throughout the book offering tips, fun facts, and warnings. Byte appears as a TikZ illustration (simple robot face in a rounded rectangle).

```latex
% --- Byte the Robot Mascot Sidebar ---
% Draw Byte as a simple TikZ robot head in a rounded box
\newcommand{\bytetip}[2][tip]{%
  % #1 = mood: tip | warn | fun | think
  % #2 = text content
  \begin{tcolorbox}[
    enhanced, breakable,
    colback=FunSky!15, colframe=FunSky,
    arc=8pt,
    left=2.5cm, right=6pt, top=6pt, bottom=6pt,
    overlay={
      \begin{scope}[shift={($(frame.west)+(0.4cm,0)$)}]
        % Robot head
        \fill[FunSky!60] (-0.55,-0.65) rectangle (0.55,0.65);
        \fill[white] (-0.55,-0.65) rectangle (0.55,0.65);
        \draw[FunSky, line width=1.5pt, rounded corners=3pt]
          (-0.55,-0.65) rectangle (0.55,0.65);
        % Eyes
        \fill[NavyBlue] (-0.22,0.15) circle (0.1);
        \fill[NavyBlue] (0.22,0.15) circle (0.1);
        % Mouth varies by mood
        \ifthenelse{\equal{#1}{warn}}{%
          \draw[WarnRed, line width=1.5pt] (-0.25,-0.2) -- (0.25,-0.2);
        }{%
          \draw[LabGreen, line width=1.5pt]
            (-0.25,-0.25) .. controls (-0.1,-0.05) and (0.1,-0.05) .. (0.25,-0.25);
        }
        % Antenna
        \draw[NavyBlue, line width=1pt] (0,0.65) -- (0,0.9);
        \fill[FunPink] (0,0.9) circle (0.07);
        % Label
        \node[font=\tiny\bfseries\sffamily, text=NavyBlue] at (0,-0.85) {BYTE};
      \end{scope}
    }
  ]
  \small\sffamily #2
  \end{tcolorbox}
}
```

Use `\bytetip[tip]{...}`, `\bytetip[warn]{...}`, `\bytetip[fun]{...}` throughout every chapter — minimum **2 Byte tips per chapter**.

---

## Custom Environments

### Core Boxes

```latex
% --- Theory Box (blue, for definitions and concepts) ---
\newtcolorbox{theorybox}[1][]{
  enhanced, breakable,
  colback=HeaderBg, colframe=ModuleBlue, arc=6pt,
  fonttitle=\bfseries\sffamily\color{white}, coltitle=white,
  attach boxed title to top left={yshift=-2mm, xshift=8mm},
  boxed title style={colback=ModuleBlue, arc=4pt},
  title={\faBook\ #1},
  left=8pt, right=8pt, top=10pt, bottom=8pt,
  shadow={2mm}{-2mm}{0mm}{black!15}
}

% --- Fun Fact Box (yellow, for interesting trivia) ---
\newtcolorbox{funfact}{
  enhanced, breakable,
  colback=FunYellow!20, colframe=FunYellow!80!black, arc=8pt,
  fonttitle=\bfseries\sffamily,
  title={\faStar\ Did You Know?},
  left=8pt, right=8pt
}

% --- Lab Step Box ---
\newtcolorbox{labstep}[1][]{
  enhanced, breakable,
  colback=LabGreen!5, colframe=LabGreen, arc=6pt,
  fonttitle=\bfseries\sffamily\color{white}, coltitle=white,
  attach boxed title to top left={yshift=-2mm, xshift=8mm},
  boxed title style={colback=LabGreen, arc=4pt},
  title={\faTerminal\ #1},
  left=8pt, right=8pt, top=10pt, bottom=8pt
}

% --- Note Box ---
\newtcolorbox{notebox}{
  enhanced, breakable,
  colback=NoteOrange!10, colframe=NoteOrange, arc=6pt,
  fonttitle=\bfseries\sffamily,
  title={\faInfoCircle\ Note},
  left=8pt, right=8pt
}

% --- Warning Box ---
\newtcolorbox{warnbox}{
  enhanced, breakable,
  colback=WarnRed!8, colframe=WarnRed, arc=6pt,
  fonttitle=\bfseries\sffamily\color{white}, coltitle=white,
  boxed title style={colback=WarnRed},
  attach boxed title to top left={yshift=-2mm, xshift=8mm},
  title={\faExclamationTriangle\ Warning!},
  left=8pt, right=8pt, top=10pt
}

% --- Shortcut Box ---
\newtcolorbox{shortcutbox}{
  enhanced, breakable,
  colback=FunPurple!8, colframe=FunPurple, arc=6pt,
  fonttitle=\bfseries\sffamily\color{white}, coltitle=white,
  boxed title style={colback=FunPurple},
  attach boxed title to top left={yshift=-2mm, xshift=8mm},
  title={\faKeyboard\ Keyboard Shortcuts},
  left=8pt, right=8pt, top=10pt
}

% --- Try It Yourself Box (for quick in-text challenges) ---
\newtcolorbox{tryit}{
  enhanced, breakable,
  colback=FunMint!15, colframe=FunMint!80!black, arc=8pt,
  fonttitle=\bfseries\sffamily,
  title={\faLightbulb\ Try It Yourself!},
  left=8pt, right=8pt
}

% --- Real World Connect Box ---
\newtcolorbox{realworld}{
  enhanced, breakable,
  colback=FunCoral!10, colframe=FunCoral, arc=6pt,
  fonttitle=\bfseries\sffamily\color{white}, coltitle=white,
  boxed title style={colback=FunCoral},
  attach boxed title to top left={yshift=-2mm, xshift=8mm},
  title={\faGlobe\ Real World Connection},
  left=8pt, right=8pt, top=10pt
}

% --- Keyboard Key Style ---
\newcommand{\key}[1]{%
  \tikz[baseline=(K.base)]{
    \node[draw=NavyBlue, fill=ShadeGray, rounded corners=2pt,
          inner sep=2pt, minimum height=16pt, drop shadow,
          font=\ttfamily\small\bfseries] (K) {#1};
  }%
}

% --- Learning Objectives ---
\newenvironment{objectives}{%
  \begin{tcolorbox}[
    enhanced, colback=ModuleBlue!8, colframe=ModuleBlue, arc=8pt,
    title={\faCheckCircle\ Learning Objectives},
    fonttitle=\bfseries\sffamily\color{white}, coltitle=white,
    boxed title style={colback=ModuleBlue},
    attach boxed title to top left={yshift=-2mm, xshift=8mm},
    top=10pt, left=8pt, right=8pt
  ]
  \begin{itemize}[leftmargin=*, label={\textcolor{ModuleBlue}{\faAngleRight}},
                  itemsep=2pt]
}{%
  \end{itemize}\end{tcolorbox}\vspace{4pt}
}

% --- Review Questions ---
\newenvironment{reviewqs}{%
  \vspace{6pt}
  \begin{tcolorbox}[
    enhanced, colback=FunSky!10, colframe=FunSky!80!black, arc=8pt,
    title={\faQuestionCircle\ Review Questions},
    fonttitle=\bfseries\sffamily, top=10pt, left=8pt
  ]
  \begin{enumerate}[label={\textbf{\textcolor{NavyBlue}{Q\arabic*.}}},
                    leftmargin=*, itemsep=4pt]
}{%
  \end{enumerate}\end{tcolorbox}
}

% --- Lab Activity Environment ---
\newenvironment{labactivity}[3]{%
  % #1 = number, #2 = title, #3 = duration (e.g. "10 min")
  \needspace{6\baselineskip}
  \begin{tcolorbox}[
    enhanced, breakable,
    colback=LabGreen!4, colframe=LabGreen, arc=8pt,
    title={\faFlask\ \textbf{Practical #1:} #2 \hfill \faClock\ #3},
    fonttitle=\sffamily\color{white}, coltitle=white,
    boxed title style={colback=LabGreen, arc=4pt},
    attach boxed title to top left={yshift=-2mm, xshift=6mm},
    top=12pt, left=8pt, right=8pt, bottom=8pt
  ]
}{%
  \end{tcolorbox}\vspace{8pt}
}

% --- Mini Challenge (end-of-chapter extension task) ---
\newtcolorbox{challenge}{
  enhanced, breakable,
  colback=FunPink!10, colframe=FunPink, arc=8pt,
  fonttitle=\bfseries\sffamily\color{white}, coltitle=white,
  boxed title style={colback=FunPink},
  attach boxed title to top left={yshift=-2mm, xshift=8mm},
  title={\faTrophy\ Challenge Task},
  left=8pt, right=8pt, top=10pt
}
```

---

## Visual Design Language — Figures, Diagrams, and Tables

> **CRITICAL DESIGN RULE:** Every section must have at least one visual element (TikZ diagram, illustrated table, infographic, or figure). Chapters must never run more than one full page of plain text without a visual break. Use the specifications below for each chapter's required visuals.

---

### Global TikZ Styles (define in preamble)

```latex
\tikzset{
  % Hardware component box
  hwbox/.style={
    draw=NavyBlue, fill=HeaderBg, rounded corners=6pt,
    minimum width=2.5cm, minimum height=1.2cm,
    font=\small\bfseries\sffamily, align=center,
    drop shadow={shadow xshift=1.5pt, shadow yshift=-1.5pt, opacity=0.3}
  },
  % Arrow style
  thickarrow/.style={
    ->, line width=2pt, color=ModuleBlue,
    >=Stealth[round]
  },
  % Flowchart decision
  decision/.style={
    diamond, draw=NoteOrange, fill=FunYellow!30,
    minimum width=3cm, minimum height=1.5cm,
    font=\small\sffamily, align=center
  },
  % Flowchart process
  process/.style={
    rectangle, draw=LabGreen, fill=LabGreen!10,
    rounded corners=4pt, minimum width=3.5cm, minimum height=1cm,
    font=\small\sffamily, align=center
  },
  % Flowchart terminal
  terminal/.style={
    rounded rectangle, draw=NavyBlue, fill=NavyBlue!10,
    minimum width=3.5cm, minimum height=1cm,
    font=\small\sffamily\bfseries, align=center
  },
  % Icon label node
  iconlabel/.style={
    circle, draw=ModuleBlue, fill=ModuleBlue, text=white,
    font=\bfseries\sffamily, minimum size=0.7cm, inner sep=0
  },
  % Comparison column header
  colhead/.style={
    fill=NavyBlue, text=white, font=\bfseries\sffamily\small,
    minimum height=0.8cm, align=center
  },
  % Step circle
  stepcircle/.style={
    circle, draw=LabGreen, fill=LabGreen, text=white,
    font=\bfseries\sffamily\small, minimum size=0.6cm, inner sep=0
  },
}
```

---

## Part Page Design

Each `\part{}` must use a **full-page TikZ splash** as the part title page. Generate the following TikZ template and apply with the correct `PartColor` per part:

```latex
% Template for part title pages — use \partpage{PartColorN}{Roman Numeral}{Part Title}{Tagline}{icon-list}
\newcommand{\partpage}[5]{%
  \clearpage
  \thispagestyle{empty}
  \begin{tikzpicture}[remember picture, overlay]
    % Full background gradient
    \fill[#1] (current page.south west) rectangle (current page.north east);
    \fill[#1!70!black, opacity=0.5]
      (current page.south west) -- ++(0, 8cm) --
      (current page.north east) -- cycle;
    % Decorative circles
    \foreach \r/\op in {6/0.08, 9/0.05, 12/0.03}{
      \fill[white, opacity=\op]
        ($(current page.north east)+(-3cm,-3cm)$) circle (\r cm);
    }
    % Part number
    \node[text=white, opacity=0.15, font=\fontsize{180}{180}\selectfont\bfseries]
      at ($(current page.center)+(4cm, 0)$) {#2};
    % "Part" label
    \node[text=white, font=\Large\sffamily, opacity=0.9]
      at ($(current page.center)+(-2cm, 3.5cm)$) {PART #2};
    % Title
    \node[text=white, font=\Huge\bfseries\sffamily, align=left,
          text width=14cm, anchor=west]
      at ($(current page.west)+(2cm, 0.5cm)$) {#3};
    % Tagline
    \node[text=white!80, font=\large\sffamily\itshape, align=left,
          text width=12cm, anchor=west]
      at ($(current page.west)+(2cm, -1.5cm)$) {#4};
    % Bottom strip
    \fill[white, opacity=0.1]
      (current page.south west) rectangle ++(21cm, 2.5cm);
    \node[text=white, font=\sffamily\small]
      at ($(current page.south)+(0, 1.2cm)$) {#5};
  \end{tikzpicture}
  \clearpage
}
```

Call example for Part I:
```latex
\partpage{PartColor1}{I}{Getting Started\\with Computers}
  {Discover what computers are, how they work, and why they matter in your world.}
  {\faDesktop\ Hardware \quad \faKeyboard\ Input \quad \faDisplay\ Output \quad \faMicrochip\ CPU \quad \faCode\ Software}
```

---

## Chapter-by-Chapter Visual Specifications

### PART I — Getting Started with Computers

---

#### Chapter 1: Introduction to Computers

**Chapter Opener:** TikZ illustration of a student at a computer desk with a speech bubble "What IS this thing?"

**Required Visuals:**

1. **Figure 1.1 — "What Is a Computer?" Analogy Diagram** (TikZ)
   Draw a 3-column comparison strip:
   - Column A: Human brain icon + label "Thinks"
   - Column B: Lightning bolt (speed) + clock (timing) + lock (accuracy)
   - Column C: Computer icon + label "Processes Data"
   Connect with double-headed arrow. Use `hwbox` style.

2. **Figure 1.2 — Characteristics of a Computer** (TikZ radial burst)
   Central node: large circle "COMPUTER" in ModuleBlue.
   Six radiating nodes (each in a different `PartColor`):
   Speed | Accuracy | Storage | Diligence | Versatility | Automation
   Each node has a small FontAwesome icon above its label.

3. **Table 1.1 — Computers in Daily Life** (colortbl styled)
   ```
   | \rowcolor{HeaderRow}\color{white}Where | \color{white}What We Use It For | \color{white}Example |
   | School   | Writing assignments    | MS Word           |
   | Home     | Entertainment         | YouTube, Games    |
   | Bank     | Transactions          | ATM, Online Bank  |
   | Hospital | Patient records       | Medical software  |
   | Shop     | Billing & inventory   | POS system        |
   ```
   Alternate rows with `RowLight`/`RowDark`. Add a relevant FontAwesome icon in the "Where" column.

4. **Byte Tip:** "Did you know the first computer was the size of a whole room? Now your phone is more powerful!" (`\bytetip[fun]{...}`)

---

#### Chapter 2: Parts of a Computer

**Required Visuals:**

1. **Figure 2.1 — Labeled Computer Setup** (TikZ)
   Draw a simplified desktop workstation from front view:
   - Tall rectangle = CPU tower (label with arrow: "CPU / System Unit")
   - Wide rectangle = Monitor (label: "Monitor — Output Device")
   - Small rectangle below monitor = Keyboard (label: "Keyboard — Input Device")
   - Small oval beside keyboard = Mouse (label: "Mouse — Input Device")
   - Small rectangle top-right = Speakers (label: "Speakers — Output Device")
   Use `hwbox` style for each component. Draw connecting lines (cables) in gray dashed.
   Use `\draw[thickarrow]` for all labels.

2. **Figure 2.2 — Hardware vs Software** (TikZ two-column split panel)
   Left half (ModuleBlue background):
   - Heading "HARDWARE" with \faServer icon
   - Bullet icons: Monitor, Keyboard, Mouse, Printer, RAM chip
   Right half (LabGreen background):
   - Heading "SOFTWARE" with \faCode icon
   - Bullet icons: Windows logo text, MS Word, Paint, Calculator
   Center dividing line with double-headed arrow labeled "Work Together"

3. **Table 2.1 — Input vs Output Devices**
   Two-column comparison with colored headers:
   ```
   | \cellcolor{ModuleBlue}\color{white}\faHandPointer\ Input Devices |
     \cellcolor{LabGreen}\color{white}\faEye\ Output Devices |
   | Keyboard    | Monitor   |
   | Mouse       | Printer   |
   | Scanner     | Speakers  |
   | Microphone  | Projector |
   | Webcam      | Headphones|
   ```

4. **Byte Tip:** "The CPU is like the brain of the computer — it does ALL the thinking!" (`\bytetip[tip]{...}`)

---

#### Chapter 3: Types of Computers

**Required Visuals:**

1. **Figure 3.1 — Types of Computers Visual Cards** (TikZ 2×2 grid)
   Four rounded-rectangle "cards", each with:
   - Large FontAwesome icon (fa-desktop, fa-laptop, fa-tablet, fa-mobile)
   - Bold name
   - 2-line description
   - Color: PartColor1, PartColor3, PartColor6, PartColor7 respectively

2. **Table 3.1 — Computer Comparison Table**
   ```
   | Feature      | Desktop  | Laptop  | Tablet  | Smartphone |
   |--------------|----------|---------|---------|------------|
   | Portability  | Low      | Medium  | High    | Very High  |
   | Screen Size  | Large    | Medium  | Medium  | Small      |
   | Performance  | High     | Medium  | Medium  | Low-Medium |
   | Battery      | No       | Yes     | Yes     | Yes        |
   | Best For     | School lab| Travel | Reading | Calling    |
   ```
   Use alternating row colors. Add ✓/✗ symbols using `\ding{51}`/`\ding{55}` where appropriate.

3. **Byte Tip:** "Smartphones are computers too! They just fit in your pocket." (`\bytetip[fun]{...}`)

---

#### Chapter 4: Basics of Software

**Required Visuals:**

1. **Figure 4.1 — Software Types Pyramid** (TikZ)
   Draw a two-level pyramid:
   - Bottom layer (wide, NavyBlue): "System Software — The Foundation"
     Sub-labels: Windows | Linux | macOS | Android
   - Top layer (narrower, ModuleBlue): "Application Software — What You Use"
     Sub-labels: MS Word | Paint | Games | Calculator
   - Arrow from bottom to top: "System Software runs first, then App Software loads"

2. **Figure 4.2 — Hardware + Software = Magic!** (TikZ equation diagram)
   Three nodes in a row:
   Node 1 (hwbox): \faMicrochip\ Hardware
   "+" sign in FunPink
   Node 2 (hwbox, LabGreen): \faCode\ Software
   "=" sign in FunYellow
   Node 3 (hwbox, FunPurple): \faStar\ Working Computer!

3. **Table 4.1 — Common Software Examples**
   ```
   | Type               | Name          | What It Does            |
   |--------------------|---------------|-------------------------|
   | System Software    | Windows 11    | Manages the computer    |
   | System Software    | Android       | Runs your smartphone    |
   | Application        | MS Word       | Word processing         |
   | Application        | MS Paint      | Drawing & editing       |
   | Application        | Calculator    | Math operations         |
   | Application        | Chrome        | Browse the internet      |
   ```

---

#### Chapter 5: Computer Lab Rules & Safety

**Required Visuals:**

1. **Figure 5.1 — Correct Sitting Posture** (TikZ)
   Draw a side-view silhouette of a person seated at a desk:
   - Straight back (highlight spine line in LabGreen)
   - Feet flat on floor (dotted line + label)
   - Eyes level with screen top (horizontal dotted line)
   - Elbows at 90° (arc + label)
   - Wrists straight (label)
   Annotate each point with a short arrow + label. Use `warnbox` for "Bad Posture" side note.

2. **Figure 5.2 — Lab Rules Infographic** (TikZ 3×2 icon grid)
   Six rule tiles, each with:
   - Large colored circle background
   - FontAwesome icon (\faUtensils crossed out, \faVolumeOff, \faBroom, \faPowerOff correct, \faHandsWash, \faMobileAlt crossed out)
   - 1-line rule text below
   Colors: alternate FunCoral and FunMint tiles.

3. **Warnbox:** "Never force-pull cables or plug in USB drives the wrong way around — always check the connector shape first!"

---

#### Lab Chapter for Part I — Practicals 1–6

Each practical uses the `labactivity` environment with three arguments: number, title, duration.

```latex
\begin{labactivity}{1}{Identifying Computer Parts}{10 min}
  \textbf{Objective:} Identify the main parts of a computer by name and function.\\[4pt]
  \textbf{Materials:} Real computer OR printed A3 image of a computer setup; identification worksheet.\\[4pt]
  \textbf{Steps:}
  \begin{enumerate}[label=\protect\stepcircle{\arabic*}, leftmargin=2cm, itemsep=4pt]
    \item Look at the computer (or image) on your desk.
    \item Point to and name each part your teacher asks about.
    \item Fill in the \emph{Parts Identification Worksheet} — draw a line from each label to the correct part.
    \item Answer: Is a keyboard an input or output device?
    \item Answer: What does the monitor display?
  \end{enumerate}
  \textbf{Expected Outcome:} Students correctly label Monitor, CPU, Keyboard, Mouse on the worksheet.
\end{labactivity}
```

> Note: `\stepcircle` is a TikZ inline numbered circle — define as:
> ```latex
> \newcommand{\stepcircle}[1]{%
>   \tikz[baseline=-0.6ex]\node[stepcircle]{#1};}
> ```

**Include for each of the 6 practicals:**
- A small **"You Will Need" icon strip** at the top (TikZ row of icons: computer icon, timer icon, worksheet icon)
- A **"Step Map"** — horizontal TikZ chain of step-circles connected by arrows, showing the flow at a glance before the detailed steps
- A **"Well Done!" badge** TikZ stamp at the bottom (star shape in FunYellow with text "Practical Complete!")

**Figure P1.1 — Step Map for Practical 3 (Mouse Practice)** example:
```tikz
% Chain: Click → Double-Click → Right-Click → Drag & Drop
\node[stepcircle] (s1) {1};
\node[process, right=0.4cm of s1] (l1) {Single Click};
\draw[thickarrow] (s1) -- (l1);
% ... continue for all steps
```

---

### PART II — Windows Operating System

---

#### Chapter 6: Introduction to Operating Systems

**Required Visuals:**

1. **Figure 6.1 — OS as a Bridge** (TikZ layered diagram)
   Three horizontal layers stacked:
   - Bottom layer (NavyBlue): "Hardware — CPU, RAM, Storage"
   - Middle layer (ModuleBlue, slightly wider): "Operating System — The Bridge"
     (with small bridge graphic elements: arches in lighter blue)
   - Top layer (AccentTeal): "Application Software — Word, Chrome, Games"
   Two-headed arrows between each layer. Label the middle: "OS manages communication."

2. **Figure 6.2 — Windows Version Timeline** (TikZ horizontal timeline)
   A horizontal line with circular nodes at:
   XP (2001) → Vista (2007) → 7 (2009) → 8 (2012) → 10 (2015) → 11 (2021)
   Each node: colored circle + version name + year.
   Alternate colors: FunSky, FunMint, FunPurple, FunCoral, ModuleBlue, LabGreen.
   Below each node: one key feature in italic small text.

3. **Table 6.1 — OS Functions Summary**
   ```
   | \faIcon\ Function      | What the OS Does                   | Example             |
   |------------------------|------------------------------------|---------------------|
   | \faMicrochip Memory    | Manages RAM allocation             | Opens Chrome        |
   | \faHdd Storage         | Reads/writes files                 | Saves a document    |
   | \faDisplay Interface   | Shows you the desktop              | Icons, Start Menu   |
   | \faNetworkWired Network| Connects to the Internet           | Wi-Fi management    |
   | \faShield Security     | Protects against viruses           | Windows Defender    |
   ```

---

#### Chapter 7: Starting and Shutting Down Windows

**Required Visuals:**

1. **Figure 7.1 — Boot Process Flowchart** (TikZ flowchart)
   Vertical flowchart with these nodes:
   ```
   [Press Power Button] → [POST Check — Hardware OK?]
        ↓ YES                        ↓ NO
   [BIOS/UEFI Loads]         [Error Beep / Message]
        ↓
   [OS Loads from Storage]
        ↓
   [Login Screen Appears]
        ↓
   [Desktop Ready!]
   ```
   Use `terminal` style for start/end, `process` for steps, `decision` for the YES/NO diamond.
   Color the YES path LabGreen and NO path WarnRed.

2. **Figure 7.2 — Shutdown Options Comparison** (TikZ 3-card strip)
   Three side-by-side cards:
   - Card 1 (FunCoral): \faPowerOff\ **Shut Down** — "Turns off completely. Use at end of day."
   - Card 2 (FunYellow!80!black): \faRedo\ **Restart** — "Turns off then on. Use to apply updates."
   - Card 3 (FunSky): \faBed\ **Sleep** — "Low power mode. Use for short breaks."

---

#### Chapter 8: Windows Desktop Environment

**Required Visuals:**

1. **Figure 8.1 — Annotated Desktop Screenshot Recreation** (TikZ)
   Recreate the Windows desktop as a TikZ drawing:
   - Large rectangle (light blue/gray fill) = screen
   - Bottom strip (NavyBlue fill) = Taskbar
   - Small square bottom-left = Start Button (circle with Windows-like grid)
   - Bottom-right strip = System Tray (clock, Wi-Fi, volume icons)
   - Several small squares on desktop = icons (with labels)
   - Small rectangle top-center = open window title bar
   Draw arrows from each element to a label box outside the screen rectangle.

2. **Table 8.1 — Desktop Elements Quick Reference**
   ```
   | Element          | Icon | What It Does                        |
   |------------------|------|-------------------------------------|
   | Desktop          | \faDesktop | Main working area             |
   | Taskbar          | \faMinus   | Shows open programs           |
   | Start Menu       | \faWindows | Opens apps and settings       |
   | Icons            | \faFolder  | Shortcuts to files/programs   |
   | Notification Area| \faBell    | Alerts and system info        |
   | Recycle Bin      | \faTrash   | Deleted files go here         |
   ```

---

#### Chapter 9: File and Folder Management

**Required Visuals:**

1. **Figure 9.1 — File and Folder Hierarchy Tree** (TikZ tree)
   ```
   Documents (folder)
   ├── School (folder)
   │   ├── Maths.docx (file)
   │   └── Science.docx (file)
   ├── Photos (folder)
   │   └── Holiday.jpg (file)
   └── MyStory.txt (file)
   ```
   Draw using TikZ `forest`-style nodes or manual `child` nodes. Folder nodes = FunYellow rounded rect. File nodes = white rect with document corner fold. Lines in NavyBlue.

2. **Figure 9.2 — File Operations Step Map** (TikZ horizontal process chain)
   Six process boxes in sequence:
   Create → Open → Edit → Save → Copy/Move → Delete
   Each box in a different color. Arrows between them.

3. **Table 9.1 — Valid vs Invalid File Names**
   Two-column table:
   ```
   | \textcolor{LabGreen}{\faCheck} Valid Names | \textcolor{WarnRed}{\faTimes} Invalid Names |
   |---------------------------------------------|----------------------------------------------|
   | MyReport                                    | My/Report (slash not allowed)               |
   | Science_Notes_2024                          | File:Name (colon not allowed)               |
   | Chapter 1 Draft                             | CON (reserved name in Windows)              |
   | photo_holiday                               | file* (asterisk not allowed)                |
   ```

4. **Byte Tip (warn):** "Never delete files from the Windows or System32 folder. This can break your computer!"

---

#### Chapter 10: Using Windows Applications

**Required Visuals:**

1. **Figure 10.1 — Applications Overview Cards** (TikZ 2×2 grid)
   Four app cards (Notepad, WordPad, Paint, Calculator) each with:
   - App icon (drawn simply in TikZ or FontAwesome)
   - Name in bold
   - One-sentence description
   - "Best for:" tag at bottom

2. **Figure 10.2 — Paint Toolbar Diagram** (TikZ)
   Draw a simplified horizontal Paint toolbar rectangle.
   Label key sections: Selection tools | Drawing tools | Shapes | Color palette | Eraser
   Arrows from each section pointing up to labels.

---

#### Chapters 11–15 (Control Panel, Storage, Internet, Security, Troubleshooting)

**Required Visuals (one per chapter):**

- **Ch 11 — Figure 11.1:** TikZ diagram of Control Panel categories as a 3×3 grid of icon tiles (System, Display, Date/Time, Printers, Network, User Accounts, Security, Sound, Programs). Each tile: colored background + FontAwesome icon + label.

- **Ch 12 — Figure 12.1:** TikZ storage device comparison chart (horizontal bar chart using pgfplots) showing typical capacities: USB 4GB | DVD 4.7GB | USB 64GB | HDD 1TB | SSD 512GB | Cloud Unlimited. Color each bar differently.

- **Ch 12 — Table 12.1:** Storage device comparison table:
  ```
  | Device    | Type      | Capacity   | Speed  | Portable |
  |-----------|-----------|------------|--------|----------|
  | HDD       | Magnetic  | 500GB–4TB  | Medium | No       |
  | SSD       | Flash     | 128GB–2TB  | Fast   | No       |
  | USB Drive | Flash     | 4GB–256GB  | Medium | Yes      |
  | DVD       | Optical   | 4.7GB      | Slow   | Yes      |
  | Cloud     | Online    | Unlimited  | Varies | Yes      |
  ```

- **Ch 14 — Figure 14.1 — Password Strength Meter:** TikZ horizontal bar:
  Red zone (Weak) | Orange (Fair) | Yellow (Good) | Green (Strong)
  With example passwords plotted on the bar:
  "abc" → Red | "pass123" → Orange | "My$chool2024" → Green

- **Ch 15 — Figure 15.1 — Troubleshooting Flowchart** (TikZ):
  ```
  [Problem Occurs]
       ↓
  [Try Restarting the App]
       ↓ Still broken?
  [Restart the Computer]
       ↓ Still broken?
  [Check All Cable Connections]
       ↓ Still broken?
  [Ask Your Teacher / IT Support]
  ```

---

#### Lab Chapter for Part II — Practicals 1–8

All 8 lab activities follow the same `labactivity` 3-argument format. Each includes:
- You Will Need strip (TikZ icon row)
- Step Map (TikZ horizontal chain)
- At least one embedded screenshot recreation or diagram
- Well Done badge

**Additional Figure for Lab Practical 3 (File/Folder Operations):**
TikZ "before and after" two-panel diagram showing file explorer state before operations vs. after (with new folder, renamed folder, and deleted file shown).

---

### PART III — Computer Basics and Shortcuts

---

#### Chapter 16: Advanced Computer Concepts

**Required Visuals:**

1. **Figure 16.1 — Real-Life Applications Infographic** (TikZ mindmap)
   Central node: "Computers in the Real World"
   Five branches in five colors:
   - Education: Online classes, e-books, assignments
   - Banking: ATMs, online transfers, statements
   - Healthcare: Patient records, scans, prescriptions
   - Entertainment: Streaming, gaming, music
   - Transport: GPS, ticket booking, traffic lights

2. **Table 16.1 — Real-Life Applications Table**
   Domain | Computer Application | Software/Device Used
   (5 rows, one per domain, alternating row colors)

---

#### Chapter 17: Hardware in Detail

**Required Visuals:**

1. **Figure 17.1 — Inside the CPU** (TikZ block diagram)
   Large rectangle labeled "CPU":
   - Left half: box labeled "ALU (Arithmetic Logic Unit)" with \faCalculator icon and note "Does all maths & logic"
   - Right half: box labeled "Control Unit (CU)" with \faDirections icon and note "Directs all operations"
   - Bottom: small box "Registers — Ultra-fast tiny storage"
   Arrows from each unit pointing to/from "RAM" box outside CPU rectangle.

2. **Figure 17.2 — RAM vs ROM Comparison** (TikZ two-panel split)
   Panel A (FunSky): RAM
   - Icon: \faDatabase
   - Volatile (data lost on power off)
   - Temporary storage
   - Example: 8GB RAM
   Panel B (FunPurple): ROM
   - Icon: \faLock
   - Non-volatile (data stays forever)
   - Permanent instructions
   - Example: BIOS chip
   Center: Venn overlap = "Both are types of memory inside the computer"

3. **Table 17.1 — Storage Device Specs**
   (expanded version of Table 12.1 with read/write speed examples)

---

#### Chapter 21: Keyboard and Mouse Skills

**Required Visuals:**

1. **Figure 21.1 — Keyboard Map** (TikZ)
   Draw a simplified keyboard layout (QWERTY) as a TikZ grid of rounded rectangles.
   Color-code key groups:
   - Function keys (F1–F12): FunPurple
   - Number row: FunSky
   - QWERTY rows: ShadeGray
   - Modifier keys (Ctrl/Alt/Shift/Win): FunCoral
   - Navigation keys (arrows, Home, End): FunMint
   - Enter/Backspace/Delete: FunYellow!80!black
   Include a color legend below the keyboard.

2. **Figure 21.2 — Mouse Anatomy** (TikZ)
   Draw an oval mouse shape from top view:
   - Left section: "Left Button — Click & Select"
   - Right section: "Right Button — Context Menu"
   - Center scroll wheel: "Scroll Wheel — Scroll up/down"
   Use arrows and labels. Add a side view showing underside with optical sensor labeled.

3. **Table 21.1 — Mouse Actions**
   ```
   | Action        | How To Do It             | What Happens             |
   |---------------|--------------------------|--------------------------|
   | Single Click  | Press left button once   | Selects item             |
   | Double Click  | Press left button twice  | Opens item               |
   | Right Click   | Press right button once  | Opens context menu       |
   | Click & Drag  | Hold left, move mouse    | Moves or selects area    |
   | Scroll        | Roll scroll wheel        | Page moves up or down    |
   ```

---

#### Chapter 22: Keyboard Shortcuts

**Required Visuals:**

1. **Figure 22.1 — Shortcuts Visual Cheat Sheet** (TikZ poster grid)
   4×4 grid of shortcut tiles. Each tile:
   - Colored background (rotate through 6 accent colors)
   - `\key{Ctrl}` + `\key{C}` rendered as styled key caps
   - Action label: "Copy"
   - Small relevant icon
   Layout:

   | Ctrl+C Copy | Ctrl+V Paste | Ctrl+X Cut | Ctrl+Z Undo |
   | Ctrl+Y Redo | Ctrl+S Save | Ctrl+A Select All | Ctrl+F Find |
   | Ctrl+P Print | Ctrl+N New | Ctrl+O Open | Ctrl+W Close |
   | Alt+Tab Switch | Win+D Desktop | Win+E Explorer | Win+L Lock |

2. **Figure 22.2 — Time Saved With Shortcuts** (pgfplots bar chart)
   Horizontal bar chart comparing:
   - Mouse click method: ~5 seconds
   - Keyboard shortcut: ~0.5 seconds
   For tasks: Copy/Paste, Save, Undo, Select All
   Label bars with time values. Title: "Shortcuts Save Time!"

---

#### Lab Chapter for Part III — Practicals 1–6

Each practical includes the full visual treatment. Additional specific figure:

**Figure L3.5 — Shortcuts Practice Worksheet Layout** (TikZ):
A grid of 8 blank shortcut tiles where students fill in the shortcut and action. Pre-filled example tile shown in corner.

---

### PART IV — Microsoft Word

---

#### Chapter 23: Introduction to MS Word

**Required Visuals:**

1. **Figure 23.1 — MS Word Window Diagram** (TikZ full-width)
   Recreate the MS Word interface as TikZ rectangles:
   - Thin top strip (NavyBlue): Title Bar — "Document1 — Microsoft Word"
   - Strip below (ModuleBlue gradient): Quick Access Toolbar (left) + Tab names (Home, Insert, Layout...) (center)
   - Wide strip (HeaderBg): Ribbon — show Home tab with icons for B/I/U, font selector, alignment buttons
   - Thin strip below ribbon: Ruler (with indent markers)
   - Large white area: Document Area with blinking cursor line
   - Bottom strip (ShadeGray): Status Bar — Page 1/1, Word Count, Zoom slider
   Draw labeled arrows from every element to an annotation outside the window frame.

2. **Figure 23.2 — File Operations Quick Reference** (TikZ 4-card horizontal strip)
   Four cards: New (\key{Ctrl+N}) | Open (\key{Ctrl+O}) | Save (\key{Ctrl+S}) | Save As (\key{F12})
   Each card: icon + shortcut badge + one-line description.

---

#### Chapter 25: Formatting in MS Word

**Required Visuals:**

1. **Figure 25.1 — Text Alignment Visual Demo** (TikZ)
   Four side-by-side panels, each showing a miniature paragraph of dummy text:
   - Panel A (Left): lines flush left, ragged right
   - Panel B (Center): lines centered
   - Panel C (Right): lines flush right, ragged left
   - Panel D (Justify): lines flush both sides
   Label each panel with its name and shortcut key.

2. **Figure 25.2 — Font Formatting Examples** (tcolorbox visual grid)
   Six tiles showing same word "Computer" in:
   - Normal | **Bold** | *Italic* | <u>Underline</u> | ~~Strikethrough~~ | SMALL CAPS
   Each tile in a different color, with the keyboard shortcut below.

3. **Table 25.1 — Line Spacing Options**
   ```
   | Spacing | Value | When To Use                  |
   |---------|-------|------------------------------|
   | Single  | 1.0   | Compact notes                |
   | 1.5     | 1.5   | Most school assignments      |
   | Double  | 2.0   | Essays (teacher can annotate)|
   ```

---

#### Chapter 26: Inserting Elements

**Required Visuals:**

1. **Figure 26.1 — Table Anatomy** (TikZ)
   Draw a 3×3 table with labels:
   - "Row" label with horizontal bracket
   - "Column" label with vertical bracket
   - "Cell" label pointing to one cell
   - "Border/Gridline" pointing to a line
   One cell highlighted in FunYellow to indicate selected cell.

2. **Figure 26.2 — Insert Tab Visual Map** (TikZ)
   Recreate the Insert tab ribbon as a TikZ strip divided into groups:
   Pages | Tables | Pictures | Illustrations | Header & Footer | Text | Symbols
   Each group: labeled bracket below + 2–3 representative icons above.

---

#### Chapter 27: Page Layout and Printing

**Required Visuals:**

1. **Figure 27.1 — Portrait vs Landscape** (TikZ)
   Two rectangles side by side:
   - Left: tall rectangle (Portrait) with text lines + label "Portrait — Best for: Letters, Reports"
   - Right: wide rectangle (Landscape) with text columns + label "Landscape — Best for: Tables, Charts"
   Each rectangle has margin indicators (dashed inner border with measurement arrows).

2. **Figure 27.2 — Margin Diagram** (TikZ)
   Single page rectangle with:
   - Top/Bottom/Left/Right margin regions shaded in FunSky!20
   - Center white area = printable area
   - Measurement arrows on each margin labeled "Top: 1 inch", etc.

---

#### Lab Chapter for Part IV — Practicals 1–8

**Additional Visual — Lab Practical 4 (Text Formatting):**
TikZ "Before and After" two-panel: left panel shows plain unformatted text; right panel shows same text with bold heading, colored subtitle, and justified body text.

**Additional Visual — Lab Practical 6 (Inserting Elements):**
TikZ annotated document mock-up showing positions of: inserted picture (top right), inserted shape (bottom left), inserted table (center), WordArt title (top).

---

### PART V — Microsoft Excel

---

#### Chapter 28: Introduction to MS Excel

**Required Visuals:**

1. **Figure 28.1 — Excel Window Diagram** (TikZ full-width)
   Similar to Word window diagram but Excel-specific:
   - Name Box (top-left of sheet area) — "A1"
   - Formula Bar — "=SUM(A1:A5)"
   - Column headers (A, B, C...) in ModuleBlue strip
   - Row numbers (1, 2, 3...) in NavyBlue strip
   - Cell grid (alternating RowLight/white for first few visible rows)
   - Sheet tabs at bottom (Sheet1, Sheet2, Sheet3) in FunSky
   - Status bar at very bottom
   Label every element with arrows.

2. **Figure 28.2 — Cell Address Explained** (TikZ)
   Zoom-in on a 4×4 cell grid.
   Highlight cell C3 in FunYellow.
   Draw two arrows: one pointing to column C header labeled "Column Letter = C", one pointing to row 3 label "Row Number = 3".
   Speech bubble from highlighted cell: "My address is C3!"

---

#### Chapter 31: Formulas and Functions

**Required Visuals:**

1. **Figure 31.1 — Anatomy of a Formula** (TikZ)
   Draw the text: `=SUM(B2:B6)` in large monospace font.
   Label each part with a colored arrow:
   - `=` → "Always start with equals sign"
   - `SUM` → "Function name (tells Excel what to do)"
   - `(` → "Opening bracket"
   - `B2:B6` → "Range of cells (B2 through B6)"
   - `)` → "Closing bracket"

2. **Figure 31.2 — Functions Comparison Cards** (TikZ 5-card strip)
   Five cards for SUM | AVERAGE | MIN | MAX | COUNT.
   Each card:
   - Function name in bold
   - Syntax: `=SUM(range)`
   - Example: `=SUM(A1:A5)` → `15`
   - Icon: \faPlus, \faDivide, \faArrowDown, \faArrowUp, \faHashtag

3. **Figure 31.3 — Fill Handle Demo** (TikZ)
   Show cells A1:A6. A1=1, A2=2, A3–A6 shown being filled (with dashed border + fill handle square at bottom right). Arrow labeled "Drag down to fill series automatically."

4. **Table 31.1 — Common Functions Reference**
   ```
   | Function | What It Does          | Example           | Result |
   |----------|-----------------------|-------------------|--------|
   | SUM      | Adds all values       | =SUM(A1:A5)       | 50     |
   | AVERAGE  | Finds the mean        | =AVERAGE(A1:A5)   | 10     |
   | MIN      | Finds smallest value  | =MIN(A1:A5)       | 2      |
   | MAX      | Finds largest value   | =MAX(A1:A5)       | 18     |
   | COUNT    | Counts numeric cells  | =COUNT(A1:A5)     | 5      |
   ```

---

#### Chapter 32: Charts and Data Management

**Required Visuals:**

1. **Figure 32.1 — Chart Type Guide** (TikZ 3-panel with mini charts)
   Three panels side by side:
   - Bar Chart panel: small pgfplots bar chart with 3 bars + label "Bar Chart — Compare categories"
   - Line Chart panel: pgfplots line chart + label "Line Chart — Show trends over time"
   - Pie Chart panel: pgf-pie simple pie + label "Pie Chart — Show parts of a whole"

2. **Figure 32.2 — Sorting Illustrated** (TikZ before/after)
   Two small Excel grid snippets:
   - Before: names in random order (Alice, Zara, Bob, Mia)
   - Arrow labeled "Sort A→Z"
   - After: names alphabetically sorted (Alice, Bob, Mia, Zara)
   Highlight sorted column in FunMint.

---

#### Lab Chapter for Part V — Practicals 1–8

**Additional Visual — Lab Practical 5 (Formulas):**
TikZ annotated spreadsheet showing: data in B2:B6, SUM formula in B7, result shown, formula bar at top displaying `=SUM(B2:B6)`. All elements labeled.

**Additional Visual — Lab Practical 7 (Charts):**
pgfplots bar chart showing sample student marks (3 students × 3 subjects) as the expected output of the practical.

---

### PART VI — Microsoft PowerPoint

---

#### Chapter 33: Introduction to PowerPoint

**Required Visuals:**

1. **Figure 33.1 — PowerPoint Interface Diagram** (TikZ full-width)
   Recreate PowerPoint window:
   - Top: Title bar + Ribbon with Tabs (Home, Insert, Design, Transitions, Animations, Slide Show)
   - Left panel: Slide panel showing 3 thumbnail slides (rectangles with slide number)
   - Center: Current slide editing area (large rectangle)
   - Bottom: Notes panel (smaller rectangle with placeholder text)
   - Bottom-right: View buttons + Zoom slider
   All elements labeled with arrows.

2. **Figure 33.2 — Slide Layouts Gallery** (TikZ 2×3 mini-slide grid)
   Six slide layout thumbnails drawn as small rectangles:
   - Title Slide: large title area + subtitle area
   - Title and Content: top title bar + large content box
   - Two Content: title + two side-by-side content boxes
   - Title Only: just a title bar
   - Blank: empty
   - Picture with Caption: image box + caption box
   Label each thumbnail below.

---

#### Chapter 36: Animation and Transitions

**Required Visuals:**

1. **Figure 36.1 — Animation Types** (TikZ 4-card strip)
   Four cards:
   - Entrance (FunMint): \faSignInAlt icon — "Object flies onto the slide"
   - Emphasis (FunYellow): \faStar icon — "Object pulses or spins"
   - Exit (FunCoral): \faSignOutAlt icon — "Object flies off the slide"
   - Motion Path (FunSky): \faRoute icon — "Object moves along a custom path"

2. **Figure 36.2 — Transition vs Animation** (TikZ comparison)
   Two rows:
   - Top: Two slides with a wavy arrow between them labeled "TRANSITION — Between slides"
   - Bottom: One slide with elements inside flying in, labeled "ANIMATION — Within one slide"

---

#### Lab Chapter for Part VI — Practicals 1–8

**Additional Visual — Lab Practical 3 (Text and Design):**
TikZ before/after: left = bland white slide with no formatting; right = same slide with a theme applied, colored title, and styled bullet points.

**Additional Visual — Lab Practical 6 (Animations):**
TikZ animation timeline diagram — horizontal strip showing: Slide appears → Title animates (0.5s) → Bullet 1 appears (1s) → Bullet 2 appears (1.5s). Color-coded timeline bars.

---

### PART VII — Internet and Browsers

---

#### Chapter 38: Introduction to the Internet

**Required Visuals:**

1. **Figure 38.1 — How the Internet Works** (TikZ network diagram)
   Draw several devices (laptop, phone, desktop) connected by lines to a central cloud shape labeled "The Internet."
   Beyond the cloud: Web server icons, email server icon, social media icon.
   Packets shown as small envelopes traveling along the lines.
   Label: ISP (Internet Service Provider) between home device and cloud.

2. **Figure 38.2 — Internet vs WWW** (TikZ Venn-style)
   Large outer circle (ModuleBlue): "The Internet — the global network of cables, routers, and computers"
   Smaller inner circle (AccentTeal): "The World Wide Web — websites and web pages that live ON the internet"
   Outside both circles: "Email, Online Games, Video Calls — also use the Internet, but are NOT the Web"

3. **Table 38.1 — Internet Uses Table**
   ```
   | Category      | \faIcon  | Example                     |
   |---------------|----------|-----------------------------|
   | Education     | \faBook  | Online lessons, YouTube      |
   | Communication | \faEnvelope | Email, WhatsApp           |
   | Entertainment | \faFilm  | Netflix, online games        |
   | Shopping      | \faShoppingCart | Amazon, online stores  |
   | Information   | \faSearch | Google, Wikipedia           |
   | Banking       | \faUniversity | Online banking, UPI    |
   ```

---

#### Chapter 39: Introduction to Web Browsers

**Required Visuals:**

1. **Figure 39.1 — Browser vs Search Engine** (TikZ comparison)
   Two-panel split:
   - Left (FunSky): Browser — "The vehicle (like a car)"
     Examples: Chrome, Firefox, Edge
     Role: Takes you to websites
   - Right (FunCoral): Search Engine — "The GPS (helps you find where to go)"
     Examples: Google, Bing, DuckDuckGo
     Role: Finds websites for you
   Center: \faCar icon with GPS icon, and the label: "You need BOTH!"

---

#### Chapter 40: Using a Browser

**Required Visuals:**

1. **Figure 40.1 — Browser Window Anatomy** (TikZ full-width)
   Recreate a browser window:
   - Top bar: \faChevronLeft \faChevronRight \faRedo (Back, Forward, Refresh) + address bar showing "https://www.example.com" + \faLock padlock + \faStar bookmark icon + \faEllipsisV settings
   - Tab strip below: Tab 1 (active, white), Tab 2 (gray), + New Tab button
   - Main content area: simple webpage layout
   Label every element with arrows.

2. **Figure 40.2 — URL Anatomy** (TikZ)
   Large text: `https://www.wikipedia.org/wiki/Computer`
   Color-code and bracket each part:
   - `https://` → "Protocol — secure connection"
   - `www.` → "Subdomain"
   - `wikipedia.org` → "Domain name — the website's address"
   - `/wiki/Computer` → "Page path — specific page on the site"

---

#### Chapter 41: Searching the Internet

**Required Visuals:**

1. **Figure 41.1 — Good vs Bad Search Keywords** (TikZ comparison table)
   Three rows:
   ```
   | \faTimes\ Bad Query          | \faCheck\ Better Query            |
   |------------------------------|-----------------------------------|
   | "computer"                   | "how does a CPU work for students"|
   | "help"                       | "MS Word how to insert table"     |
   | "planet"                     | "solar system planets facts kids" |
   ```
   Bad column in WarnRed background, Better column in LabGreen background.

2. **Figure 41.2 — Anatomy of a Search Results Page** (TikZ)
   Recreate a Google results page mockup:
   - Top: Search bar
   - First result: Blue title link + green URL + 2 lines description — label: "Organic Result"
   - Small "Ad" badge result above it — label: "Paid Advertisement"
   - Right side box — label: "Featured Snippet / Knowledge Panel"

---

#### Chapter 42: Safe Internet Use

**Required Visuals:**

1. **Figure 42.1 — Password Strength Ladder** (TikZ)
   Vertical ladder with 4 rungs:
   - Rung 1 (WarnRed): "Weak — 'abc123'" → Can be cracked in seconds
   - Rung 2 (NoteOrange): "Fair — 'password1'" → Can be cracked in minutes
   - Rung 3 (FunYellow!80!black): "Good — 'MyDog!2024'" → Takes hours/days
   - Rung 4 (LabGreen): "Strong — 'T!ger@Sk3wl#99'" → Very hard to crack
   Each rung has a time-to-crack estimate and a strength bar.

2. **Figure 42.2 — Phishing Warning Infographic** (TikZ)
   A fake email mockup with red warning overlays pointing to:
   - Strange sender address — "Not the real company!"
   - Urgent language — "Act now!" — "Red flag!"
   - Suspicious link — "Hover before clicking!"
   - Request for password — "Legitimate sites NEVER ask for your password via email!"

3. **Table 42.1 — Online Safety Rules (Netiquette)**
   ```
   | # | Rule                              | Why It Matters              |
   |---|-----------------------------------|-----------------------------|
   | 1 | Be kind and respectful online     | Your words affect real people|
   | 2 | Don't share personal info          | Protect your privacy         |
   | 3 | Think before you post             | The internet never forgets   |
   | 4 | Don't share others' photos        | Respect their privacy        |
   | 5 | Report cyberbullying              | Keep the internet safe       |
   ```

---

#### Lab Chapter for Part VII — Practicals 1–6

All 6 practicals follow the standard `labactivity` format.

**Additional Visual — Lab Practical 4 (Effective Searching):**
TikZ table showing search query refinement steps with result counts (illustrative):
- "animals" → ~2 billion results
- "endangered animals" → ~50 million results
- "endangered animals India 2024" → ~500,000 results
- "endangered animals India 2024 site:.gov" → ~5,000 results
Arrow-chain showing refinement process.

---

### PART VIII — Capstone Project

---

#### Chapter 43: Mini Project — Bringing It All Together

**Required Visuals:**

1. **Figure 43.1 — Project Folder Structure** (TikZ tree diagram)
   ```
   MyProject (root folder)
   ├── Documents
   │   └── MyReport.docx
   ├── Spreadsheets
   │   └── MyData.xlsx
   ├── Presentations
   │   └── MySlides.pptx
   └── Research
       └── InternetFindings.docx
   ```
   Draw as TikZ tree with folder icons in FunYellow and file icons in white.

2. **Figure 43.2 — Project Timeline** (TikZ Gantt-style)
   Horizontal timeline showing suggested time allocation:
   - Session 1: Folder structure + Word document (30 min)
   - Session 2: Excel spreadsheet + chart (30 min)
   - Session 3: PowerPoint presentation (30 min)
   - Session 4: Internet research + final check (20 min)
   - Session 5: Presentation to teacher (10 min)
   Each bar in a different PartColor.

3. **Table 43.1 — Full Rubric** (`longtable`, booktabs style)
   ```
   | Component        | Criteria                                      | Marks |
   |------------------|-----------------------------------------------|-------|
   | Folder Structure | Named correctly, logical hierarchy             | 10    |
   | Word Document    | Formatting, table, image all correct           | 20    |
   | Excel Sheet      | Data, 3 functions (SUM/AVERAGE/COUNT), 1 chart | 25   |
   | PowerPoint       | 5+ slides, transition, animation, notes        | 25    |
   | Internet Report  | Relevant content, source cited                 | 10    |
   | Demo/Presentation| Student explains their work clearly            | 10    |
   | \textbf{Total}   |                                               | \textbf{100} |
   ```
   Header row: `\rowcolor{NavyBlue}\color{white}`. Alternate rows with RowLight/RowDark. Last row bold in AccentTeal.

4. **Figure 43.3 — Assessment Checklist** (tcolorbox with checkboxes)
   A printable checklist formatted as a `tcolorbox` with the following items, each preceded by `$\square$`:
   - [ ] Folder structure created with correct names
   - [ ] Word document formatted (font, alignment, bold/italic)
   - [ ] Word document has at least one table and one image
   - [ ] Excel spreadsheet has data for at least 5 rows
   - [ ] Excel spreadsheet uses SUM, AVERAGE, and one other function
   - [ ] Excel has a chart (bar or pie)
   - [ ] PowerPoint has 5 or more slides
   - [ ] PowerPoint has at least one transition applied
   - [ ] PowerPoint has at least one animation applied
   - [ ] Speaker notes added to at least 2 slides
   - [ ] Internet research saved with source URL noted
   - [ ] Student is ready to explain their project

5. **Byte Tip (fun):** "You've learned SO much! From turning on a computer to building your own project — you're basically a tech wizard now! 🎉" (`\bytetip[fun]{...}`)

---

## Front Matter Content

### Title Page Design (TikZ full-page)

```latex
% titlepage.tex
\begin{tikzpicture}[remember picture, overlay]
  % Background
  \fill[NavyBlue] (current page.south west) rectangle (current page.north east);
  % Top decorative band
  \fill[ModuleBlue] (current page.north west) rectangle
    ++(21cm, -4cm);
  % Circuit board decorative pattern (repeat small TikZ dots and lines)
  \foreach \x in {1,2,...,20}{
    \foreach \y in {1,2,3}{
      \fill[white, opacity=0.05]
        (\x cm - 0.5, \paperheight - \y cm) circle (2pt);
    }
  }
  % Bottom accent
  \fill[AccentTeal] (current page.south west) rectangle ++(21cm, 2cm);
  % Book title
  \node[text=white, font=\fontsize{32}{38}\selectfont\bfseries\sffamily,
        align=center, text width=16cm]
    at ($(current page.center)+(0, 3cm)$)
    {Foundations of\\Computer Science};
  % Subtitle
  \node[text=FunMint, font=\Large\sffamily\itshape]
    at ($(current page.center)+(0, 1cm)$)
    {A Complete Theory \& Lab Manual};
  % Big Byte mascot illustration (TikZ robot, larger version)
  % ... [draw enlarged Byte robot at center-right of page]
  % Module icons strip
  \foreach \icon/\label/\x in {
    \faDesktop/Computers/2,
    \faWindows/Windows/4.5,
    \faKeyboard/Shortcuts/7,
    \faFileWord/Word/9.5,
    \faFileExcel/Excel/12,
    \faFilePowerpoint/PowerPoint/14.5,
    \faGlobe/Internet/17,
    \faTrophy/Project/19.5}{
      \node[text=white, font=\scriptsize\sffamily, align=center]
        at ($(current page.south)+(\x cm - 10.5cm, 3.5cm)$)
        {\Large\icon\\[2pt]\label};
  }
\end{tikzpicture}
```

### Preface

Generate 4 paragraphs:
1. Welcome addressed directly to the student: "Welcome to your Computer Science adventure!" — conversational tone.
2. What the book covers and how each module builds on the last.
3. The theory–shortcut–lab structure explained with reference to the Byte mascot.
4. Encouragement: "Don't worry about getting everything right the first time. Experiment, make mistakes, and learn — that's exactly how real computer scientists work!"

### How to Use This Book

Include a **TikZ legend/guide panel** showing each box type with its color, icon, and purpose:
- theorybox → "Learn the concept"
- funfact → "Cool trivia"
- notebox → "Important note"
- warnbox → "Be careful!"
- shortcutbox → "Save time with shortcuts"
- tryit → "Quick hands-on challenge"
- bytetip → "Byte's advice"
- labactivity → "Full practical activity"
- challenge → "Extra challenge"

---

## Back Matter

### Glossary

All 40+ terms defined in full. Include in the glossary header a **TikZ alphabet index strip** (A–Z across a horizontal band, each letter in a small colored tile) for quick navigation.

### Index

All key terms indexed. Include `\index{hardware}`, `\index{software}`, `\index{shortcut!keyboard}` etc. with sub-entries where appropriate.

---

## Formatting and Style Rules (Updated for Teen Audience)

1. **Every chapter opens** with a TikZ "chapter splash panel" — a full-width colored strip with the chapter number, title, and a relevant icon.
2. **Every chapter begins** with an `objectives` box and a `\bytetip` welcome.
3. **Every chapter ends** with a `reviewqs` box AND a `challenge` task AND a `funfact`.
4. **No more than one full page of unbroken text** — insert a figure, table, or callout box if approaching this limit.
5. **All tables** use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`) + `colortbl` alternating rows.
6. **All keyboard shortcuts** use `\key{}` (styled TikZ key cap, not plain `\texttt`).
7. **Byte mascot** appears minimum **2× per chapter** — vary moods (tip, warn, fun, think).
8. **Lab practicals** include: You-Will-Need strip | Step Map | numbered steps with `\stepcircle` | Expected Outcome | Well Done badge.
9. **Part pages** are full-color TikZ splash pages.
10. **Section headings** use `\titleformat` with `\color{NavyBlue}` and an underline rule.
11. **Figures** always have captions in `\small\sffamily` with colored label prefix.
12. **Fun language** — use occasional "Cool!", "Wait, what?", "Remember this!" as informal section starters in callout boxes.
13. **QR codes** (using `qrcode` package): add at the end of each Part pointing to a teacher-curated extension resource URL (placeholder URL `https://example.com/module1` etc.).
14. Use `\ding{51}` (✓) and `\ding{55}` (✗) from `pifont` for Yes/No comparisons.
15. Use `\hl{important phrase}` from `soul` package to highlight key terms inline in yellow.

---

## File Output Specification

```
book/
├── main.tex
├── preamble.tex
├── assets/
│   └── tikz_styles.tex        % All reusable TikZ styles and macros
├── frontmatter/
│   ├── titlepage.tex          % Full-page TikZ title
│   ├── preface.tex
│   └── howto.tex              % How to Use This Book (with legend diagram)
├── part1/
│   ├── partpage.tex           % Part I TikZ splash page
│   ├── ch01_intro.tex
│   ├── ch02_parts.tex
│   ├── ch03_types.tex
│   ├── ch04_software.tex
│   ├── ch05_lab_rules.tex
│   └── ch_lab1.tex
├── part2/
│   ├── partpage.tex
│   ├── ch06_os_intro.tex
│   ├── ch07_startup.tex
│   ├── ch08_desktop.tex
│   ├── ch09_files.tex
│   ├── ch10_apps.tex
│   ├── ch11_control_panel.tex
│   ├── ch12_storage.tex
│   ├── ch13_internet_win.tex
│   ├── ch14_security.tex
│   ├── ch15_troubleshoot.tex
│   └── ch_lab2.tex
├── part3/
│   ├── partpage.tex
│   ├── ch16_advanced.tex
│   ├── ch17_hardware.tex
│   ├── ch18_software.tex
│   ├── ch19_os.tex
│   ├── ch20_files_adv.tex
│   ├── ch21_keyboard.tex
│   ├── ch22_shortcuts.tex
│   └── ch_lab3.tex
├── part4/
│   ├── partpage.tex
│   ├── ch23_word_intro.tex
│   ├── ch24_word_editing.tex
│   ├── ch25_word_format.tex
│   ├── ch26_word_insert.tex
│   ├── ch27_word_layout.tex
│   └── ch_lab4.tex
├── part5/
│   ├── partpage.tex
│   ├── ch28_excel_intro.tex
│   ├── ch29_excel_worksheets.tex
│   ├── ch30_excel_format.tex
│   ├── ch31_excel_formulas.tex
│   ├── ch32_excel_charts.tex
│   └── ch_lab5.tex
├── part6/
│   ├── partpage.tex
│   ├── ch33_ppt_basics.tex
│   ├── ch34_ppt_design.tex
│   ├── ch35_ppt_visuals.tex
│   ├── ch36_ppt_anim.tex
│   ├── ch37_ppt_deliver.tex
│   └── ch_lab6.tex
├── part7/
│   ├── partpage.tex
│   ├── ch38_internet_intro.tex
│   ├── ch39_browsers.tex
│   ├── ch40_browser_use.tex
│   ├── ch41_search.tex
│   ├── ch42_safe.tex
│   └── ch_lab7.tex
├── part8/
│   ├── partpage.tex
│   └── ch43_capstone.tex
└── backmatter/
    ├── glossary.tex
    └── index_entries.tex
```

---

## Complete Visual Inventory (Summary)

Every visual below must be generated. Total: **60+ TikZ diagrams + 30+ tables + 8 part splash pages + mascot appearances throughout**.

| Module | Figures | Tables | Byte Tips | Lab Step Maps |
|--------|---------|--------|-----------|---------------|
| 1 — Computers | 5 | 3 | 10+ | 6 |
| 2 — Windows | 8 | 5 | 16+ | 8 |
| 3 — Shortcuts | 5 | 4 | 12+ | 6 |
| 4 — Word | 6 | 3 | 10+ | 8 |
| 5 — Excel | 7 | 4 | 10+ | 8 |
| 6 — PowerPoint | 5 | 2 | 10+ | 8 |
| 7 — Internet | 8 | 4 | 12+ | 6 |
| 8 — Capstone | 3 | 1 | 2+ | — |
| **Total** | **47+** | **26+** | **82+** | **50** |

---

## Build Instructions

```bash
# Full build sequence (run from book/ directory):
pdflatex -shell-escape main.tex   # -shell-escape needed for some TikZ externalization
makeglossaries main
makeindex main.idx
pdflatex -shell-escape main.tex
pdflatex -shell-escape main.tex   # Third pass resolves all cross-references and TOC

# Optional: externalize TikZ figures for faster rebuilds
# Add to preamble: \usetikzlibrary{external} \tikzexternalize[prefix=tikz-cache/]
mkdir -p tikz-cache
```

Recommended engine: **pdflatex** with `-shell-escape`. XeLaTeX acceptable if system fonts required.

---

## Quality Checklist Before Output

### Content
- [ ] Every chapter has `objectives`, at least 2 `\bytetip`, at least 1 `funfact`, `reviewqs`, and a `challenge` task
- [ ] Every section has at least one visual element
- [ ] No page runs >1 full page of unbroken prose
- [ ] All 50+ lab practicals include: Duration, Objective, Materials, Step Map, Numbered Steps, Expected Outcome, Well Done badge
- [ ] Byte mascot appears in every chapter (minimum 2×)
- [ ] QR code present at end of each Part

### Technical LaTeX
- [ ] Every `\ref{}` has a corresponding `\label{}`
- [ ] Every `\begin{}` has a matching `\end{}`
- [ ] All custom macros defined in `preamble.tex` before first use
- [ ] `tikz_styles.tex` loaded via `\input{assets/tikz_styles}` in preamble
- [ ] All `colortbl` table rows sum to correct column count
- [ ] `\index{}` on every bolded key term
- [ ] Glossary compiles with `makeglossaries`
- [ ] `\stepcircle` macro defined before first lab chapter
- [ ] `qrcode` package installed and URLs are valid placeholders
- [ ] `pgf-pie` package available for pie chart figures
- [ ] `soul` package `\hl{}` does not conflict with colored backgrounds (test in tcolorbox)
- [ ] Part splash pages use `\thispagestyle{empty}` and `\cleardoublepage`
- [ ] Font package `sourcesanspro` and `sourcecodepro` installed (or fallback to `helvet` + `courier`)
