#!/usr/bin/env python
import argparse

# opening the .txt file
file_name = "list.txt"
file = open(file_name, 'a+')

# help messages
msg_help = 'Simple and maybe useless to do list made from python'
msg_add = 'Add task to your to do list'
msg_remove = 'Remove things'

# arguments parser
parser = argparse.ArgumentParser(description = msg_help)
parser.add_argument('-a', '--add', dest='add', help=msg_add)
parser.add_argument('-r', '--remove', dest='rm', type=int, help=msg_remove)
args = vars(parser.parse_args())

# reading file per lines into a list then print it
with open(file_name) as f:
  li = f.read().splitlines()

add = args['add']
rm = args['rm']

# a method to rewrite
def rewrite():
  file.truncate(0)
  for i in li:
    file.write(i + "\n") 
  print("Completed")

# append to do list (if argument is passed)
if add:
  li.append(add)
  rewrite()

if rm:
  del li[rm - 1]
  rewrite()

for idx, val in enumerate(li):
  print("%i | %s" % ((idx + 1), val))
