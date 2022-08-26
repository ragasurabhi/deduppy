#!/usr/bin/env python3

import fileinput
import re

def process_bag(mybag):
  if not mybag:
    return

  # simple strategy to pick winner - pick first
  winner = mybag[0]
  dup_positions = [x[0] for x in mybag[1:]]
  print(f"{','.join(winner[1:])}|{','.join(dup_positions)}|")

def main():
  the_bag = []
  patt = re.compile(r"^(?P<col_one>.+?),(?P<col_two>.+?),(?P<col_rest>.+)")
  (prev, curr) = (None, None)
  
  for line in fileinput.input():
    m = patt.match(line)
    curr = m.group("col_rest")
    #print(f"curr={curr}, prev={prev}, bagsize={len(the_bag)}")
    if curr != prev:
      process_bag(the_bag)
      prev = curr
      the_bag = []
    the_bag.append((m.group("col_one"), m.group("col_two"), m.group("col_rest")))
  process_bag(the_bag)

main()


