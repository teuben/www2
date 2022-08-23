#
#   ADASS web page management
#

URL1 = https://adass.org
URL2 = https://www.astro.umd.edu/~teuben/adass/www2/
URL3 = https://github.com/teuben/www2

help:
	@echo no help

sync1:
	(cd ..; rsync -av www2 pteuben@adass.org:/u1/www/htdocs)
