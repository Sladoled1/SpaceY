from ursina import *
import numpy as np

app=Ursina()

window.fullscreen = True
sky=Entity(model='sphere', scale=10000, texture='stars', double_sided=True)

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

def update():
       global  t
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
       earth.z = np.sin(t + angle) * earth_orbit_rad

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


       #saturn
       saturn_orbit_rad = 24
       saturn.rotation_y += time.dt * 20
       saturn.x = np.cos((t + angle) / 29.46) * saturn_orbit_rad
       saturn.z = np.sin((t + angle) / 29.46) * saturn_orbit_rad

       ring.x = np.cos((t + angle) / 29.46) * saturn_orbit_rad
       ring.z = np.sin((t + angle) / 29.46) * saturn_orbit_rad

       #uranus
       uranus_orbit_rad = 30
       uranus.rotation_y += time.dt * 20
       uranus.x = np.cos((t + angle) / 84) * uranus_orbit_rad
       uranus.z = np.sin((t + angle) / 84) * uranus_orbit_rad

       #neptune
       neptune_orbit_rad = -35
       neptune.rotation_y += time.dt * 20
       neptune.x = np.cos((t + angle) / 164) * neptune_orbit_rad
       neptune.z = np.sin((t + angle) / 164) * neptune_orbit_rad

#планетки
app.run()