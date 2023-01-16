#!/usr/bin/env perl
use strict;
use warnings;

my $para = "";

TEXT:
while (<>)
{
NOTES:
    while (m/^\s*\[(\d+)]\s+(.*)/)
    {
        my $tag = $1;
        my $note = $2;
        $para =~ s/\[$tag]/\\footnote{$note}/m;
        while (<>)
        {
            last if $_ =~ m/^\s*\[/;
            if ($_ !~ m/^\s*$/)
            {
            print $para;
            $para = "";
            last NOTES;
            }
        }
        last TEXT if eof;
    }

    $para .= $_;
}

print "$para";
