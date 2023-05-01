
# CALCULATION FOR THE LOAD REGULATION
VNL= float(input("enter the no load voltage of your circuit"))
VFL= float(input("enter the Full load voltage of your circuit"))
load_regulation = ((VNL-VFL)/VFL)*100                             #in percentage
print("load regulation in percentage",load_regulation,"%")

# CALCULATION FOR THE LINE REGULATION
Vin_min =float(input("enter the minimum input voltage of your circuit"))
Vin_max =float(input("enter the maximum input voltage of your circuit"))
V_out1= float(input("enter the output volt corresponding to minimum input voltage of your circuit"))
V_out2= float(input("enter the output volt corresponding to maximum input voltage of your circuit"))

delta_vin = Vin_max- Vin_min
delta_vout= abs(V_out1- V_out2)
line_regulation = ((delta_vout/V_out1)/delta_vin)*100          # units in %/V
print("line regulation in percentage per volt",line_regulation,"%/V")

# CALCULATION FOR THE RISE IN TEMPERATURE ABOVE THE AMBIENT TEMPERATURE
V_out= float(input("enter the output voltage of your circuit"))
I_out_max= float(input("enter the maximum output/load current of your circuit"))
T_amb= float(input("enter the value of ambient temperature")) 
I_GND= float(input("enter the ground pin current of your circuit"))  
# GND pin current depends on the load current and the input voltage
# for example:  IGND at (IOUT = 50mA, VIN = 30V) = 1mA for IC LT3010

Ther_res =50  # units in °C/W, approximated value.
# The thermal resistance will be in the range of 40°C/W to 62°C/W depending on the copper area for the IC LT3010.

P = I_out_max*(Vin_max-V_out) + I_GND* Vin_max         #power dissipation
rise_temp = P*Ther_res
print("the junction temperature rise above ambient temperature will be approximately equal to:",rise_temp,"°C")

T_jun_max = T_amb+rise_temp
print("The maximum junction temperature will be equal to",T_jun_max,"°C")
#The maximum junction temperature will then be equal to the maximum junction temperature rise above ambient plus the maximum ambient temperature







