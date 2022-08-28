#!/usr/bin/env python3

import fileinput
import re
from collections import defaultdict

def main():
  patt = re.compile(r"^(?P<col_one>.+?),(?P<col_rest>.+)")
  d = defaultdict(list)
  
  for line in fileinput.input():
    m = patt.match(line)
    if m:
      hk = str(hash(m.group("col_rest")))
      d[hk].append(line.strip())

  for k, v in d.items():
    if len(v) > 1:
      for item in v:
        print(f"DUPPP: {item}")
    else:
      print(f"UNIQQ: {v[0]}")

main()

