#!/bin/bash -x

cat input.txt | sort -k2 -t\, > junk1.del
cat junk1.del | ./dedup.py  > output.txt

