#!/usr/bin/env python
import sys
import argparse

def readFile():
  li = open('list.txt', 'a+')
  return li

def arguments():
  # Help messages
  msg = 'Simple and maybe useless to do list made from python'
  add = 'Add to your to do list'
  
  # Parser
  parser = argparse.ArgumentParser(description = msg)
  parser.add_argument('-a', '-add')
  args = vars(parser.parse_args())

  return args

def process(args):
  li = readFile()

  add = args['a']

  # append the todo list
  if args['a'] is not None:
    append(li, add)

def append(li, add):
  try:
    li.write(add + "\n")
    print("Completed.")
  except:
   print("An error occured.")

if __name__ == "__main__":
  args = arguments()
  process(args)
