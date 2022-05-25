from ursina import *
import numpy as np

app=Ursina()

window.fullscreen = True
Sky(texture="textures/stars",rotation=(45,45,45))
#sky=Entity(model='sphere', scale=10000, texture='textures/stars', double_sided=True)

sun=Entity(model='sphere', scale=2, texture='textures/sun', double_sided=True)

mercury=Entity(model='sphere',position=(3,0,0), scale=0.2, texture='textures/mercury', double_sided=True)

venus=Entity(model='sphere',position=(6,0,0), scale=0.6, texture='textures/venus', double_sided=True)

earth=Entity(model='sphere',position=(9,0,0), scale=0.6, texture='textures/earth', double_sided=True)
moon=Entity(parent=earth,model='sphere',position=(1.5,0,0), scale=0.25, texture='textures/moon', double_sided=True)

mars=Entity(model='sphere',position=(12,0,0), scale=0.35, texture='textures/mars', double_sided=True)

jupiter=Entity(model='sphere',position=(17,0,0), scale=0.9, texture='textures/jupiter', double_sided=True)

saturn=Entity(model='sphere',position=(24,0,0), scale=0.8, texture='textures/saturn', double_sided=True)
ring=Entity(model='Models/ring.obj',position=(24,0,0), scale=(0.03,0.03,-0.001),rotation=(35,45,0), texture='textures/satt', double_sided=True)


uranus=Entity(model='sphere',position=(30,0,0), scale=0.7, texture='textures/uranus', double_sided=True)

neptune=Entity(model='sphere',position=(-35,0,0), scale=0.7, texture='textures/neptune', double_sided=True)
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

       #mars
       mars_orbit_rad = 12
       mars.rotation_y += time.dt * 20
       mars.x = np.cos((t + angle)/1.88) * mars_orbit_rad
       mars.z = np.sin((t + angle)/1.88) * mars_orbit_rad

       #jupiter
       jupiter_orbit_rad = 17
       jupiter.rotation_y += time.dt * 20
       jupiter.x = np.cos((t + angle) / 11.86) * jupiter_orbit_rad
       jupiter.z = np.sin((t + angle) / 11.86) * jupiter_orbit_rad

       # uranus
       uranus_orbit_rad = 30
       uranus.rotation_y += time.dt * 20
       uranus.x = np.cos((t + angle) / 84) * uranus_orbit_rad
       uranus.z = np.sin((t + angle) / 84) * uranus_orbit_rad

       # neptune
       neptune_orbit_rad = -35
       neptune.rotation_y += time.dt * 20
       neptune.x = np.cos((t + angle) / 164) * neptune_orbit_rad
       neptune.z = np.sin((t + angle) / 164) * neptune_orbit_rad



       # saturn
       saturn_orbit_rad = 24
       saturn.rotation_y += time.dt * 20
       saturn.x = np.cos((t + angle) / 29.46) * saturn_orbit_rad
       saturn.z = np.sin((t + angle) / 29.46) * saturn_orbit_rad
       ring.x = np.cos((t + angle) / 29.46) * saturn_orbit_rad
       ring.z = np.sin((t + angle) / 29.46) * saturn_orbit_rad

       if held_keys["q"]:

              for i in range(150):
                     t = t + .05
                     earth_center = Vec3(earth.x, earth.y, earth.z)
                     earth.x = np.cos((t + angle)) * earth_orbit_rad
                     earth.z = np.sin((t + angle)) * earth_orbit_rad
                     earth_center2 = Vec3(earth.x, earth.y, earth.z)
                     points_trajectory_line = (earth_center, earth_center2)
                     connections_trajectory_line = ((0, 1), (1, 0))
                     trajectory_line2 = Entity(
                            model=Mesh(vertices=points_trajectory_line, triangles=connections_trajectory_line,
                                       mode="line",
                                       thickness=4), color=color.lime)
       if held_keys["w"]:
                     for i in range(150):
                            t = t + .5
                            jupiter_center = Vec3(jupiter.x, jupiter.y, jupiter.z)
                            jupiter.x = np.cos((t + angle) / 11.86) * jupiter_orbit_rad
                            jupiter.z = np.sin((t + angle) / 11.86) * jupiter_orbit_rad
                            jupiter_center2 = Vec3(jupiter.x, jupiter.y, jupiter.z)
                            points_trajectory_line = (jupiter_center, jupiter_center2)
                            connections_trajectory_line = ((0, 1), (1, 0))
                            trajectory_line2 = Entity(
                                          model=Mesh(vertices=points_trajectory_line,
                                                     triangles=connections_trajectory_line,
                                                     mode="line",
                                                     thickness=4), color=color.lime)

       if held_keys["e"]:
                     for i in range(40):
                            t = t + .5
                            mars_center = Vec3(mars.x, mars.y, mars.z)
                            mars.x = np.cos((t + angle) / 1.88) * mars_orbit_rad
                            mars.z = np.sin((t + angle) / 1.88) * mars_orbit_rad
                            mars_center2 = Vec3(mars.x, mars.y, mars.z)
                            points_trajectory_line = (mars_center, mars_center2)
                            connections_trajectory_line = ((0, 1), (1, 0))
                            trajectory_line2 = Entity(
                                   model=Mesh(vertices=points_trajectory_line, triangles=connections_trajectory_line,
                                              mode="line",
                                              thickness=4), color=color.lime)

       if held_keys["r"]:
                            for i in range(40):
                                   t = t + .05
                                   merc_center = Vec3(mercury.x,mercury.y,mercury.z)
                                   mercury.x = np.cos((t + angle) / 0.24) * mercury_orbit_rad
                                   mercury.z = np.sin((t + angle) / 0.24) * mercury_orbit_rad
                                   merc_center2 = Vec3(mercury.x, mercury.y, mercury.z)
                                   points_trajectory_line = (merc_center, merc_center2)
                                   connections_trajectory_line = ((0, 1), (1, 0))
                                   trajectory_line1 = Entity(
                                          model=Mesh(vertices=points_trajectory_line, triangles=connections_trajectory_line, mode="line",
                                                     thickness=4), color=color.magenta)

       if held_keys["t"]:
                            for i in range(80):
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

       if held_keys["y"]:
              for i in range(80):
                     t = t + 5
                     uranus_center = Vec3(uranus.x, uranus.y, uranus.z)
                     uranus.x = np.cos((t + angle) / 84) * uranus_orbit_rad
                     uranus.z = np.sin((t + angle) / 84) * uranus_orbit_rad
                     uranus_center2 = Vec3(uranus.x, uranus.y, uranus.z)
                     points_trajectory_line = (uranus_center, uranus_center2)
                     connections_trajectory_line = ((0, 1), (1, 0))
                     trajectory_line2 = Entity(
                            model=Mesh(vertices=points_trajectory_line, triangles=connections_trajectory_line,
                                       mode="line",
                                       thickness=4), color=color.lime)
       if held_keys["u"]:
              for i in range(40):
                     t = t + 50
                     neptune_center = Vec3(neptune.x, neptune.y, neptune.z)
                     neptune.x = np.cos((t + angle) / 164) * neptune_orbit_rad
                     neptune.z = np.sin((t + angle) / 164) * neptune_orbit_rad
                     neptune_center2 = Vec3(neptune.x, neptune.y, neptune.z)
                     points_trajectory_line = (neptune_center, neptune_center2)
                     connections_trajectory_line = ((0, 1), (1, 0))
                     trajectory_line2 = Entity(
                            model=Mesh(vertices=points_trajectory_line, triangles=connections_trajectory_line,
                                       mode="line",
                                       thickness=4), color=color.lime)

       if held_keys["i"]:
              for i in range(90):
                     t = t + 5
                     saturn_center = Vec3(saturn.x, saturn.y, saturn.z)
                     saturn.x = np.cos((t + angle) / 29.46) * saturn_orbit_rad
                     saturn.z = np.sin((t + angle) / 29.46) * saturn_orbit_rad
                     saturn_center2 = Vec3(saturn.x, saturn.y, saturn.z)
                     points_trajectory_line = (saturn_center, saturn_center2)
                     connections_trajectory_line = ((0, 1), (1, 0))
                     trajectory_line2 = Entity(
                            model=Mesh(vertices=points_trajectory_line, triangles=connections_trajectory_line,
                                       mode="line",
                                       thickness=4), color=color.lime)
       if held_keys["z"]:
              sun.texture="textures/sun2"
              sun.scale = 16

       if held_keys["b"]:
              print(1)
              object = Entity(model='Models/2.obj', position=(30, 30, 30), scale=(1), texture='models/texture.jpg', double_sided=True)


app.run()