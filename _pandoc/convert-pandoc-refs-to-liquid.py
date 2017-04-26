# -*- coding: utf-8 -*-
#
# Originally by Dan McCloy

infile = '../_publications-edit-this-one.md'
outfile = '../publications.md'

with open(infile, 'r') as f, open(outfile, 'w') as g:
	for line in f:
		if '^N^' in line:
			line = line.replace('^N^', '<sup>N</sup>')
		if '[@' in line:
			line = line.replace('[@', '{% reference ')
			line = line.replace('] ', ' %} ')
			line = line.replace(']\n', ' %}\n')
		g.write(line)
