import math
import matplotlib.pyplot as plt

#Flags=-fetch:ifqsize
fetch_ifqsize_xVals=[1, 2, 4, 8, 16, 32, 64, 128, 256]
fetch_ifqsize_yVals=[487397825.10940003, 327129097.34143335, 288576715.4845333, 287762430.68576664, 288280212.4538, 289305888.4220333, 290081293.0168667, 291141391.732, 292355368.1364667]
#Flags=-ruu:size
ruu_size_xVals=[2, 4, 8, 16, 32, 64, 128, 256]
ruu_size_yVals=[431122329.4824, 355002897.00303334, 306438220.39056665, 288583828.5056667, 312834964.3812, 350209334.7835667, 411763141.0093667, 531732322.21643335]
#Flags=-lsq:size
lsq_size_xVals=[2, 4, 8, 16, 32, 64, 128, 256]
lsq_size_yVals=[354460443.9352667, 308513729.0169, 288580986.12170005, 288158131.18256664, 289581648.4488333, 292505918.46723336, 298613618.52786666, 310830844.0915]
#Flags=-res:ialu
res_ialu_xVals=[1, 2, 3, 4, 5, 6, 7, 8]
res_ialu_yVals=[337304092.06983334, 271296015.25333333, 271092495.81513333, 288570659.5694333, 307268612.6034, 325807205.15136665, 344233494.2938, 362539557.5267]
#Flags=-res:imult
res_imult_xVals=[1, 2, 3, 4, 5, 6, 7, 8]
res_imult_yVals=[288583194.3606667, 288576684.8710334, 288580152.9146, 288577378.7692334, 288576982.4639333, 288574802.88556665, 288580248.92973334, 288576152.68716663]
#Flags=-res:fpalu
res_fpalu_xVals=[1, 2, 3, 4, 5, 6, 7, 8]
res_fpalu_yVals=[280611882.02783334, 283196904.6643, 285883658.67249995, 288566759.74736667, 291281123.56159997, 293966141.43126667, 296643320.3627667, 299293092.8083667]
#Flags=-res:fpmult
res_fpmult_xVals=[1, 2, 3, 4, 5, 6, 7, 8]
res_fpmult_yVals=[288584242.9711333, 287656746.64140004, 287858787.2126333, 287442492.19423336, 287443633.3115334, 287453423.2342333, 287438984.4864333, 287452230.2354]


scale = lambda listVals: [math.log(i, 2) for i in listVals]
plt.title("Energy Consumption with respect to increasing a parameter size")
plt.ylabel("avg total_power_cycle_cc1")
"""
plt.xlabel("log2(size of parameter)")
plt.plot(scale(fetch_ifqsize_xVals), fetch_ifqsize_yVals)
plt.plot(scale(ruu_size_xVals), ruu_size_yVals)
plt.plot(scale(lsq_size_xVals), lsq_size_yVals)
plt.legend(['fetch:ifqsize', 'ruu:size', 'lsq:size'],loc='upper left')
"""

plt.xlabel("size of parameter")
plt.plot(res_ialu_xVals, res_ialu_yVals)
plt.plot(res_imult_xVals, res_imult_yVals)
plt.plot(res_fpalu_xVals, res_fpalu_yVals)
plt.plot(res_fpmult_xVals, res_fpmult_yVals)
plt.legend(['res:ialu', 'res:imult', 'res:fpalu', 'res:fpmult'], loc='upper left')
plt.show()







