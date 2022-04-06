#!/usr/bin/perl -s
select(STDOUT); $| = 1;		# set unbuffered
$dataroot = "/usr/local/www/data/gridpix/" ;
#print "Content-type: text/html\n\n" ;
#($gridpix = $ENV{'PATH_INFO'}) =~ s|^/|| ;
$_ = $ENV{'QUERY_STRING'} ;
#$_ = "2319102115470094&4&1200&675&6&2";
/([^&]+)&(\d+)&(\d+)&(\d+)&([^&]+)&([^&]+)&([^&]+)&([^&]+)/;
$gpx = $1;
$res = $2;
$width = $3;
$height = $4;
$x = $5;
$y = $6;
$smooth = $7;
$internal = $8;
if (0) {
  $dir = substr($gpx, 0, 12);
  system "/usr/local/bin/mkhtml $dataroot$dir/images/$gpx.gpx $res $width $height $x $y $smooth $internal" ;
  }
else {
  system "/usr/local/bin/mkhtml $dataroot$gpx.gpx $res $width $height $x $y $smooth $internal" ;
}
