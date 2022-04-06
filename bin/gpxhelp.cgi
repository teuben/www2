#!/usr/bin/perl -s
select(STDOUT); $| = 1;		# set unbuffered
$dataroot = "/usr/local/www/data/gridpix/" ;
#print "Content-type: image/jpeg\n\n" ;
print "Content-type: text/html\n\n" ;
#($gridpix = $ENV{'PATH_INFO'}) =~ s|^/|| ;
$_ = $ENV{'QUERY_STRING'} ;
#$_ = "2319102115470094&4&1200&675&6&2";
/([^&]+)&(\d+)&(\d+)&(.+)&(\d+)/;
$gpx = $1;
$width = $2;
$height = $3;
$mag = $4;
$internal = $5;
#print "<html><header></header><body>" ;
if ($internal) {
  $file = "help2.html";
} else {
  $file = "help.html";
}
system "/usr/bin/sed -e 's/%gpx%/$gpx/' -e 's/%width%/$width/' -e 's/%height%/$height/' -e 's/%mag%/$mag/' $dataroot/docs/$file" ;
#print "</body></html>" ;
