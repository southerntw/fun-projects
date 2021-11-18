import argparse

file_name = "list.txt"
file = open(file_name, "a+")

# help messages
msg = 'Simple and maybe useless to do list made from python'
add = 'Add task to your to do list'

# arguments parser
parser = argparse.ArgumentParser(description = msg)
parser.add_argument('-a', '-add', dest='task', help=add)
parser.add_argument('-r', '-remove', dest='task', help=add)
args = vars(parser.parse_args())

add = args['task']

# append to do list
if add:
  file.write(add + "\n") 
  print("Completed")
