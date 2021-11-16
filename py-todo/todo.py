#!/usr/bin/env python

#def parseList():
#  li.read()  

def appendList(li, index):
  try:
    for i in range(index, 0, -1):
      li.seek(0)
      data = li.read(100)
      if len(data) > 0:
        li.write("\n")
      entry = str(input().strip())
      li.write(entry)
    print("Completed.")
  except:
    print("An error occured.")

def printList(list):
  print()
  print("Your to do list:")
  for i in list:
    print(i)

if __name__ == "__main__":
  li = open('list.txt', 'a+')
  index = int(input("Number of entries: ").strip())
  appendList(li, index)
