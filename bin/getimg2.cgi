#!/usr/bin/perl -s
select(STDOUT); $| = 1;		# set unbuffered
$dataroot = "/usr/local/www/data/gridpix/" ;
#print "Content-type: image/jpeg\n\n" ;
#print "Content-type: text/html\n\n" ;
#($gridpix = $ENV{'PATH_INFO'}) =~ s|^/|| ;
$_ = $ENV{'QUERY_STRING'} ;
#$_ = "2319102115470094&4&1200&675&6&2";
/([^&]+)&(\d+)&(\d+)/;
$gpx = $1;
$res = 1;
$width = $2;
$height = $3;
$x = 0;
$y = 0;
if (0) {
  $dir = substr($gpx, 0, 12);
  system "/usr/local/bin/mkhtml $dataroot$dir/images/$gpx.gpx $res $width $height $x $y 0 1" ;
}
else {
  system "/usr/local/bin/mkhtml $dataroot$gpx.gpx $res $width $height $x $y 0 1" ;
}
