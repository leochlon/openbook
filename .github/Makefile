.PHONY: build clean help
help:
@echo "LaTeX Book Build System"
@echo ""
@echo "make build  - Build PDF"
@echo "make clean  - Remove artifacts"
build:
xelatex -interaction=nonstopmode main.tex
biber main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
clean:
rm -f *.aux *.log *.out *.toc *.bbl *.blg *.bcf *.run.xml *.fls .fdb_latexmk
rm -f chapters/**/.aux
