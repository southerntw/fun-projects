#!/usr/bin/env python
import args

file_name = "list.txt"
file = open(file_name, 'a+')

with open(file_name) as f:
  li = f.read().splitlines()

for i in li:
  print(i)
