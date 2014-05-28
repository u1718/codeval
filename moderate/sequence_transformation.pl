#!/bin/env perl

while( <> ) {
    my ($bs, $ls) = split(/ /);
    my $p = '';
    foreach (split //, $bs) {
        if (/0/) {
            $p .= 'A+';
        } else {
            $p .= '(A+|B+)';
        }
    }
    if ($ls =~ /^$p$/) {
        print "Yes\n"
    } else {
        print "No\n"
    }
}

