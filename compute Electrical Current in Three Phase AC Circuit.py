from math import cos,acos,sqrt
R = 20.;#  in ohm
X_L = 15.;#  in ohm
V_L = 400.;#  in V
f = 50.;#  in Hz
#calculations
V_Ph = V_L/sqrt(3);#  in V
Z_Ph = sqrt( (R**2) + (X_L**2) );#  in ohm
I_Ph = V_Ph/Z_Ph;#  in A
I_L = I_Ph;#  in A
print( "The line current in A is",round(I_L,2))
# pf = cos(phi) = R_Ph/Z_Ph;
R_Ph = R;#  in ohm
phi= acos(R_Ph/Z_Ph);
#  Power factor
pf= cos(phi);#  in radians
print ("The power factor is : ",pf,"degrees lag.")
P = sqrt(3)*V_L*I_L*cos(phi);#  in W
print ("The power supplied in W is",P)
