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

#   should set 'umask 002' in the shell
GROUP = adass

umask:
	chgrp -R $(GROUP)
	find . -type d | xargs chmod g+wx
	find . -type f | xargs chmod g+w

#   only for Peter Teuben to push to adass.org and/or our mirror
pjt:
	rsync -av . pteuben@adass.org:/u1/www/htdocs

pjt2:
	ssh lma "cd public_html/adass/www2; git pull"
