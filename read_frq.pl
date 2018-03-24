#!/usr/bin/perl
use strict;
use warnings;
my $input_file = $ARGV[0];
open (IN, $input_file) || die "Can't open input file.";
while( my $line = <IN> ) {
  chomp($line);
  my @field =split("\t",$line);
  my $scaffold=$field[0];
  my $pos=$field[1];
  my $alleleN=$field[4];
  my $alleleA;
  my $alleleT;
  my $alleleG;
  my $alleleC;
  print "$scaffold\t$pos\t$alleleN";
 }
close (IN);
exit;