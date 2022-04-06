#!/usr/bin/perl -s
select(STDOUT); $| = 1;		# set unbuffered
$dataroot = "/usr/local/www/data/gridpix/" ;
#print "Content-type: image/jpeg\n\n" ;
print "Content-type: text/html\n\n" ;
#($gridpix = $ENV{'PATH_INFO'}) =~ s|^/|| ;
$_ = $ENV{'QUERY_STRING'} ;
#$_ = "2319102115470094&4&1200&675&6&2";
/(\d+)&(\d+)&(\d+)/;
$dir = $1;
$width = $2;
$height = $3;
#print "<html><header></header><body>" ;
#system "/usr/bin/sed -e 's/%width%/$width/' -e 's/%height%/$height/' -e 's,%dir%,/famsf/gridpix/$dir/thumbnails,' -e 's,/cgi-bin/getimg2,http://128.32.45.101/cgi-bin/getimg7,' $dataroot/$dir/files.html" ;
if (-r "$dataroot/$dir/files.html") {
  system "/usr/bin/sed -e 's/%width%/$width/' -e 's/%height%/$height/' -e 's,%dir%,/famsf/gridpix/$dir/thumbnails,' -e 's,updir.gif\"></a>,updir.gif\"></a><p><form action=\"/cgi-bin/subdir2.cgi\" method=\"GET\">View folder by number: <input name=\"dir\"><input name=\"width\" type=\"hidden\" value=\"$width\"><input name=\"height\" type=\"hidden\" value=\"$height\"> <input type=\"submit\" value=\"go\"></form><form action=\"/cgi-bin/getimg4.cgi\" method=\"GET\">View image by number: <input name=\"gpx\"><input name=\"width\" type=\"hidden\" value=\"$width\"><input name=\"height\" type=\"hidden\" value=\"$height\"> <input type=\"submit\" value=\"go\"></form>,' $dataroot/$dir/files.html" ;
}
else {
  print "<html><header></header><body>" ;
  print "The folder you requested (\"$dir\") does not exist on this server.\n";
  print "</body></html>" ;
}
