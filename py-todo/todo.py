#!/usr/bin/env python
import sys
import argparse

file_name = "list.txt"
file = open(file_name, 'a+')

def import_file():
  with open(file_name) as f:
    li = f.read().splitlines()
  return li

def arguments():
  # help messages
  msg = 'Simple and maybe useless to do list made from python'
  add = 'Add task to your to do list'
  
  # arguments parser
  parser = argparse.ArgumentParser(description = msg)
  parser.add_argument('-a', '-add', dest='task', help=add)
  args = vars(parser.parse_args())

  return args

def process(args):
  li = import_file()

  # initialize stuffs
  add = args['task']

  # append the todo list
  if add:
    append(li, add)

def append(li, add):
  try:
    file.write(add + "\n")
    print("Completed.")
  except:
   print("An error occured.")

def printList(li):
  for i in li:
    print(i)

if __name__ == "__main__":
  args = arguments()
  li = import_file()
  process(args)
  printList(li)
