SHELL = /bin/sh
LATEXMK = latexmk
FLAGS = -xelatex -bibtex-cond

all: descartes

descartes: descartes-titlepage.tex descartes-introduction.tex \
	descartes-background.tex descartes-main.tex descartes.bib \
	meditatio-prima.tex meditatio-secunda.tex
	$(LATEXMK) $(FLAGS) descartes-main.tex -jobname=descartes

clean:
	- $(RM) *.{aux,log,pdf,bbl,blg,fls,fdb_latexmk,end,eledsec*,out,toc}
	- $(RM) descartes.[1-9]
	- $(RM) descartes.[1-9][0-9]
	- $(RM) descartes.bcf
	- $(RM) reled.[A-Z]end

.PHONY : clean
