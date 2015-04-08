# -*- coding: utf-8 -*-

class Shape(object):

  def __init__(self, ax, x = 0., y = 0., z = 0., a = 1., **kwargs) :

    self.ax = ax
    self.position = [x, y, z, a]
    self.surfaces = []
    self.current_position = [x, y, z, a]

  @property
  def x(self):
    return self.position[0]

  @x.setter
  def x(self, value):
    self.position[0] = value

  @property
  def y(self):
    return self.position[1]

  @y.setter
  def y(self, value):
    self.position[1] = value

  @property
  def z(self):
    return self.position[2]

  @z.setter
  def z(self, value):
    self.position[2] = value

  @property
  def a(self):
    return self.position[3]

  @a.setter
  def a(self, value):
    self.position[3] = value

  @property
  def alpha(self):
    return self.position[3]

  @alpha.setter
  def alpha(self, value):
    self.position[3] = value

  _dimension_dict = {'x': 0, 'y': 1, 'z': 2, 'a': 3, 'alpha': 3}

  def _modify_dimension(self, new_value, dimension = 0) :

    if dimension not in [0, 1, 2, 3] :
      dimension = Shape._dimension_dict[dimension.lower()]

    diff = new_value - self.position[dimension]

    for surface in self.surfaces :
      for i, __ in enumerate(surface._vec[dimension]) :
        surface._vec[dimension][i] += diff

    self.position[dimension] = new_value

  def modify_x(self, new_x) :
    self._modify_dimension(new_x, dimension = 0)

  def modify_y(self, new_y) :
    self._modify_dimension(new_y, dimension = 1)

  def modify_z(self, new_z) :
    self._modify_dimension(new_z, dimension = 2)

  def modify_alpha(self, new_alpha) :
    self._modify_dimension(new_alpha, dimension = 3)

  def modify_position(self, *position) :
    self.modify_x(position[0])
    self.modify_y(position[1])
    self.modify_z(position[2])

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

  s = Shape(ax, x = 0, y = 1, z = 1)
  s.modify_x(2)

  plt.show()
