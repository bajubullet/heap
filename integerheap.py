class IntegerHeap(object):
  def __init__(self, *args, **kwargs):
    self.data = []

  def insert(self, num):
    assert isinstance(num, int)
    self.data.append(num)
    self.heapify(len(self.data)-1)

  def heapify(self, i):
    # check parent nodes
    parent = self.get_parent(i)
    if parent > -1:
      if self.data[parent] < self.data[i]:
        self.data[parent], self.data[i] = self.data[i], self.data[parent]
        self.heapify(parent)
        return
    # check left and right
    left, right = self.get_left(i), self.get_right(i)
    try:
      leftEl, rightEl = self.data[left], self.data[right]
    except IndexError:
      return
    if leftEl > rightEl:
      if self.data[i] < leftEl:
        self.data[left], self.data[i] = self.data[i], self.data[left]
        self.heapify(left)
        return
    if rightEl > self.data[i]:
      self.data[right], self.data[i] = self.data[i], self.data[right]
      self.heapify(right)
      return


  def get_parent(self, i):
    return (i - 1)/2

  def get_left(self, i):
    return 2 * i + 1

  def get_right(self, i):
    return self.get_left(i) + 1

  def delete(self, i):
    length = len(self.data)
    if i == length - 1:
      del self.data[i]
      return
    self.data[i], self.data[length-1] = self.data[length-1], self.data[i]
    del self.data[length-1]
    self.heapify(i)

import random
asd = IntegerHeap()
data = range(50)
random.shuffle(data)
for i in data:
  asd.insert(i)

print asd.data
asd.delete(0)
print asd.data
asd.delete(0)
print asd.data
asd.delete(0)
print asd.data
asd.delete(0)
print asd.data
asd.delete(0)
print asd.data
