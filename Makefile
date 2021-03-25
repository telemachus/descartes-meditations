SHELL = /bin/sh
LATEXMK = latexmk
FLAGS = -xelatex -bibtex-cond -pdfxe -jobname=descartes

all: descartes

descartes: descartes-titlepage.tex descartes-introduction.tex \
	descartes-background.tex descartes-main.tex descartes.bib \
	synopsis.tex meditatio-prima.tex meditatio-secunda.tex
	$(LATEXMK) $(FLAGS) descartes-main.tex

clean:
	- $(RM) build/*

.PHONY : clean
