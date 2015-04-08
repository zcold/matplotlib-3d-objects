# -*- coding: utf-8 -*-

import numpy
from shape import Shape

class Sphere(Shape):

  def __init__(self, ax, x = 0, y = 0, z = 0,
    radius = 1., detail_level = 16, rstride = 1, cstride = 1, **kwargs) :

    super(Sphere, self).__init__(ax, x, y, z, **kwargs)

    self.initiate(ax, x, y, z, radius, detail_level, rstride, cstride, **kwargs)

  def set_size(self, radius = None, update = False) :

    self.radius = radius or self.radius

    if update :
      self.change_size(radius)

  def change_size(self, radius) :

    current_radius = self.radius
    for i, center_value in enumerate(self.position[:3]) :
      for j, value in enumerate(self.surfaces[0]._vec[i]) :
        self.surfaces[0]._vec[i][j] = center_value + \
          (value - center_value) * float(radius) / current_radius

  def create_Ploy3DCollection(self, **kwargs) :

    u = numpy.linspace(0, 2 * numpy.pi, self.detail_level)
    v = numpy.linspace(0, numpy.pi, self.detail_level)

    X = self.x + \
        self.radius * numpy.outer(numpy.cos(u), numpy.sin(v))

    Y = self.y + \
        self.radius * numpy.outer(numpy.sin(u), numpy.sin(v))

    Z = self.z + \
        self.radius * numpy.outer(numpy.ones(numpy.size(u)), numpy.cos(v))

    return self.ax.plot_surface(X, Y, Z,
      rstride = self.rstride, cstride = self.cstride, **kwargs)

  def initiate(self, ax, x = 0, y = 0, z = 0, radius = 1., detail_level = 16,
    rstride = 1, cstride = 1, **kwargs) :

    self.ax = ax
    self.x, self.y, self.z = x, y, z
    self.detail_level = detail_level
    self.rstride = rstride
    self.cstride = cstride
    self.set_size(radius)

    self.surface = self.create_Ploy3DCollection(**kwargs)
    self.surfaces = [ self.surface ]

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

  s = Sphere(ax, x = 0, y = 1, z = 1, radius = 2)
  s.modify_x(2)

  plt.show()
