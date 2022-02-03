
from .AbstractProjection import AbstractProjection
import math

class FisheyeProjection(AbstractProjection):
  def __init__(self):
    AbstractProjection.__init__(self)

  def set_angular_resolution(self):
    self.angular_resolution = math.pi/self.imsize[1]

  def _pixel_value(self, angle):
    FOV = math.pi
    
    theta = angle[0] * 0.5
    phi = angle[1]
    if theta is None or phi is None:
      return (0,0,0)

    
    # phi: -pi/2..pi/2 
    # theta: -pi..pi

    # using convention from http://paulbourke.net/dome/fish2/
    pt = self.point_on_sphere(theta, phi)
    p_y = pt[0]
    p_x = pt[1]
    p_z = pt[2]

    theta_l = math.atan2(p_z,p_x);
    phi_l = math.atan2(math.sqrt(p_x*p_x+p_z*p_z),p_y);
    r = phi_l / FOV;

    u = 0.5 + r * math.cos(theta_l);
    v = 0.5 + r * math.sin(theta_l);    
    
    return self.get_pixel_from_uv(u,v, self.image)

  @staticmethod
  def angular_position(texcoord):
    u = texcoord[0]
    v = texcoord[1]
    # theta: u: 0..1 -> -pi..pi
    theta = math.pi*2.0*(u-0.5)
    # phi: v: 0..1 - > -pi/2..pi/2
    phi = math.pi*(v-0.5)
    return (theta,phi)
