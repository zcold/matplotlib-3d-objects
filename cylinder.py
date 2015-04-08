# -*- coding: utf-8 -*-

import numpy
from shape import Shape

class Cylinder(Shape):

  def __init__(self, ax, x = 0, y = 0, z = 0, height = 1., radius = 1.,
    radius_dimension = ['x', 'z'], height_dimension = 'y',
    has_top_cover = True, has_bottom_cover = True,
    detail_level = 16, rstride = 1, cstride = 1, **kwargs) :

    super(Cylinder, self).__init__(ax, x, y, z, **kwargs)

    self.initiate(ax, x, y, z, height, radius,
      radius_dimension, height_dimension,
      has_top_cover, has_bottom_cover,
      detail_level, rstride, cstride, **kwargs)

  def set_size(self, radius = None, height = None, update = False) :

    self.radius = radius or self.radius
    self.height = height or self.height

    if update :
      self.change_size(radius, height)

  def change_size(self, radius = None, height = None) :

    if radius :

      current_radius = self.radius
      for i in self.radius_dimension :
        center_value = self.position[i]
        for surface in self.surfaces :
          for j, value in enumerate(surface._vec[i]) :
            surface._vec[i][j] = center_value + \
              (value - center_value) * float(radius) / current_radius

  def create_Ploy3DCollection(self, **kwargs) :

    if 'shell' :

      phi = numpy.linspace(0, 2 * numpy.pi, self.detail_level)
      r = numpy.ones(self.detail_level)
      h = numpy.linspace(0, 1, self.detail_level)

      shell_points = [ [], [], [] ]

      shell_points[self.radius_dimension[0]] = \
        self.position[self.radius_dimension[0]] + \
        self.radius * numpy.outer(numpy.cos(phi), r)

      shell_points[self.radius_dimension[1]] = \
        self.position[self.radius_dimension[1]] + \
        self.radius * numpy.outer(numpy.sin(phi), r)

      shell_points[self.height_dimension] = \
        self.position[self.height_dimension] + \
        self.height * numpy.outer(numpy.ones(numpy.size(r)), h)

      shell = ax.plot_surface(
        shell_points[0], shell_points[1], shell_points[2],
        rstride = self.rstride, cstride = self.cstride, **kwargs)

    top_cover = None
    bottom_cover = None

    if self.has_top_cover or self.has_bottom_cover :

      phi_cover = numpy.linspace(0, 2 * numpy.pi, self.detail_level)
      r_cover = numpy.linspace(0, 1, self.detail_level)
      phi_grid, r_grid = numpy.meshgrid(phi_cover, r_cover)

      if self.has_top_cover :

        top_cover_points = [ [], [], [] ]

        top_cover_points[self.radius_dimension[0]] = \
          self.position[self.radius_dimension[0]] + \
          self.radius * numpy.cos(phi_grid) * r_grid

        top_cover_points[self.radius_dimension[1]] = \
          self.position[self.radius_dimension[1]] + \
          self.radius * numpy.sin(phi_grid) * r_grid

        top_cover_points[self.height_dimension] = \
          self.position[self.height_dimension] + \
          self.height * numpy.ones([self.detail_level, self.detail_level])

        top_cover = ax.plot_surface(
          top_cover_points[0], top_cover_points[1], top_cover_points[2],
          rstride = self.rstride*2, cstride = self.cstride*2, **kwargs)

      if self.has_bottom_cover :

        bottom_cover_points = [ [], [], [] ]

        bottom_cover_points[self.radius_dimension[0]] = \
          top_cover_points[self.radius_dimension[0]]

        bottom_cover_points[self.radius_dimension[1]] = \
          top_cover_points[self.radius_dimension[1]]

        bottom_cover_points[self.height_dimension] = \
          self.position[self.height_dimension] + \
          numpy.zeros([self.detail_level, self.detail_level])

        bottom_cover = ax.plot_surface(
          bottom_cover_points[0], bottom_cover_points[1], bottom_cover_points[2],
          rstride = self.rstride*2, cstride = self.cstride*2, **kwargs)

    return shell, top_cover, bottom_cover

  def initiate(self, ax, x = 0, y = 0, z = 0, height = 1., radius = 1.,
    radius_dimension = ['x', 'z'], height_dimension = 'y',
    has_top_cover = True, has_bottom_cover = True,
    detail_level = 16, rstride = 1, cstride = 1, **kwargs) :

    self.ax = ax
    self.x, self.y, self.z = x, y, z
    self.detail_level = detail_level
    self.rstride = rstride
    self.cstride = cstride
    self.radius_dimension = radius_dimension
    self.height_dimension = height_dimension
    self.radius = radius
    self.height = height
    self.has_top_cover = has_top_cover
    self.has_bottom_cover = has_bottom_cover

    for i, d in enumerate(self.radius_dimension) :
      if d not in Shape._dimension_dict.values() :
        self.radius_dimension[i] = Shape._dimension_dict[d.lower()]

    if height_dimension not in Shape._dimension_dict.values() :
        self.height_dimension = Shape._dimension_dict[height_dimension.lower()]

    self.set_size(radius)

    self.shell, self.top_cover, self.bottom_cover = \
      self.create_Ploy3DCollection(**kwargs)
    self.surfaces = [ self.shell, self.top_cover, self.bottom_cover ]


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

  c = Cylinder(ax, x = 0, y = 1, z = 1, height = 2, radius = 4)
  c.modify_x(2)

  plt.show()
