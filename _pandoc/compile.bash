#! /bin/bash
#
# Originally by Dan McCloy

texbin="/Library/Tex/texbin"

${texbin}/xelatex -shell-escape $1
${texbin}/bibtex8 $(basename $1 .tex)
mv foti_cv.bbl foti_cv.bbl.bak
python boldify-my-name.py
${texbin}/xelatex -shell-escape $1
${texbin}/xelatex -shell-escape $1
${texbin}/xelatex -shell-escape $1
bn=$(basename $1 .tex)
for ext in .aux .ent .fff .log .lof .lol .lot .toc .blg .bbl .out .pyg .ttt; do
    if [ -f "$bn$ext" ]; then
        rm "$bn$ext"
    fi
done
