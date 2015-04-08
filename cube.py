# -*- coding: utf-8 -*-

import numpy
from shape import Shape
from ulti import iterable_to_chunks

class Cube(Shape):

  def __init__(self, ax, x = 0, y = 0, z = 0,
    height = 1., width = 1., depth = 1., **kwargs) :

    super(Cube, self).__init__(ax, x, y, z, **kwargs)

    self.initiate(ax, x, y, z, height, width, depth, **kwargs)

  def set_size(self, height = None, width = None, depth = None, update = False) :

    self.height = height or self.height
    self.width = width or self.width
    self.depth = depth or self.depth

    if update : # To do: update size using _vec

      self.front_bot_left  = [x,         y,          z]
      self.front_bot_right = [x + width, y,          z]
      self.front_top_left  = [x,         y + height, z]
      self.front_top_right = [x + width, y + height, z]

      self.rear_bot_left   = [x,         y,          z + depth]
      self.rear_bot_right  = [x + width, y,          z + depth]
      self.rear_top_left   = [x,         y + height, z + depth]
      self.rear_top_right  = [x + width, y + height, z + depth]

  def change_size(self, height = None, width = None, depth = None) :
    raise NotImplementedError('Change size is not implemented for Cube.')

  def create_Ploy3DCollection(self, *two_lines, **kwargs) :

    x, y, z = zip(two_lines[0], two_lines[1], two_lines[2], two_lines[3])

    X = [ __ for __ in iterable_to_chunks(x, 2) ]
    Y = [ __ for __ in iterable_to_chunks(y, 2) ]
    Z = [ __ for __ in iterable_to_chunks(z, 2) ]

    return self.ax.plot_surface(X, Y, Z, **kwargs)

  def initiate(self, ax, x = 0, y = 0, z = 0,
    height = 1., width = 1., depth = 1., **kwargs) :

    self.ax = ax
    self.x, self.y, self.z = x, y, z
    self.set_size(height, width, depth)

    if 'initiate points' :

      self.points = [ numpy.zeros(3, dtype = 'float') for __ in xrange(8) ]

      self.front_bot_left  = self.points[0]
      self.front_bot_right = self.points[1]
      self.front_top_left  = self.points[2]
      self.front_top_right = self.points[3]

      self.rear_bot_left   = self.points[4]
      self.rear_bot_right  = self.points[5]
      self.rear_top_left   = self.points[6]
      self.rear_top_right  = self.points[7]

      self.front_bot_left  = [x,         y,          z]
      self.front_bot_right = [x + width, y,          z]
      self.front_top_left  = [x,         y + height, z]
      self.front_top_right = [x + width, y + height, z]

      self.rear_bot_left   = [x,         y,          z + depth]
      self.rear_bot_right  = [x + width, y,          z + depth]
      self.rear_top_left   = [x,         y + height, z + depth]
      self.rear_top_right  = [x + width, y + height, z + depth]

    if 'initiate surfaces' :

      self.top = self.create_Ploy3DCollection(
        self.front_top_left, self.front_top_right,
        self.rear_top_left,  self.rear_top_right, **kwargs)

      self.bot = self.create_Ploy3DCollection(
        self.front_bot_left, self.front_bot_right,
        self.rear_bot_left,  self.rear_bot_right, **kwargs)

      self.front = self.create_Ploy3DCollection(
        self.front_bot_left, self.front_bot_right,
        self.front_top_left, self.front_top_right, **kwargs)

      self.rear = self.create_Ploy3DCollection(
        self.rear_top_left, self.rear_top_right,
        self.rear_bot_left, self.rear_bot_right, **kwargs)

      self.left = self.create_Ploy3DCollection(
        self.front_bot_left, self.front_top_left,
        self.rear_bot_left, self.rear_top_left, **kwargs)

      self.right = self.create_Ploy3DCollection(
        self.front_bot_right, self.front_top_right,
        self.rear_bot_right, self.rear_top_right, **kwargs)

    self.surfaces = [ self.top,   self.bot,
                      self.front, self.rear,
                      self.left,  self.right ]

if __name__ == '__main__' :

  from mpl_toolkits.mplot3d import Axes3D

  import matplotlib.pyplot as plt

  fig = plt.figure()
  ax = Axes3D(fig)
  ax.view_init(elev = -80., azim = 90)
  plt.xlabel('x')
  plt.ylabel('y')
  ax.set_xlim(-10, 10)
  ax.set_ylim(-10, 10)
  ax.set_zlim(-10, 10)
  ax.set_zlabel('z')
  ax.set_zticks([])

  c = Cube(ax, x = 0, y = 1, z = 1, height = 2, width = 2, depth = 3)
  c.modify_x(2)

  plt.show()
