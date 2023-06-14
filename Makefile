#
#   ADASS web page management
#

URL1 = https://adass.org
URL2 = https://www.astro.umd.edu/~teuben/adass/www2/
URL3 = https://github.com/teuben/www2

.PHONY : help
## help:          This Help
help : Makefile
	@sed -n 's/^##//p' $<

## url:
url:
	@echo no help
	@echo URL1=$(URL1)
	@echo URL2=$(URL2)
	@echo URL3=$(URL3)

#   should set 'umask 002' in the shell
GROUP = adass

## umask
umask:
	chgrp -R $(GROUP)
	find . -type d | xargs chmod g+wx
	find . -type f | xargs chmod g+w

#   only for Peter Teuben to push to adass.org and/or our mirror
## pjt: rsync to adass.org 
pjt:
	rsync -av . pteuben@adass.org:/u1/www/htdocs

## pjt2: git pull on lma
pjt2:
	ssh lma "cd public_html/adass/www2; git pull"

## pjt3 : make pjt on lma
pjt3:
	ssh lma "cd public_html/adass/www2; make pjt"
