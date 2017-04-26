# -*- coding: utf-8 -*-
#
# Originally by Dan McCloy

import sys

#infile = './foti_cv_shell.tex'
#outfile = './foti_cv.tex'
infile = sys.argv[2]
outfile = sys.argv[1]

with open(infile, 'r') as f, open(outfile, 'w') as g:
	for line in f:
		# give full references, not in-text cites
		line = line.replace('\\citep', '\\bibentry')
		# don't number sections:
		#line = line.replace('\\section{', '\\section*{')
		#line = line.replace('\\subsection{', '\\subsection*{')
		# pandoc generates this, don't remember why I object to it
		line = line.replace('\itemsep1pt\parskip0pt\parsep0pt', '')
		# italicize the '-er' suffix
		line = line.replace('{-er}', '\\emph{–er}')
		# convert bold to smallcaps. DANGER! Very fragile, side effects likely.
        # foti: this didn't work for me
		#if '\\textbf{' in line:
		#	line = line.replace('\\textbf{', '\\textbf{\\MakeLowercase{\osf ')
		#	line = line.replace('}', '}}')
		# allow line breaking at the hyphens
		line = line.replace('re-Proto-Indo-European', 're\-/Proto\-/Indo\-/European')
		# avoid italics crashing in LABS^N
		line = line.replace('\\textsuperscript{N}', '\\thinspace\\textsuperscript{N}')
		# remove indent before bullets
		line = line.replace('\\begin{itemize}', '\\begin{itemize}[leftmargin=*]')
		if '../' in line:
			line = line.replace('../bib/foti.bib', 'http://nfoti.github.io/bib/foti.bib')
			line = line.replace('../pubs', 'http://nfoti.github.io/pubs')
		g.write(line)
