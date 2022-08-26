#!/bin/bash -x

cat input.txt | perl -ne 'chomp; print "$.,$_\n";' | sort -k3 -t\, | tee junk1.del
cat junk1.del | ./dedup.py  | tee output.txt

