#!/usr/bin/env python3

import fileinput
import re

def process_bag(mybag):
  if not mybag:
    return

  # simple strategy to pick winner - pick first
  winner = mybag[0]
  print(winner)

def main():
  the_bag = []
  patt = re.compile(r"^(?P<rownum>\w+),(?P<rowkey>\w+),")
  (prev, curr) = (None, None)
  
  for line in fileinput.input():
    m = patt.match(line)
    curr = m.group("rowkey")
    #print(f"curr={curr}, prev={prev}, bagsize={len(the_bag)}")
    if curr != prev:
      process_bag(the_bag)
      prev = curr
      the_bag = []
    the_bag.append(line.strip())
  process_bag(the_bag)

main()

