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
      d[m.group("col_rest")].append(m.group("col_one"))

  for k, v in d.items():
    if len(v) > 1:
      for item in v:
        print(f"DUPPP: {item},{k}")
    else:
      print(f"UNIQQ: k={k}")

main()

