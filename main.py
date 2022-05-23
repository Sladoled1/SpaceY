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

#fffuiieiehieihe
app.run()