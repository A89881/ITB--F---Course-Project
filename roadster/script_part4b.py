#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import route_nyc 

### Given contour plot ###
n_fine = 100
t_fine = np.linspace(0, 24, n_fine)
x_fine = np.linspace(0, 60, n_fine)
tt_fine, xx_fine = np.meshgrid(t_fine, x_fine)
zz_fine = route_nyc.route_nyc(tt_fine,xx_fine)
w, h = plt.figaspect(0.4)
fig = plt.figure(figsize=(w, h))
plt.axes().set_aspect(0.2, adjustable='box')
cs = plt.contourf(tt_fine,xx_fine,zz_fine, 50, cmap=cm.get_cmap('jet'))
plt.xlabel('Time [hour of day]',fontsize=18)
plt.ylabel('Distance [km]',fontsize=18)
plt.title('Speed [km/h]',fontsize=18)
fig.colorbar(cs)
plt.savefig("speed-data-nyc.eps", bbox_inches='tight')

# Add Euler route travelers for two different start times - Using nyc_route_traveler_euler
# Arbitrary step size for Euler method
h_euler = 0.1  # in hours

# Trip 1: start 04:00 -> t0 = 4.0
t0_a = 4.0
time_a, dist_a, speed_a = route_nyc.nyc_route_traveler_euler(t0_a, h_euler)
plt.plot(time_a, dist_a, linewidth=1, marker='s', label='Trip start 04:00 (Euler)')

# Trip 2: start 09:30 -> t0 = 9.5
t0_b = 9.5
time_b, dist_b, speed_b = route_nyc.nyc_route_traveler_euler(t0_b, h_euler)
plt.plot(time_b, dist_b, linewidth=1, marker='o', label='Trip start 09:30 (Euler)')


plt.savefig("speed-data-nyc.eps", bbox_inches='tight')
plt.savefig("speed-data-nyc.png", bbox_inches='tight')
plt.legend(loc='best', fontsize=12)
plt.show()
