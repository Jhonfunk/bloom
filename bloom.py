#!/bin/python
list = os.listdir(rootdir)
for name in list:
  if os.path.isfile(name):
    with open(name, 'r') as f:
      print(f.read())
