from ursina import *
import numpy as np

app=Ursina()

window.fullscreen = True
sky=Entity(model='sphere', scale=10000, texture='stars', double_sided=True)
sun=Entity(model='sphere', scale=1.5, texture='textures/sun', double_sided=True)
mercury=Entity(model='sphere',position=(3,0,0), scale=0.2, texture='textures/mercury', double_sided=True)
venus=Entity(model='sphere',position=(6,0,0), scale=0.6, texture='textures/venus', double_sided=True)
earth=Entity(model='sphere',position=(9,0,0), scale=0.6, texture='textures/earth', double_sided=True)
moon=Entity(parent=earth,model='sphere',position=(1.5,0,0), scale=0.25, texture='textures/moon', double_sided=True)
EditorCamera()
t=np.pi
trajectory_line4 = Entity()

def update():
       global  t


       dt,x,y,z=0,0,0,0

       t=t+.005
       angle=np.pi*40/180

       #mercury

       mercury_orbit_rad = 3
       mercury.rotation_y += time.dt * 20
       mercury.x = np.cos((t+angle)/0.24) * mercury_orbit_rad
       mercury.z = np.sin((t+angle)/0.24) * mercury_orbit_rad

       #venus
       venus_orbit_rad = 6
       venus.rotation_y += time.dt * 20
       venus.x = np.cos((t + angle)/0.62) * venus_orbit_rad
       venus.z = np.sin((t + angle)/0.62) * venus_orbit_rad

       # earth
       earth_orbit_rad = 9


       earth.rotation_y += time.dt * 20
       earth.x = np.cos(t + angle) * earth_orbit_rad
       earth.z = np.sin((t + angle)) * earth_orbit_rad

       # moon
       moon_orbit_rad = 1.5
       moon.x = np.cos((t + angle)*5) * moon_orbit_rad
       moon.z = np.sin((t + angle)*5) * moon_orbit_rad

       if held_keys["q"]:


                     for i in range(360):
                            t = t + .005
                            merc_center = Vec3(mercury.x,mercury.y,mercury.z)
                            mercury.x = np.cos((t + angle) / 0.24) * mercury_orbit_rad
                            mercury.z = np.sin((t + angle) / 0.24) * mercury_orbit_rad
                            merc_center2 = Vec3(mercury.x, mercury.y, mercury.z)
                            points_trajectory_line = (merc_center, merc_center2)
                            connections_trajectory_line = ((0, 1), (1, 0))
                            trajectory_line1 = Entity(
                                   model=Mesh(vertices=points_trajectory_line, triangles=connections_trajectory_line, mode="line",
                                              thickness=4), color=color.magenta)

                            earth_center = Vec3(earth.x, earth.y, earth.z)
                            earth.x = np.cos((t + angle)  ) * earth_orbit_rad
                            earth.z = np.sin((t + angle)  ) * earth_orbit_rad
                            earth_center2 = Vec3(earth.x, earth.y, earth.z)
                            points_trajectory_line = (earth_center, earth_center2)
                            connections_trajectory_line = ((0, 1), (1, 0))
                            trajectory_line2 = Entity(
                                   model=Mesh(vertices=points_trajectory_line, triangles=connections_trajectory_line,
                                              mode="line",
                                              thickness=4), color=color.lime)
                            for i in range(1):
                                   t = t + .05
                                   venus_center = Vec3(venus.x,venus.y,venus.z)
                                   venus.x = np.cos((t + angle) / 0.62) * venus_orbit_rad
                                   venus.z = np.sin((t + angle) / 0.62) * venus_orbit_rad
                                   venus_center2 = Vec3(venus.x, venus.y, venus.z)
                                   points_trajectory_line = (venus_center, venus_center2)
                                   connections_trajectory_line = ((0, 1), (1, 0))
                                   trajectory_line3 = Entity(
                                          model=Mesh(vertices=points_trajectory_line, triangles=connections_trajectory_line, mode="line",
                                                     thickness=4), color=color.magenta)



app.run()