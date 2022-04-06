#!/usr/bin/perl -s
select(STDOUT); $| = 1;		# set unbuffered
$dataroot = "/usr/local/www/data/gridpix/" ;
#print "Content-type: image/jpeg\n\n" ;
print "Content-type: text/plain\n\n" ;
#($gridpix = $ENV{'PATH_INFO'}) =~ s|^/|| ;
$gpx = $ENV{'QUERY_STRING'} ;
if (0) {
  $dir = substr($gpx, 0, 12);
  system "/usr/local/bin/gpxinfo $dataroot/$dir/images/$gpx.gpx" ;
  }
else {
  system "/usr/local/bin/gpxinfo $dataroot$gpx.gpx" ;
}
