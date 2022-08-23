#
#   ADASS web page management
#

URL1 = https://adass.org
URL2 = https://www.astro.umd.edu/~teuben/adass/www2/
URL3 = https://github.com/teuben/www2

help:
	@echo no help
	@echo URL1=$(URL1)
	@echo URL2=$(URL2)
	@echo URL3=$(URL3)

GROUP = adass

umask:
	chgrp -R $(GROUP)
	chmod -R g+w *.html
	find . -type d | xargs chmod g+wx
	find . -type f | xargs chmod g+w

#   only for Peter Teuben.
pjt:
	(cd ..; rsync -av www2 pteuben@adass.org:/u1/www/htdocs)
