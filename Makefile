SHELL = /bin/sh
LATEXMK = latexmk
FLAGS = -xelatex

all: descartes

descartes: descartes-titlepage.tex descartes-introduction.tex \
	descartes-text.tex descartes-commentary.tex descartes.bib \
	descartes-background.tex descartes-main.tex
	$(LATEXMK) $(FLAGS) descartes-main.tex -jobname=descartes

babel: babel-main.tex babel-text.tex
	$(LATEXMK) $(FLAGS) babel-main.tex -jobname=babel

clean:
	- $(RM) *.{aux,log,pdf,bbl,blg,fls,1,fdb_latexmk,end,eledsec1,out,toc}

.PHONY : clean
