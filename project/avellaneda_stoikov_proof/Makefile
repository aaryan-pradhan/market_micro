# The one entry point for the book. Every tool the book needs is called from here.
# Book-specific settings live in book.mk; this file is identical in every book (copied from the euclid-book skill).
#
#   make                  deps (first time only) + build + log gate + order check + VERIFY + open the PDF
#   make build check      the same without VERIFY and without opening (use while writing)
#   make review CH=01     build only chapter 01 and render its pages to build/review/
#   make source P=95-113  render source pages as images to build/source/  (C=name picks SRC_name)
#   make verify           run the book's own number checks (VERIFY in book.mk), if any
#   make test             check.py must pass tests/good and fail each tests/bad-* with its expected message
#   make clean            delete build/
#
# Fails (non-zero exit) on any LaTeX error, undefined reference, overfull box, or check.py violation.

include book.mk

TEX     := pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build
TEXPKGS := tcolorbox tikzfill pdfcol cleveref enumitem environ trimspaces thmtools

.PHONY: all build check verify review source test open clean

all: build check verify open

# TeX packages BasicTeX lacks, installed once per machine into ~/texmf (no sudo).
build/.deps: Makefile
	mkdir -p build/chapters
	tlmgr init-usertree 2>/dev/null || true
	tlmgr --usermode install $(TEXPKGS)
	touch $@

# Run 1 writes aux + index, makeindex sorts the glossary, run 2 typesets the final pages.
build: build/.deps
	$(TEX) main >/dev/null || true
	makeindex -q build/main
	$(TEX) main >/dev/null || (grep -A3 '^!' build/main.log; exit 1)
	@! grep -nE '^!|Warning: (Reference|Citation|Hyper reference).*undefined|undefined references|Overfull' build/main.log || (echo 'build: fix the log lines above'; exit 1)
	@echo "build: ok, $$(grep -o '([0-9]* pages' build/main.log | tr -d '(')"

check:
	BANNED="$(BANNED)" python3 tools/check.py

verify:
	@test -z "$(VERIFY)" || $(VERIFY)

# \includeonly via \only (see main.tex): only chapter CH is typeset; cross-refs come from the full build's aux files.
review: build
	@test -n "$(CH)" || (echo 'usage: make review CH=01'; exit 1)
	ch=$$(ls chapters/$(CH)-*.tex | head -1); ch=$${ch%.tex}; \
	$(TEX) -jobname=review "\def\only{$$ch}\input{main}" >/dev/null && \
	$(TEX) -jobname=review "\def\only{$$ch}\input{main}" >/dev/null
	rm -rf build/review && mkdir -p build/review
	pdftoppm -r 80 -png build/review.pdf build/review/p
	@echo "review: $$(ls build/review | wc -l | tr -d ' ') pages in build/review/"

source:
	@test -n "$(P)" || (echo 'usage: make source P=95-113 [C=name]'; exit 1)
	rm -rf build/source && mkdir -p build/source
	pdftoppm -f $(firstword $(subst -, ,$(P))) -l $(lastword $(subst -, ,$(P))) -r 85 -jpeg -jpegopt quality=75 "$(or $(SRC_$(C)),$(SRC))" build/source/p
	@echo "source: $$(ls build/source | wc -l | tr -d ' ') pages in build/source/"

test:
	@test -d tests || { echo 'test: no tests/ here; they live in the euclid-book skill template'; exit 0; }
	@fail=0; for d in tests/*/; do \
	  out=$$(BANNED=Forbidden python3 tools/check.py $$d); rc=$$?; \
	  if [ -f $$d/expect ]; then [ $$rc = 1 ] && echo "$$out" | grep -qF "$$(cat $$d/expect)"; else [ $$rc = 0 ]; fi \
	    && echo "ok   $$d" || { echo "FAIL $$d: $$out"; fail=1; }; \
	done; exit $$fail

open: build
	open build/main.pdf

clean:
	rm -rf build
