#!/usr/bin/perl -s
select(STDOUT); $| = 1;		# set unbuffered
$dataroot = "/usr/local/www/data/famsf/gridpix" ;
#print "Content-type: image/jpeg\n\n" ;
print "Content-type: text/html\n\n" ;
#($gridpix = $ENV{'PATH_INFO'}) =~ s|^/|| ;
$_ = $ENV{'QUERY_STRING'} ;
#$_ = "864&576";
$file = 'files.html';
$width = 864;
$height = 576;
if (/([^&]+)&(\d+)&(\d+)/) {
  $file = $1;
  $width = $2;
  $height = $3;
}
elsif (/(\d+)&(\d+)/) {
  $width = $1;
  $height = $2;
}
#print "<html><header></header><body>" ;
system "/usr/bin/sed -e 's/%width%/$width/' -e 's/%height%/$height/' $dataroot/$file" ;
#print "</body></html>" ;
