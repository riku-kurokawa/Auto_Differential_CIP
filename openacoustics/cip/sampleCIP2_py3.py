#  ooo  oooo  oooo o   o     o    ooo   ooo  o   o  oooo ooooo o  ooo   oooo
# 0   0 0   0 0    00  0    0 0  0   0 0   0 0   0 0       0   0 0   0 0
# 0   0 oooo  oooo 0 0 0   0   0 0     0   0 0   0  oooo   0   0 0      oooo
# 0   0 o     0    0 o 0   ooooo 0   o 0   0 0   0      0  0   0 0   o      0
#  ooo  o     oooo o  0o  0     0 ooo   ooo   ooo  0oooo   0   0  ooo  0oooo
#
#  (  (  (  (  (  (  (  (  (  (  (  (  O  )  )  )  )  )  )  )  )  )  )  )  )
#
#    OpenAcoustics: The Open Source Collection for Computational Acoustics
#
#               Copyright (C) 2008-2012 The OpenAcoustics Team
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from time  import *
from pylab import *
from numpy import *
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

X = 101
Y = 101
NT = 301

f_p   = zeros((X,Y), "float64")
f_m   = zeros((X,Y), "float64")
g_p   = zeros((X,Y), "float64")
g_m   = zeros((X,Y), "float64")
fn_p  = zeros((X,Y), "float64")
fn_m  = zeros((X,Y), "float64")
gn_p  = zeros((X,Y), "float64")
gn_m  = zeros((X,Y), "float64")

P     = zeros((X,Y), "float64")
dx_P  = zeros((X,Y), "float64")
dy_P  = zeros((X,Y), "float64")

ZUx    = zeros((X,Y), "float64")
dx_ZUx = zeros((X,Y), "float64")

ZUy    = zeros((X,Y), "float64")
dy_ZUy = zeros((X,Y), "float64")

coeff10 = zeros(8,  "float64")
coeff31 = zeros(32, "float64")

xc= (X-1) // 2
yc= (Y-1) // 2

dx = 5.e-2
dy = 5.e-2
dt = 5.e-5

Ro = 1.21
bm = 1.4235529e5
c0 = sqrt(bm / Ro)
Z0 = sqrt(bm * Ro)
sigma = 0.2

Ua = c0
xi =-Ua * dt
C  = c0 * dt / dx
C2 = C  * C
C3 = C2 * C

coeff10[0]  = C * 0.5
coeff10[1]  = (-C + 1.) * 0.5

coeff31[0]  = (-2. * C3 + 3. * C2) * 0.5
coeff31[1]  = (2. * C3 - 3. * C2 + 1.) * 0.5
coeff31[2]  = xi * (C2 - C) * 0.5
coeff31[3]  = xi * (C2 - 2. * C + 1.) * 0.5
coeff31[4]  = 6. * (-C3 + C2) / xi * 0.5
coeff31[5]  = 6. * (C3 - C2) / xi * 0.5
coeff31[6]  = (3. * C2 - 2. * C) * 0.5
coeff31[7]  = (3. * C2 - 4. * C + 1.) * 0.5

Ua =-c0
xi =-Ua * dt
C  = c0 * dt / dx
C2 = C  * C
C3 = C2 * C

coeff10[2]  = C * 0.5
coeff10[3]  = (-C + 1.) * 0.5

coeff31[8]  = (-2. * C3 + 3. * C2) * 0.5
coeff31[9]  = (2. * C3 - 3. * C2 + 1.) * 0.5
coeff31[10] = xi * (C2 - C) * 0.5
coeff31[11] = xi * (C2 - 2. * C + 1.) * 0.5
coeff31[12] = 6. * (-C3 + C2) / xi * 0.5
coeff31[13] = 6. * (C3 - C2) / xi * 0.5
coeff31[14] = (3. * C2 - 2. * C) * 0.5
coeff31[15] = (3. * C2 - 4. * C + 1.) * 0.5

Ua = c0
yi =-Ua * dt
C  = c0 * dt / dy
C2 = C  * C
C3 = C2 * C

coeff10[4]  = C * 0.5
coeff10[5]  = (-C + 1.) * 0.5

coeff31[16] = (-2. * C3 + 3. * C2) * 0.5
coeff31[17] = (2. * C3 - 3. * C2 + 1.) * 0.5
coeff31[18] = yi * (C2 - C) * 0.5
coeff31[19] = yi * (C2 - 2. * C + 1.) * 0.5
coeff31[20] = 6. * (-C3 + C2) / yi * 0.5
coeff31[21] = 6. * (C3 - C2) / yi * 0.5
coeff31[22] = (3. * C2 - 2. * C) * 0.5
coeff31[23] = (3. * C2 - 4. * C + 1.) * 0.5

Ua =-c0
yi =-Ua * dt
C  = c0 * dt / dy
C2 = C  * C
C3 = C2 * C

coeff10[6]  = C * 0.5
coeff10[7]  = (-C + 1.) * 0.5

coeff31[24] = (-2. * C3 + 3. * C2) * 0.5
coeff31[25] = (2. * C3 - 3. * C2 + 1.) * 0.5
coeff31[26] = yi * (C2 - C) * 0.5
coeff31[27] = yi * (C2 - 2. * C + 1.) * 0.5
coeff31[28] = 6. * (-C3 + C2) / yi * 0.5
coeff31[29] = 6. * (C3 - C2) / yi * 0.5
coeff31[30] = (3. * C2 - 2. * C) * 0.5
coeff31[31] = (3. * C2 - 4. * C + 1.) * 0.5

for i in range(1, X-1):
    x = dx * i
    for j in range(1, Y-1):
        y = dy * j
        TX = x - xc * dx
        TY = y - yc * dy
        P[i][j]     = \
                    exp(((-TX * TX) + (-TY * TY)) / (2. * sigma**2))
        dx_P[i][j]  = -TX * \
                    exp(((-TX * TX) + (-TY * TY)) / (2. * sigma**2)) / sigma**2
        dy_P[i][j]  = -TY * \
                    exp(((-TX * TX) + (-TY * TY)) / (2. * sigma**2)) / sigma**2
                    
def LINEAR(coeff0, coeff1, f0, f1):
    return    coeff0 * f0 \
            + coeff1 * f1

def CIP(coeff0, coeff1, coeff2, coeff3, f0, f1, g0, g1):
    return    coeff0 * f0 \
            + coeff1 * f1 \
            + coeff2 * g0 \
            + coeff3 * g1

start = time.time()


for t in range(NT):
    if (t % 50) == 0:
        figure(figsize=(7.5,6))
        pcolor(P)
        colorbar()
        xlim(0,X-1)
        ylim(0,Y-1)
        clim(-0.25,0.25)
        xlabel("Y [sample]")
        ylabel("X [sample]")
        show()

    f_p[1:X-1,1:Y-1]   = dy_P[1:X-1,1:Y-1] + (ZUx[1:X-1,2:Y] \
                          - ZUx[1:X-1,0:Y-2]) / (2. * dy)
    f_m[1:X-1,1:Y-1]   = dy_P[1:X-1,1:Y-1] - (ZUx[1:X-1,2:Y] \
                          - ZUx[1:X-1,0:Y-2]) / (2. * dy)

    fn_p[1:X-1,1:Y-1]  = LINEAR(coeff10[0], coeff10[1], \
                                 f_p[0:X-2,1:Y-1], f_p[1:X-1,1:Y-1])
    fn_m[1:X-1,1:Y-1]  = LINEAR(coeff10[2], coeff10[3], \
                                 f_m[2:X,1:Y-1],   f_m[1:X-1,1:Y-1])

    dy_P[1:X-1,1:Y-1]  = (fn_p[1:X-1,1:Y-1] + fn_m[1:X-1,1:Y-1]) 

    f_p[1:X-1,1:Y-1]   =    P[1:X-1,1:Y-1] +ZUx[1:X-1,1:Y-1]
    f_m[1:X-1,1:Y-1]   =    P[1:X-1,1:Y-1] - ZUx[1:X-1,1:Y-1]
    g_p[1:X-1,1:Y-1]   = dx_P[1:X-1,1:Y-1] + dx_ZUx[1:X-1,1:Y-1]
    g_m[1:X-1,1:Y-1]   = dx_P[1:X-1,1:Y-1] - dx_ZUx[1:X-1,1:Y-1]

    fn_p[1:X-1,1:Y-1]  = CIP(coeff31[0],  coeff31[1],  coeff31[2],  coeff31[3], \
                               f_p[0:X-2,1:Y-1], f_p[1:X-1,1:Y-1], \
                               g_p[0:X-2,1:Y-1], g_p[1:X-1,1:Y-1])
    gn_p[1:X-1,1:Y-1]  = CIP(coeff31[4],  coeff31[5],  coeff31[6],  coeff31[7], \
                               f_p[0:X-2,1:Y-1], f_p[1:X-1,1:Y-1], \
                               g_p[0:X-2,1:Y-1], g_p[1:X-1,1:Y-1])
    fn_m[1:X-1,1:Y-1]  = CIP(coeff31[8],  coeff31[9],  coeff31[10], coeff31[11], \
                               f_m[2:X,1:Y-1],   f_m[1:X-1,1:Y-1], \
                               g_m[2:X,1:Y-1],   g_m[1:X-1,1:Y-1])
    gn_m[1:X-1,1:Y-1]  = CIP(coeff31[12], coeff31[13], coeff31[14], coeff31[15], \
                               f_m[2:X,1:Y-1],   f_m[1:X-1,1:Y-1], \
                               g_m[2:X,1:Y-1],   g_m[1:X-1,1:Y-1])

    P[1:X-1,1:Y-1]     = (fn_p[1:X-1,1:Y-1] + fn_m[1:X-1,1:Y-1]) 
    ZUx[1:X-1,1:Y-1]    = (fn_p[1:X-1,1:Y-1] - fn_m[1:X-1,1:Y-1]) 
    dx_P[1:X-1,1:Y-1]  = (gn_p[1:X-1,1:Y-1] + gn_m[1:X-1,1:Y-1]) 
    dx_ZUx[1:X-1,1:Y-1] = (gn_p[1:X-1,1:Y-1] - gn_m[1:X-1,1:Y-1]) 

    f_p[1:X-1,1:Y-1]   = dx_P[1:X-1,1:Y-1] \
                          + (ZUy[2:X,1:Y-1] - ZUy[0:X-2,1:Y-1]) / (2. * dx)
    f_m[1:X-1,1:Y-1]   = dx_P[1:X-1,1:Y-1] \
                          - (ZUy[2:X,1:Y-1] - ZUy[0:X-2,1:Y-1]) / (2. * dx)

    fn_p[1:X-1,1:Y-1]  = LINEAR(coeff10[4], coeff10[5], \
                                 f_p[1:X-1,0:Y-2], f_p[1:X-1,1:Y-1])
    fn_m[1:X-1,1:Y-1]  = LINEAR(coeff10[6], coeff10[7], \
                                 f_m[1:X-1,2:Y],   f_m[1:X-1,1:Y-1])

    dx_P[1:X-1,1:Y-1]  = (fn_p[1:X-1,1:Y-1] + fn_m[1:X-1,1:Y-1]) 

    f_p[1:X-1,1:Y-1]   =    P[1:X-1,1:Y-1] + ZUy[1:X-1,1:Y-1]
    f_m[1:X-1,1:Y-1]   =    P[1:X-1,1:Y-1] -   ZUy[1:X-1,1:Y-1]
    g_p[1:X-1,1:Y-1]   = dy_P[1:X-1,1:Y-1] + dy_ZUy[1:X-1,1:Y-1]
    g_m[1:X-1,1:Y-1]   = dy_P[1:X-1,1:Y-1] - dy_ZUy[1:X-1,1:Y-1]

    fn_p[1:X-1,1:Y-1]  = CIP(coeff31[16], coeff31[17], coeff31[18], coeff31[19], \
                               f_p[1:X-1,0:Y-2], f_p[1:X-1,1:Y-1], \
                               g_p[1:X-1,0:Y-2], g_p[1:X-1,1:Y-1])
    gn_p[1:X-1,1:Y-1]  = CIP(coeff31[20], coeff31[21], coeff31[22], coeff31[23], \
                               f_p[1:X-1,0:Y-2], f_p[1:X-1,1:Y-1], \
                               g_p[1:X-1,0:Y-2], g_p[1:X-1,1:Y-1])
    fn_m[1:X-1,1:Y-1]  = CIP(coeff31[24], coeff31[25], coeff31[26], coeff31[27], \
                               f_m[1:X-1,2:Y],   f_m[1:X-1,1:Y-1], \
                               g_m[1:X-1,2:Y],   g_m[1:X-1,1:Y-1])
    gn_m[1:X-1,1:Y-1]  = CIP(coeff31[28], coeff31[29], coeff31[30], coeff31[31], \
                               f_m[1:X-1,2:Y],   f_m[1:X-1,1:Y-1], \
                               g_m[1:X-1,2:Y],   g_m[1:X-1,1:Y-1])

    P[1:X-1,1:Y-1]     = (fn_p[1:X-1,1:Y-1] + fn_m[1:X-1,1:Y-1]) 
    ZUy[1:X-1,1:Y-1]    = (fn_p[1:X-1,1:Y-1] - fn_m[1:X-1,1:Y-1]) 
    dy_P[1:X-1,1:Y-1]  = (gn_p[1:X-1,1:Y-1] + gn_m[1:X-1,1:Y-1]) 
    dy_ZUy[1:X-1,1:Y-1] = (gn_p[1:X-1,1:Y-1] - gn_m[1:X-1,1:Y-1]) 

end = time.time()

print("Processing Time : " + str((end - start)) + " [sec]")

