"""Checks for the book (run by `make`). Each rule here is a lesson from LESSONS.md made mechanical.

Walks the chapters in \\include order (from main.tex) and reports:
  1. a term used in prose before its \\dfn{term};
  2. a \\ref/\\cref/\\Cref to a \\label that appears later (a forward reference);
  3. a box (definition, theorem, example, ...) whose body opens with a list: it renders beside the title;
  4. an expectation \\E without a subscript: every E names what it averages over.
  5. a source name (env BANNED, set in book.mk) in chapter text: the book carries no source references.
The front matter (00-*), the 'whatfor' preview boxes, the 'question' boxes and the 'sayit' (interview pitch) boxes are skipped: they look ahead on purpose.
Exit code 1 if anything is found.  Run:  python3 tools/check.py [book-root]   (default: this repo)
"""
import os, re, sys, pathlib

root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
order = re.findall(r'\\include\{([^}]+)\}', re.sub(r'(?<!\\)%.*', '', (root / 'main.tex').read_text()))
chapters = [c for c in order if not pathlib.Path(c).name.startswith('00')]

def clean(text):
    text = re.sub(r'(?<!\\)%.*', '', text)                                   # comments
    text = re.sub(r'\\begin\{(whatfor|question|sayit|lstlisting)\}.*?\\end\{\1\}', '', text, flags=re.S)  # code is not prose
    text = re.sub(r'\\(code|texttt)\{(?:[^{}]|\{[^{}]*\})*\}', '', text)
    return re.sub(r'\\(chapter|section|subsection|sources)\*?\{[^}]*\}', '', text)  # titles, sources

docs = [(c, clean((root / f'{c}.tex').read_text())) for c in chapters]
full = ''.join(t for _, t in docs)
where = []                                                                     # char offset -> chapter
for c, t in docs: where += [c] * len(t)

# prose view for term checks: blank out labels, refs and box titles (same length, so offsets still line up)
blank = lambda m: ' ' * len(m.group(0))
prose = re.sub(r'\\(label|[cC]?ref)\{[^}]*\}|\\begin\{[a-z]+\}\[[^\]]*\]', blank, full)

errors = []
for m in re.finditer(r'\\dfn\{((?:[^{}]|\{[^{}]*\})+)\}', prose):   # one level of nested braces: \dfn{I/\allowbreak{}O}
    term = re.sub(r'\\[a-zA-Z]+|[{}$]', '', m.group(1)).strip()
    if not term: continue
    use = re.search(r'\b' + re.escape(term) + r'(s|es)?\b', prose[:m.start()], re.I)
    if use:
        ctx = ' '.join(prose[max(0, use.start() - 40):use.end() + 20].split())
        errors.append(f'{where[use.start()]}: "{term}" used before its definition ... {ctx} ...')

seen = set()
for m in re.finditer(r'\\label\{([^}]+)\}|\\[cC]?ref\{([^}]+)\}', full):
    if m.group(1): seen.add(m.group(1)); continue
    for lab in m.group(2).split(','):
        if lab.strip() not in seen:
            errors.append(f'{where[m.start()]}: forward reference to "{lab.strip()}"')

box = r'\\begin\{(definition|theorem|result|lemma|corollary|example|remark)\}(\[[^\]]*\])?\s*(\\label\{[^}]*\}\s*)?\\begin\{(itemize|enumerate|steps)\}'
for m in re.finditer(box, full):
    errors.append(f'{where[m.start()]}: {m.group(1)} opens with a list; add a lead sentence first')

for m in re.finditer(r'\\E(?![a-zA-Z_])', full):
    line = full[:m.start()].count('\n')  # approximate; context printed instead
    ctx = ' '.join(full[max(0, m.start() - 30):m.end() + 25].split())
    errors.append(f'{where[m.start()]}: \\E without a subscript ... {ctx} ...')

for w in os.environ.get('BANNED', '').split():
    for m in re.finditer(r'\b' + re.escape(w) + r'\b', full):
        errors.append(f'{where[m.start()]}: source name "{w}" in the text; remove it')

print('\n'.join(errors) or 'check: 0 violations')
sys.exit(1 if errors else 0)
