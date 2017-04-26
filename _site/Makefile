
cv:
	#cd _pandoc; pandoc --output=pubs-tmp.tex --natbib ../_publications-edit-this-one.md
	cd _pandoc; python pandoc-latex-postprocessor.py foti_cv.tex foti_cv_shell.tex
	#cd _pandoc; python pandoc-latex-postprocessor.py pubs.tex pubs-tmp.tex
	#cd _pandoc; python convert-pandoc-refs-to-liquid.py
	cd _pandoc; sh compile.bash foti_cv.tex
	mv _pandoc/foti_cv.pdf ./
	#cd _pandoc; rm -f pubs.tex foti_cv.* *.pyc

website:
	cd _pandoc; python convert-pandoc-refs-to-liquid.py
	bundle exec jekyll build --verbose
	cd _pandoc; python boldify-my-name-site.py

website-drafts:
	cd _pandoc; python convert-pandoc-refs-to-liquid.py
	bundle exec jekyll build --verbose

build: website
build-drafts: website-drafts

serve: website
	bundle exec jekyll serve --verbose --skip-initial-build

serve-drafts: website-drafts
	bundle exec jekyll serve --drafts --verbose --skip-initial-build

