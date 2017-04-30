

infile = "../_site/publications.html"
outfile = "../_site/pubs.html.tmp"

with open(infile, 'r') as f, open(outfile, 'w') as g:
    for line in f:
        line = line.replace('Foti, N. J.', '<span style="font-weight:bold">Foti, N. J.</span>')
        g.write(line)
