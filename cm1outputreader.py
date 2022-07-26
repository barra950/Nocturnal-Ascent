#from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset,num2date
import datetime
from myfunctions import maxmin



#This part gets the parcel data but its not necessary

rootgrp = Dataset('cm1out_pdata.nc','r')

dims = rootgrp.dimensions

vars = rootgrp.variables

attrs = rootgrp.ncattrs

ndims = len(dims)

print ('number of dimensions = ' + str(ndims))

for key in dims:
    print ('dimension['+key+'] = ' +str(len(dims[key])))

gattrs = rootgrp.ncattrs()
ngattrs = len(gattrs)

print ('number of global attributes = ' + str(ngattrs))

for key in gattrs:
    print ('global attribute['+key+']=' + str(getattr(rootgrp,key)))

vars = rootgrp.variables
nvars = len(vars)
print ('number of variables = ' + str(nvars))

for var in vars:
    print ('---------------------- variable '+var+'----------------')
    print ('shape = ' + str(vars[var].shape))
    vdims = vars[var].dimensions
    for vd in vdims:
        print ('dimension['+vd+']=' + str(len(dims[vd])))
        

xparcel= vars['x'][:]
yparcel= vars['y'][:]
zparcel= vars['z'][:]



########################################################################################################################


#This part reads the output from the model


rootgrp = Dataset('cm1out.nc','r')

dims = rootgrp.dimensions

vars = rootgrp.variables

attrs = rootgrp.ncattrs

ndims = len(dims)

print ('number of dimensions = ' + str(ndims))

for key in dims:
    print ('dimension['+key+'] = ' +str(len(dims[key])))

gattrs = rootgrp.ncattrs()
ngattrs = len(gattrs)

print ('number of global attributes = ' + str(ngattrs))

for key in gattrs:
    print ('global attribute['+key+']=' + str(getattr(rootgrp,key)))

vars = rootgrp.variables
nvars = len(vars)
print ('number of variables = ' + str(nvars))

for var in vars:
    print ('---------------------- variable '+var+'----------------')
    print ('shape = ' + str(vars[var].shape))
    vdims = vars[var].dimensions
    for vd in vdims:
        print ('dimension['+vd+']=' + str(len(dims[vd])))

#133 
#172      
limit = 133
#rain = vars['rain'][:limit]
P= vars['prs'][:limit] #pressure
#Ppert= vars['prspert'][:limit] #pressure perturbation
#Pi= vars['pi'][:limit] #nondimensional pressure (exner function)
#Pipert= vars['pipert'][:limit] #nondimensional pressure perturbation (exner function

# PGFpertwPi = vars['wb_pgrad'][:limit] #pressure gradient term in the CM1 w equation
# Bw = vars['wb_buoy'][:limit] #buoyancy in the CM1 w equation
# hadvw = vars['wb_hadv'][:limit] #horizontal advection in the CM1 w equation
# vadvw = vars['wb_vadv'][:limit] #vertical advection in the CM1 w equation
# whturb = vars['wb_hturb'][:limit] #horizontal turbulence tendency in the CM1 w equation
# wvturb = vars['wb_vturb'][:limit] #vertical turbulence tendency in the CM1 w equation
# wrdamp = vars['wb_rdamp'][:limit] #rayleigh damping tendency in the CM1 w equation
# hidiffw = vars['wb_hidiff'][:limit] #horizontal diffusion term in the w equation
# vidiffw = vars['wb_vidiff'][:limit] #vertical diffusion term in the w equation

PGFpertuPi = vars['ub_pgrad'][:limit] #pressure gradient term in the CM1 u equation
fcoru = vars['ub_cor'][:limit] #coriolis term in the CM1 u equation
urdamp = vars['ub_rdamp'][:limit] #rayleigh damping term in the CM1 u equation
hadvu = vars['ub_hadv'][:limit] #horizontal advection in the CM1 u equation
vadvu = vars['ub_vadv'][:limit] #vertical advection in the CM1 u equation
uhturb = vars['ub_hturb'][:limit] #horizontal turbulence tendency in the CM1 u equation
uvturb = vars['ub_vturb'][:limit] #vertical turbulence tendency in the CM1 u equation
upblten = vars['ub_pbl'][:limit] #pbl tendency in the CM1 u equation
uidiff = vars['ub_hidiff'][:limit] #Diffusion (incuding artificial) in the CM1 u equation

PGFpertvPi = vars['vb_pgrad'][:limit] #pressure gradient term in the CM1 v equation
fcorv = vars['vb_cor'][:limit] #coriolis term in the CM1 v equation
vrdamp = vars['vb_rdamp'][:limit] #rayleigh damping term in the CM1 v equation
hadvv = vars['vb_hadv'][:limit] #horizontal advection in the CM1 v equation
vadvv = vars['vb_vadv'][:limit] #vertical advection in the CM1 v equation
vhturb = vars['vb_hturb'][:limit] #horizontal turbulence tendency in the CM1 v equation
vvturb = vars['vb_vturb'][:limit] #vertical turbulence tendency in the CM1 v equation
vpblten = vars['vb_pbl'][:limit] #pbl tendency in the CM1 v equation
vidiff = vars['vb_hidiff'][:limit] #Diffusion (incuding artificial) in the CM1 v equation


xh= vars['xh'][:] #x coordinate
yh= vars['yh'][:] #y cooordinate
xf= vars['xf'][:] #extra x coordinate
yf= vars['yf'][:] #extra y coordinate
#z= vars['z'][:limit] #height
z= vars['zh'][:] #height (use only for version 20.2 of cm1)
#zh=vars['zh'][:limit] #height on nominal levels (use for plots if terrain is not flat and in version 19.8)
zh=vars['zhval'][:limit] #height on nominal levels (use for plots if terrain is not flat and in version 20.2)
u= vars['u'][:limit] #u wind
#u= vars['ua'][:limit] #u wind (for restart runs only)
v= vars['v'][:limit] #v wind
#v= vars['va'][:limit] #v wind (for restart runs only)
w= vars['w'][:limit] #vertical velocity
#w= vars['wa'][:limit] #vertical velocity (for restart runs only)
#dbz= vars['dbz'][:limit] #reflectivity
time= vars['time'][:limit] #time 
theta= vars['th'][:limit] #potential temperature
#theta= vars['tha'][:limit] #potential temperature (for restart runs only)
thpert= vars['thpert'][:limit] #potential temperature perturbation
#N= np.sqrt(vars['nm'][:limit]) #brunt-vaisala frequency 
B= vars['buoyancy'][:limit] #buoyancy
rho= vars['rho'][:limit] #dry air density
#zs= vars['zs'][:limit] #height of the terrain
solrad= vars['swten'][:limit] #heating from shortwaves (K/s)
#swdnt= vars['swdnt'][:limit] #heating from shortwaves (K/s)
#solrad= vars['swdnt'][:limit] #incoming solar radiation
#thpert= vars['thpert'][:limit] #potential temperature perturbation
#cloud= vars['cldfra'][:limit] #cloud fraction
#mavail= vars['mavail'][:limit] #moisture availability
#lu0= vars['lu'][:limit] #subgrid tke
#xland= vars['xland'][:limit] #1 for land and 2 for water
#z0= vars['znt'][:limit] #surface roughness length
qv= vars['qv'][:limit] #water vapor mixing ratio
tke= vars['xkzm'][:limit] #subgrid tke
#km= vars['kmh'][:limit] #subgrid eddy viscosity (eddy diffusivity for momentum)
#kh= vars['khh'][:limit] #subgrid eddy diffusivity (eddy diffusivity for temperature)





#Make a datetime array
time1=[]
for k in range(0,len(time)):
    time1.append(datetime.datetime(2019, 6, 25, 0, 30, 0) + datetime.timedelta(seconds=int(time[k]))  )
    
time1=np.array(time1)



#Converts from seconds to readable time
def convert(timeinsecs):
   time = timeinsecs
   day = time // (24 * 3600)
   time = time % (24 * 3600)
   hour = time // 3600
   time %= 3600
   minutes = time // 60
   time %= 60
   seconds = time
   return("Day %d at %d:%d:%d" % (day, hour, minutes, seconds))





#Makes a readable time array (different from time1)
time2=[]
for k in range(0,len(time)):
    time2.append(convert(time[k]+1800+86400))
time2=np.array(time2)

#%%

#Calculates the virtual potential temperature
#thetaV = theta * (1 + 0.61*qv )





##Print Pressure  (horizontal section)
#X=np.linspace(-59,59,60)
#Y=np.linspace(-59,59,60)
#
#xm,ym=np.meshgrid(X,Y)
#
#plt.contourf(xm,ym,P[5][0],cmap='CMRmap')
#
#plt.colorbar()
#
#plt.xlabel('x axis')
#plt.ylabel('y axis')

#%%
#Prints potential temperature profile
plt.figure()
plt.rcParams.update({"font.size": 16})
plt.plot(theta[0,:,0,0],z,linewidth=3,color='b')
plt.xlabel('Potential temperature (K)',name='Arial',size=20,style='italic')
plt.ylabel('Height (km)',name='Arial',size=20,style='italic')
#plt.ylim([0,4])
#plt.xlim([290,335])
plt.grid('True')

#%%
#Prints mixing ratio profile
plt.figure()
plt.rcParams.update({"font.size": 16})
plt.plot(qv[0,:,0,0],z,linewidth=3,color='b')
plt.xlabel('Water vapor mixing ratio ($kgkg^{-1}$)',name='Arial',size=20,style='italic')
plt.ylabel('Height (km)',name='Arial',size=20,style='italic')
plt.ylim([0,14])
plt.xlim([0,0.001])
plt.grid('True')


#%%

##Print U, V and W winds (horizontal section )
#xm,ym = np.meshgrid(xf,yh)
#
#xn,yn = np.meshgrid(xh,yf)
#
#xw,yw = np.meshgrid(xh,yh)
#
#
#
##plt.contourf(xm,ym,u[30,10,:,:],cmap='CMRmap')
##plt.contourf(xn,yn,v[30,10,:,:],np.arange(0,20,1),cmap='CMRmap')
#plt.contourf(xw,yw,w[50,10,:,:],cmap='seismic')
#
#plt.colorbar()
#
#plt.xlabel('x axis')
#plt.ylabel('y axis')



##Print Reflectivity (horizontal section)
#X=np.linspace(-59,59,60)
#Y=np.linspace(-59,59,60)
#
#xm,ym=np.meshgrid(X,Y)
#
#plt.contourf(xm,ym,dbz[5][20],cmap='CMRmap')
#
#plt.colorbar()
#
#plt.xlabel('x axis')
#plt.ylabel('y axis')




##Print U and V winds (xz section )
#xmv,zmv=np.meshgrid(xh,z)
##xmu,zmu=np.meshgrid(xf,z)
#
#
##plt.contourf(xmu,zmu,u[120,:,50,:],np.arange(-10,10,0.1),cmap='CMRmap')
##plt.colorbar()
##plt.contour(xmu,zmu,u[96,:,100,:],np.arange(0,20,1),colors='k')
#
#
#plt.contourf(xmv,zmv,v[90,:,1,:],np.arange(0,20,0.1),cmap='CMRmap')
#plt.colorbar()
##plt.contour(xmv,zmv,v[5,:,1,:],np.arange(0,20,1),colors='k')
#
#
#plt.xlabel('x axis')
#plt.ylabel('z axis')



#Animation of U or V winds (xz section )
#xm,zm=np.meshgrid(xh,z)
#
##Comment/uncomment this part for terrain following coordinates or not (dont use this anymore)
##for k in zmv:
##    for t in range(0,len(k)):
##        k[t] = k[t] + zs[0,0,t]/1000.0
##for k in zmu:
##    for t in range(0,len(k)-1):
##        k[t] = k[t] + zs[0,0,t]/1000.0
#        
#        
#        
#for k in range(0,len(v),5):
#    
#    
##    plt.contourf(xm,zh[0,:,0,:],u[k,:,1,:-1],np.arange(-10,10,0.1),cmap='seismic')
##    plt.colorbar()
#    #plt.contour(xmu,zmu,u[96,:,100,:],np.arange(0,20,1),colors='k')
#    
#    
#    plt.contourf(xm,zh[0,:,0,:],v[k,:,1,:],np.arange(0,20,0.1),cmap='CMRmap')
#    plt.colorbar(label='Wind Speed (m/s)')
#    #plt.contour(xmv,zmv,v[5,:,1,:],np.arange(0,20,1),colors='k')
#    
#    
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    
#    
#    plt.pause(0.5)
#    plt.clf()




#Print Potential temperature or potential temp perturbation (xz section)
#xm,zm=np.meshgrid(xh,z)
##
##
###Comment/uncomment this part for terrain following coordinates or not (dont use this anymore)
###for k in zm:
###    for t in range(0,len(k)):
###        k[t] = k[t] + zs[0,0,t]/1000.0
##
#ax = plt.gca()
#
#plt.contourf(xm,zh[0,:,0,:],theta[0,:,0,:],np.arange(290,330,0.5),cmap='CMRmap')
##plt.contourf(xm,zm,thpert[0,:,0,:],np.arange(0,8.1,0.1),cmap='CMRmap')
##plt.contourf(xm,zh,theta[0,:,0,:],np.arange(290,330,0.5),cmap='CMRmap')
#ax.set_xlim([-1000,1000])
##
###To be used fr testing only
###ttheta = abs( abs(xm*1000)-np.amax(xm)*1000 )/371062# + abs( zm*1000-np.amax(zm)*1000 )/5000.0
###ttheta = -(xm*1000)*8/1000000 - zm*1000*8/2000.0 + 8
###plt.contourf(xm,zm,ttheta,np.arange(0,8,0.1),cmap='CMRmap')
##
##
#plt.colorbar()
#
#plt.xlabel('x axis')
#plt.ylabel('z axis')







#Print Pressure (xz section)
#xm,zm=np.meshgrid(xh,z)
#
##Comment/uncomment this part for terrain following coordinates or not (dont use this anymore)
##for k in zm:
##    for t in range(0,len(k)):
##        k[t] = k[t] + zs[0,0,t]/1000.0
#
#
#
#plt.contourf(xm,zh[0,:,0,:],P[0,:,0,:],cmap='CMRmap')
#
#
#plt.colorbar()
#
#plt.xlabel('x axis')
#plt.ylabel('z axis')






#Animation of potential temperature (or perturbation) (xz section )
#xm,zm=np.meshgrid(xh,z)
#
#
##Comment/uncomment this part for terrain following coordinates or not (dont use this anymore)
##for k in zm:
##    for t in range(0,len(k)):
##        k[t] = k[t] + zs[0,0,t]/1000.0
#        
# 
#              
#for k in range(0,len(theta),5):
#    
#    
#    #plt.contourf(xm,zh[0,:,0,:],theta[k,:,0,:],np.arange(290,330,0.5),cmap='CMRmap')
#    #plt.colorbar()
#    
#    plt.contourf(xm,zh[0,:,0,:],theta[k,:,0,:]-theta[0,:,0,:],np.arange(-10,10,0.1),cmap='seismic')
#    plt.colorbar()
#    
#    
#    
#    
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    
#    
#    plt.pause(0.5)
#    plt.clf()





#Animation of U or V winds, potential temperature and pressure (xz section)
#xm,zm=np.meshgrid(xh,z)
#
##Comment/uncomment this part for terrain following coordinates or not (dont use this anymore)
##for k in zmv:
##    for t in range(0,len(k)):
##        k[t] = k[t] + zs[0,0,t]/1000.0
##for k in zmu:
##    for t in range(0,len(k)-1):
##        k[t] = k[t] + zs[0,0,t]/1000.0
##for k in zm:
##    for t in range(0,len(k)):
##        k[t] = k[t] + zs[0,0,t]/1000.0
#        
#        
#        
#for k in range(0,len(time),4):
#    
#    #plt.figure()
#    
#    plt.subplot(2,1,1)
#    plt.contourf(xm,zm,u[k,:,0,:-1],np.arange(-10,10.1,0.1),cmap='seismic')
#    plt.colorbar(label='Wind Speed (m/s)')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
##    plt.subplot(2,1,1)
##    plt.contourf(xm,zm,v[k,:,0,:],np.arange(0,21.1,0.1),cmap='CMRmap')
##    plt.colorbar(label='Wind Speed (m/s)')
##    plt.title(time1[k],name='Arial',weight='bold',size=20)
##    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
##    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
#    plt.subplot(2,1,2)
#    wndspeed = np.sqrt(np.array(v[:,:,0:3,:])**2   +  np.array(u[:,:,0:3,:-1])**2)
#    plt.contourf(xm,zm,wndspeed[k,:,0,:],np.arange(0,20.1,0.1),cmap='CMRmap')
#    plt.colorbar(label='Wind Speed (m/s)')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
#    
##    plt.subplot(2,1,1)
##    plt.contourf(xm,zm,thpert[k,:,0,:],np.arange(-10,10.5,0.5),cmap='seismic')
##    plt.colorbar(label='Potential temperature (K)')
##    plt.title(time2[k],name='Arial',weight='bold',size=20)
##    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
##    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
##   
##    plt.subplot(2,1,2)
##    plt.contourf(xm,zm,B[k,:,0,:],np.arange(-0.4,0.42,0.02),cmap='seismic')
##    plt.colorbar(label='Buoyancy ($s^{-2}$)')
##    plt.title(time1[k],name='Arial',weight='bold',size=20)
##    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
##    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
##    plt.subplot(2,1,2)
##    plt.contourf(xm,zh[0,:,0,:],P[k,:,0,:]-P[0,:,0,:],np.arange(-350,350,10),cmap='seismic')
##    plt.colorbar(label='Presure Perturbaion (Pa)')
##    plt.title(time1[k],name='Arial',weight='bold',size=20)
##    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
##    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
##    plt.subplot(2,1,2)
##    plt.contourf(xm,zm,cloud[k,:,0,:],cmap='seismic')
##    plt.colorbar(label='Cloud Fraction (Pa)')
##    plt.title(time1[k],name='Arial',weight='bold',size=20)
##    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
##    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
##    plt.subplot(2,1,2)
##    plt.contourf(xm,zm,w[k,:-1,0,:],np.arange(-0.1,0.11,0.01),cmap='seismic')
##    plt.colorbar(label='Vertical velocity (m/s)')
##    plt.title(time1[k],name='Arial',weight='bold',size=20)
##    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
##    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
##    
##    plt.subplot(2,1,2)
##    plt.contourf(xm,zm,qv[k,:,0,:],np.arange(0,0.0075,0.0001),cmap='CMRmap')
##    plt.colorbar(label='Water vapor mixing ratio')
##    plt.title(time2[k],name='Arial',weight='bold',size=20)
##    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
##    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#
#    
#    plt.subplot(2,1,2)
#    plt.contourf(xm,zh[0,:,0,:],tke[k,:-1,0,:],np.arange(0,30,1),cmap='CMRmap')
#    plt.colorbar(label='Subgrid TKE')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
##    plt.subplot(2,1,2)
##    plt.contourf(xm,zm,PGFx[k,:,0,:],np.arange(-5,5.1,0.1),cmap='seismic')
##    plt.colorbar(label='Pressure gradient')
##    plt.title(time1[k],name='Arial',weight='bold',size=20)
##    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
##    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
#    
#  
#    plt.pause(0.5)
#    nameoffigure = time2[k]
#    string_in_string = "{}".format(nameoffigure)
#    plt.savefig(string_in_string)
#    plt.clf()   
    
    







#Print Reflectivity (xz section)
#xm,zm=np.meshgrid(xh,z)
#
#plt.contourf(xm,zm,dbz[190,:,1,:],cmap='CMRmap')
#
#
#plt.colorbar()
#
#plt.xlabel('x axis')
#plt.ylabel('z axis')









#Print Pressure (xz section)
#xm,zm=np.meshgrid(xh,z)
#
#plt.contourf(xm,zm,P[0,:,50,:],np.arange(32473,100115,1000),cmap='CMRmap')
#
#
#plt.colorbar()
#
#plt.xlabel('x axis')
#plt.ylabel('z axis')









#Print V wind in function of time and height
#plt.title('v wind in function of time and height')
#zv,tv=np.meshgrid(z,time)
#plt.contourf(tv,zv,np.nanmean(v[:,:,:,:],axis=(2,3)),np.arange(0,20,1),cmap='CMRmap')
#plt.colorbar()
#
#
#plt.xlabel('time (seconds)')
#plt.ylabel('height (km)')




#%%
# time=time[0:85]
# time2=time2[0:85]
# zh=zh[0:85]
# u=u[0:85]
# v=v[0:85]
#Print wind speed in function of time and height
fig = plt.figure()
plt.rcParams.update({"font.size": 16})
#plt.title('Wind Speed as a Function of Time and Height',weight='bold',name='Arial',size=20)
wndspeed = np.sqrt(np.array(v[:,:,0:3,:])**2   +  np.array(u[:,:,0:3,:-1])**2)
zv,tv=np.meshgrid(z,time)
#field = plt.contourf(tv,zv,np.nanmean(wndspeed[:,:,:,:],axis=(2,3)),np.arange(0,20,1),cmap='CMRmap')
#ufield = plt.contourf(tv,zv,np.nanmean(u[:,:,:,:],axis=(2,3)),np.arange(-10,10,1),cmap='CMRmap')
field2 = plt.contourf(tv,zv,np.nanmean(wndspeed[:,:,:,164:165],axis=(2,3)),np.arange(0,20,1),cmap='CMRmap')
#field2 = plt.contourf(tv,zva,np.nanmean(wndspeed[:,:,:,328],axis=(2)),np.arange(0,20,1),cmap='CMRmap')
#field2terrain = plt.contourf(tv,zh[:,:,0,328]/1000,wndspeed[:,:,0,328],np.arange(0,21,1),cmap='CMRmap')
cbar = plt.colorbar()
cbar.set_label("Wind Speed ($ms^{-1}$)", name='Arial',size=18)
plt.xticks(time[0:len(time):4], time2[0:len(time):4], rotation='vertical')
plt.ylabel('Height (km)',size=20,style='italic')
plt.gcf().autofmt_xdate()
plt.ylim([0,10])
#plt.ylim([977/1000,4000/1000])
#plt.yticks(np.arange(0,5,1))
#plt.contour(field,np.arange(0,20,1),colors='k')
#plt.clabel(field,inline=False,fontsize=8,colors='k')
#plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')

#%%
#Print ageostrophic wind speed in function of time and height
fig = plt.figure()
#plt.title('Ageostrophic Wind Speed in Function of Time and Height',name='Arial',weight='bold',size=20)
awndspeed = np.sqrt((v[:,:,0:3,:]-10.0)**2   +  (u[:,:,0:3,:-1])**2)
zv,tv=np.meshgrid(z,time)
field = plt.contourf(tv,zv,np.nanmean(awndspeed[:,:,:,:],axis=(2,3)),np.arange(0,9.5,0.2),cmap='inferno')
#field2 = plt.contourf(tv,zv,np.nanmean(awndspeed[:,:,:,165:170],axis=(2,3)),np.arange(0,9.5,0.2),cmap='inferno')
cbar = plt.colorbar()
cbar.set_label("Wind Speed ($ms^{-1}$)", name='Arial',size=18)
plt.xticks(time[0:len(time):5], time2[0:len(time):5], rotation='vertical')
plt.gcf().autofmt_xdate()
plt.ylim([0,4])
#plt.contour(field,np.arange(0,20,1),colors='k')
#plt.clabel(field,inline=False,fontsize=8,colors='k')

plt.ylabel('Height (km)',name='Arial',size=18,style='italic')
#%%

#Print potential temperature in function of time and height
#plt.title('Potential Temperature in Function of Time and Height',name='Arial',weight='bold',size=20)
#zv,tv=np.meshgrid(z,time)
#field = plt.contourf(tv,zv,np.nanmean(theta[:,:,:,:],axis=(2,3)),np.arange(280,340,1),cmap='CMRmap')
#plt.colorbar(label='Potential Temperature (K)')
#plt.xticks(time[0:len(time):19], time2[0:len(time):19], rotation='vertical')
#plt.gcf().autofmt_xdate()
##plt.contour(field,np.arange(0,20,1),colors='k')
##plt.clabel(field,inline=False,fontsize=8,colors='k')
#
#plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')



#Print vertical motion in function of time and height
# plt.figure()
# plt.title('Vertical motion in Function of Time and Height',name='Arial',weight='bold',size=20)
# zv,tv=np.meshgrid(z,time)
# field = plt.contourf(tv,zv,np.nanmean(w[:,:-1,:,159:160],axis=(2,3)),np.arange(-0.05,0.051,0.001),cmap='seismic')
# plt.colorbar(label='Vertical motion (m/s)')
# plt.xticks(time[6:len(time):3], time2[6:len(time):3], rotation='vertical')
# plt.gcf().autofmt_xdate()
# #plt.contour(field,np.arange(0,20,1),colors='k')
# #plt.clabel(field,inline=False,fontsize=8,colors='k')

# plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')










#Plots the height of the terrain
#plt.plot(xh,zs[0,1,:]/1000,color='k',linewidth=5)
#ax = plt.gca()
##ax.set_xticks(np.linspace(np.amin(xh),np.amax(xh),5))
##ax.set_ylim([0,9])
#plt.xlabel('X-Extent of Domain (km)',name='Arial',weight='bold',size=15,style='italic')
#plt.ylabel('Height (km)',name='Arial',weight='bold',size=15,style='italic')
#plt.grid(True)



#Plots the moisture avaliability 
#plt.plot(xh,mavail[0,1,:],color='k',linewidth=5)
#ax = plt.gca()
#plt.xlabel('X-Extent of Domain (km)',name='Arial',weight='bold',size=15,style='italic')
#plt.ylabel('Moisture Avaliability (km)',name='Arial',weight='bold',size=15,style='italic')
#plt.grid(True)



#Plots the u and v wind with height at a certain point
#plt.plot(v[150,:,0,1100],z,label='V wind')
#plt.plot(u[150,:,0,1100],z,label='U wind')
#plt.xlabel('Wind speed (m/s)')
#plt.ylabel('height (km)')
#ax = plt.gca()
#ax.set_xlim([0,20])
#ax.set_xticks(np.arange(0,21,1))
#ax.set_ylim([0,9])
#ax.set_yticks(np.arange(0,10,1))
#plt.grid(True)
#plt.legend()


#Ignore this
#ax = plt.gca()
#plt.plot(time1,[1]*len(time1))
#plt.gcf().autofmt_xdate()
#ax.xaxis.set_major_locator(plt.MaxNLocator(10))



#Plots the U wind at certain times
# fig=plt.figure(figsize=(10,10))
# ax=fig.add_subplot(1,1,1)
# #fig.suptitle("U Wind ",name='Arial',weight='bold',size=20)
# #plt.title('U Wind Profiles',name='Arial',weight='bold',size=20)
# plt.plot(u[70,:,0,0],z,label='22:30 local time')
# plt.plot(u[72,:,0,0],z,label='00:30 local time')
# plt.plot(u[74,:,0,0],z,label='02:30 local time')
# plt.plot(u[76,:,0,0],z,label='04:30 local time')
# plt.xlabel('U wind (m/s)',name='Arial',weight='bold',size=16,style='italic')
# plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
# plt.legend()
# ax.set_xlim([-10,20])
# ax.set_ylim([0,2])
    

#%%
#Plots the u and v wind ratio with time at a certain heights
plt.rcParams.update({"font.size": 16})
plt.figure(figsize=(20,20))
xposition = 0
init_time = 44  
final_time = 68  
sunrise_time = 53  #was 54 for old 40km run
zposition1 = 44 #height1  was 19 for old 40km run
zposition2 = 94 #height2  was 44 for old 40km run
#plt.title('LLJ Winds at Distinct Heights',name='Arial',weight='bold',size=20)
plt.plot(u[init_time:final_time + 1,zposition1,0,xposition],v[init_time:final_time + 1,zposition1,0,xposition],label='900m',linestyle = ':',c='r')
plt.plot(u[init_time:final_time + 1,zposition2,0,xposition],v[init_time:final_time + 1,zposition2,0,xposition],label='1900m',linestyle = ':',c='b')

#plt.plot(u[init_time,0:100,0,xposition],v[init_time,0:100,0,xposition],label='ratao',c='k')

plt.plot(u[init_time,zposition1,0,xposition],v[init_time,zposition1,0,xposition],label='20:30 LST',color='white',marker='*',markersize=25,markerfacecolor='purple')
plt.plot(u[init_time + 8,zposition1,0,xposition],v[init_time + 8,zposition1,0,xposition],label='04:30 LST',color='white',marker='*',markersize=25,markerfacecolor='green')
plt.plot(u[init_time + 16,zposition1,0,xposition],v[init_time + 16,zposition1,0,xposition],label='12:30 LST',color='white',marker='*',markersize=25,markerfacecolor='crimson')
plt.plot(u[init_time + 24,zposition1,0,xposition],v[init_time + 24,zposition1,0,xposition],label='20:30 LST',color='white',marker='*',markersize=25,markerfacecolor='k')
plt.plot(u[sunrise_time,zposition1,0,xposition],v[sunrise_time,zposition1,0,xposition],label='Sunrise',color='white',marker='*',markersize=25,markerfacecolor='orange')

plt.plot(u[init_time,zposition2,0,xposition],v[init_time,zposition2,0,xposition],color='white',marker='*',markersize=25,markerfacecolor='purple')
plt.plot(u[init_time + 8,zposition2,0,xposition],v[init_time + 8,zposition2,0,xposition],color='white',marker='*',markersize=25,markerfacecolor='green')
plt.plot(u[init_time + 16,zposition2,0,xposition],v[init_time + 16,zposition2,0,xposition],color='white',marker='*',markersize=25,markerfacecolor='crimson')
plt.plot(u[init_time + 24,zposition2,0,xposition],v[init_time + 24,zposition2,0,xposition],color='white',marker='*',markersize=25,markerfacecolor='k')
plt.plot(u[sunrise_time,zposition2,0,xposition],v[sunrise_time,zposition2,0,xposition],color='white',marker='*',markersize=25,markerfacecolor='orange')

plt.plot([0],[10],label='Geostrophic wind',color='white',marker='*',markersize=25,markerfacecolor='y')
plt.xlabel('U wind ($ms^{-1}$)',name='Arial',size=18,style='italic')
plt.ylabel('V wind ($ms^{-1}$)',name='Arial',size=18,style='italic')
# plt.xlim([-5,5])
# plt.ylim([5,15])


#plt.xlim([-4,4])
#plt.ylim([5,14])
plt.legend(loc = 1)
plt.grid(True)
#%%   

############################################################################## 
    
#Plots the solar radiation
plt.rcParams.update({"font.size": 16})
time_len = 24
plt.figure()
plt.plot(time[0:time_len],solrad[0:time_len,209,0,0],linewidth=3,color='k')
plt.plot(time[5],solrad[5,209,0,0],label='Sunrise',color='white',marker='*',markersize=20,markerfacecolor='orange')
plt.plot(time[20],solrad[20,209,0,0],label='Sunset',color='white',marker='*',markersize=20,markerfacecolor='red')
plt.xticks(time[0:time_len:1], time2[0:time_len:1], rotation='vertical')
plt.gcf().autofmt_xdate()
plt.ylabel('Heating from shortwaves at the top of the atmosphere ($Ks^{-1}$)',name='Arial',size=20,style='italic')
#plt.xlim([0,20])
plt.grid('True')
plt.legend(fontsize=20)
#plt.plot(time,swdnt[:,0,0])


#%%
#Plots the soil characteristics
x= np.arange(-2000,2001,10)
MAVAIL = 0.3 - 0.23 * np.exp(-x**2/500**2)
ALBEDO = 0.15 + 0.07 * np.exp(-x**2/500**2)
THC = 0.04 + 0.015 * np.exp(-x**2/500**2)

plt.rcParams.update({"font.size": 16})
plt.plot(x,MAVAIL,linewidth=3,color='b',label='Mavail')
plt.plot(x,ALBEDO,linewidth=3,color='k',label='Albedo')
plt.plot(x,THC,linewidth=3,color='r',label='Thermal Inertia')
plt.grid('True')
plt.legend(fontsize=20)
plt.xlabel('X Domain (km)',name='Arial',size=20,style='italic')

 




    
#%%
############################################################################## 
    
#This part creates a new sounding from output data
#
#
#    
##Choosing the time index we are using to extract our profile
#timeindex = 50
#    
#    
##Transforming the arrays into lists to make it easier 
#zexp = []
#for k in z:
#    zexp.append(k*1000.0)
#    
#thetaexp = []
#for k in theta[timeindex,:,0,0]:
#    thetaexp.append(k)
#    
#    
#mixratioexp = []
#for k in qv[0,:,0,0]:
#    mixratioexp.append(k)
#    
#
#uwndexp = []
#for k in u[0,:,0,0]:
#    uwndexp.append(k)
#    
#vwndexp = []
#for k in v[0,:,0,0]:
#    vwndexp.append(k)
#    
#
#    
#
#
##Creating the variables that are going into the sounding in string form
#
#for k in range(0,len(zexp)):
#    
#    while len(str(zexp[k])) < 20:
#        zexp[k] = str(zexp[k]) + ' '
#    
#    while len(str(thetaexp[k])) < 20:
#        thetaexp[k] = str(thetaexp[k]) + ' '
#        
#    while len(str(mixratioexp[k])) < 20:
#        mixratioexp[k] = str(mixratioexp[k]) + ' '
#        
#    while len(str(uwndexp[k])) < 20:
#        uwndexp[k] = str(uwndexp[k]) + ' '
#        
#    while len(str(vwndexp[k])) < 20:
#        vwndexp[k] = str(vwndexp[k]) + ' '
#        
##Creating the surface values for each souding variable
#p0 = 1000.0
#
#theta0 = theta[timeindex,0,0,0]
#
#mixratio0 = 0.5       
#
#        
#        
##writing the new sounding 
#f = open('input_sounding.txt', 'w' )
#
#f.write(str(p0)+ '     '+ str(theta0)+ '     ' + str(mixratio0) + '     ' + '\n')
#
#for k in range(0,len(zexp)):
#    f.write(zexp[k]  + thetaexp[k] + mixratioexp[k] + uwndexp[k]  + vwndexp[k] + '\n'  )
#
#
#f.close() 


#############################################################################




   
#Animation of U or V winds and potential temperature (xz section )
#xmv,zmv=np.meshgrid(xh,z)
#xmu,zmu=np.meshgrid(xf,z)
#xm,zm=np.meshgrid(xh,z)
##
###Comment/uncomment this   part for terrain following coordinates or not
##for k in zmv:
##    for t in range(0,len(k)):
##        k[t] = k[t] + zs[0,0,t]/1000.0
##for k in zmu:
##    for t in range(0,len(k)-1):
##        k[t] = k[t] + zs[0,0,t]/1000.0
##for k in zm:
##    for t in range(0,len(k)):
##        k[t] = k[t] + zs[0,0,t]/1000.0
##        
##        
#        
#for k in range(0,len(time),5):
#    
#    
#    plt.figure()
#    
#    plt.subplot(1,2,1)
#    plt.contourf(xmu,zmu,u[k,:,1,:],np.arange(-10,10,0.1),cmap='seismic')
#    plt.colorbar(label='Wind Speed (m/s)')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
#    
#    plt.contourf(xmv,zmv,v[k,:,1,:],np.arange(0,20,0.1),cmap='CMRmap')
#    plt.colorbar(label='Wind Speed (m/s)')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
#    plt.subplot(1,2,2)
#    plt.contourf(xm,zm,theta[k,:,0,:],np.arange(290,330,0.5),cmap='CMRmap')
#    plt.colorbar(label='Potential temperature (K)')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    
#    plt.contourf(xm,zm,theta[k,:,0,:]-theta[0,:,0,:],np.arange(-10,10,0.1),cmap='seismic')
#    plt.colorbar(label='Potential temperature perturbation (K)')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
##    
##    
##    
##    
##    
##    
##    
#    plt.pause(0.5)
#    plt.clf()    


####################################################################################################################################

#Creating the plots of maximum intensity and height of w


#This plot only has the max w and max height for each day
# maxheight = []
# maxtime =[]
# maxintensity = []
# for k in range (0,len(w)-24,24):
#     maxtime.append(np.where(w[k:k+24,:,:,:] == np.amax(w[k:k+24,:,:,:]))[0][0] + k)
#     maxheight.append(np.where(w[k:k+24,:,:,:] == np.amax(w[k:k+24,:,:,:]))[1][0])
#     maxintensity.append(np.amax(w[k:k+24,:,:,:]))

# time2plot=[]
# zplot =[]    
# for k in range(0,len(maxtime)):
#     time2plot.append(time2[maxtime[k]])
#     zplot.append(z[maxheight[k]])
    

# fig,ax1=plt.subplots()
# plt.xticks(maxtime, time2plot, rotation='vertical')
# plt.gcf().autofmt_xdate()
# plt.plot(maxtime,zplot,marker='*')
# ax1.set_ylim([0,3])
# plt.xlabel('Peak w time',name='Arial',weight='bold',size=16,style='italic')
# plt.ylabel('Peak height',name='Arial',weight='bold',size=16,style='italic')

# ax2=ax1.twinx()
# plt.plot(maxtime,maxintensity,marker='o',markersize='5')
# plt.ylabel('Max w',name='Arial',weight='bold',size=16,style='italic')




#This is a continuous plot of w and max height
# maxheight2 = []
# maxtime2 =[]
# maxintensity2 = []
# for k in range(0,len(w)):
#     maxtime2.append(k)
#     maxheight2.append(np.where(w[k,0:75,:,:] == np.amax(w[k,0:75,:,:]))[0][0])
#     maxintensity2.append(np.amax(w[k,:,:,:]))

# time2plot2=[]
# zplot2 =[]    
# for k in range(0,len(maxtime2)):
#     time2plot2.append(time2[maxtime2[k]])
#     zplot2.append(z[maxheight2[k]])
    

# fig,ax1=plt.subplots()
# plt.xticks(maxtime2[0:len(maxtime2):24], time2plot2[0:len(time2plot2):24], rotation='vertical')
# plt.gcf().autofmt_xdate()
# plt.plot(maxtime2,zplot2)
# #ax1.set_ylim([0,3])
# plt.xlabel('Peak w time',name='Arial',weight='bold',size=16,style='italic')
# plt.ylabel('Peak height',name='Arial',weight='bold',size=16,style='italic')

#%%
# This is the scatterplot of w with height and intensity
maxheight2 = []
maxtime2 =[]
maxintensity2 = []
timesteps = 101
maxheight = 166
for k in range(0,timesteps):
    maxtime2.append(k)
    maxheight2.append(np.where(w[k,0:maxheight,:,:] == np.amax(w[k,0:maxheight,:,:]))[0][0])
    maxintensity2.append(np.amax(w[k,:,:,:]))

time2plot2=[]
zplot2 =[]    
for k in range(0,len(maxtime2)):
    time2plot2.append(time2[maxtime2[k]])
    zplot2.append(z[maxheight2[k]]) 
    

maxintensity2.insert(0,0.05)
zplot2.insert(0,0.020000001)
maxtime2.insert(0,0)


fig,ax1=plt.subplots()
plt.rcParams.update({"font.size": 16})
plt.xticks(maxtime2[1:len(maxtime2):4], time2plot2[0:len(time2plot2):4], rotation='vertical')
plt.gcf().autofmt_xdate()
plt.plot(maxtime2,zplot2,zorder=1)
plt.scatter(maxtime2,zplot2,c=maxintensity2,s=60,cmap='Spectral_r',zorder=2)
cbar=plt.colorbar()
cbar.ax.tick_params(labelsize=20)
cbar.set_label(u'Peak w intensity ($ms^{-1}$)',size=20,style='italic')
#ax1.set_ylim([0,3])
#plt.xlabel('hi',name='Arial',weight='bold',size=20,style='italic')
plt.ylabel('Peak height (km)',name='Arial',size=20,style='italic')
ax1.set_xlim([0,timesteps-1])
ax1.set_ylim([0,4])
plt.grid(True)
    
#%%    

###############################################################################################

#Calculating and plotting the total kinetic energy of the system 
wndspeed = np.sqrt((v[:,:,0:3,:])**2   +  (u[:,:,0:3,:-1])**2)

zweight = np.ones_like(wndspeed)
for k in range(1,len(z)):
    zweight[:,k,:,:] = abs(z[k] - z[k-1]) * 1000
zweight[:,0,:,:] = z[0] * 1000

kenergy = np.ones_like(wndspeed)

kenergy = wndspeed**2 * rho * zweight/2

meankenergy = []
for k in kenergy:
    meankenergy.append(np.mean(k))

plt.figure()
plt.plot(time,meankenergy)


###############################################################################################

#%%
#Calculating the maximum vertical parcel displacements for every 24 hour period
reference = -99999999
for k in range (0,len(zparcel[0])):
    for t in range(0,len(time)-21+2-4-2):
        counter = 0
        while counter < 19:
            if abs(zparcel[t][k]-zparcel[t+1+counter][k]) > reference:
                max_displacement = abs(zparcel[t][k]-zparcel[t+1+counter][k])
                initial_time_index = t
                final_time_index = t+1+counter
                parcel_index = k       
                initial_x_position = xparcel[t][k]
                final_x_position = xparcel[t+1+counter][k]
                initial_z_position = zparcel[t][k]
                final_z_position = zparcel[t+1+counter][k]
                reference = abs(zparcel[t][k]-zparcel[t+1+counter][k])
                
            counter = counter + 1
    print (k)
        
print ("max_displacement = ", max_displacement) 
print ("initial_time = ", time2[initial_time_index])       
print ("final_time = ", time2[final_time_index])
print ("initial_x_position = ", initial_x_position)
print ("final_x_position = ", final_x_position)
print ("initial_z_position = ", initial_z_position)
print ("final_z_position = ", final_z_position)
        


    
#%%
#Plot of tke and 'pbl' tendency before and after sunset

fig=plt.figure(figsize=(20,20))
plt.rcParams.update({"font.size": 16})

twopm = 38
b4sunset = 43

ax=fig.add_subplot(2,2,1)
plt.plot(tke[twopm,:-1,0,0],z, linewidth=3,color='b')
#plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
plt.xlabel('Subgrid TKE ($m^{-2}s^{-2}$)',name='Arial',size=16,style='italic')
plt.ylabel('Height (km)',name='Arial',size=19,style='italic')
ax.set_xlim([0.0,270])
ax.set_ylim([0,4])
plt.grid(True)


ax=fig.add_subplot(2,2,2)
plt.plot(tke[b4sunset,:-1,0,0],z, linewidth=3,color='b')
#plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
plt.xlabel('Subgrid TKE ($m^{-2}s^{-2}$)',name='Arial',size=16,style='italic')
plt.ylabel('Height (km)',name='Arial',size=19,style='italic')
ax.set_xlim([0.0,270])
ax.set_ylim([0,4])
plt.grid(True)


ax=fig.add_subplot(2,2,3)
plt.plot(upblten[twopm,:,0,0],z, linewidth=3,color='b')
plt.xlabel('PBL tendency ($ms^{-2}$)',name='Arial',size=16,style='italic')
plt.ylabel('Height (km)',name='Arial',size=19,style='italic')
ax.set_xlim([-0.0006,0.0006])
plt.xticks(np.arange(-0.0006,0.0007,0.0003))
ax.set_ylim([0,4])
plt.grid(True)


ax=fig.add_subplot(2,2,4)
plt.plot(upblten[b4sunset,:,0,0],z, linewidth=3,color='b')
plt.xlabel('PBL tendency ($ms^{-2}$)',name='Arial',size=16,style='italic')
plt.ylabel('Height (km)',name='Arial',size=19,style='italic')
ax.set_xlim([-0.0006,0.0006])
plt.xticks(np.arange(-0.0006,0.0007,0.0003))
ax.set_ylim([0,4])
plt.grid(True)




#%%
#Calculating the convergence/divergence (dudx only) 
dudx = np.ones_like(u)*np.nan


for k in range(1,len(xh)-1):
    dudx[:,:,:,k] = (u[:,:,:,k+1] - u[:,:,:,k-1]) / (xh[2]-xh[0])
    

#%%    
##################################################################################################
    
#Calculating the actual temperature
#T = np.ones_like(theta)*np.nan

# T = theta * (    100000.0 * ( P**(-1) )     )**(-2.0/7)

###############################################################################################

#Calculating the terms in the the dw/dt equation (navier stokes) for local change

#Calculating the local change term

dwdt=np.ones_like(w[:,:-1,:,:])*np.nan
for k in range(1,len(time)-1):
    dwdt[k,:,:,:] = ( w[k+1,:-1,:,:] - w[k-1,:-1,:,:] ) / abs(time[k-1]-time[k+1])


# #Getting the PGF in the w direction
# PGFw=np.ones_like(P)*np.nan
# for k in range(1,len(z)-1):
#     PGFw[:,k,:,:] = (rho[:,k,:,:])**(-1) * ( P[:,k+1,:,:] - P[:,k-1,:,:] ) / abs( (z[k-1]-z[k+1])*1000.0 )
    
# #Getting the PGFpert in the w direction
# PGFpertw=np.ones_like(Ppert)*np.nan
# for k in range(1,len(z)-1):
#     PGFpertw[:,k,:,:] = - (rho[:,k,:,:])**(-1) * ( Ppert[:,k+1,:,:] - Ppert[:,k-1,:,:] ) / abs( (z[k-1]-z[k+1])*1000.0 )
    
    
# #Getting the nondimensional PGFpert in the w direction
# PGFPipertw=np.ones_like(Pipert)*np.nan
# for k in range(1,len(z)-1):
#     PGFPipertw[:,k,:,:] = - (rho[:,k,:,:])**(-1) * ( Pipert[:,k+1,:,:] - Pipert[:,k-1,:,:] ) / abs( (z[k-1]-z[k+1])*1000.0 )
    

# #Getting the buoyancy term 
# Bw = Bw

# #Getting the first advection term 
# dwdz=np.ones_like(w[:,:-1,:,:])*np.nan
# for k in range(1,len(z)-1):
#     dwdz[:,k,:,:] = ( w[:,k+1,:,:] - w[:,k-1,:,:] ) / abs( (z[k-1]-z[k+1])*1000.0 )
    
# advwz = w[:,:-1,:,:] * dwdz

# #Getting the second advection term
# dwdx=np.ones_like(w[:,:-1,:,:])*np.nan
# for k in range(1,len(xh)-1):
#     dwdx[:,:,:,k] = ( w[:,:-1,:,k+1] - w[:,:-1,:,k-1] ) / abs( (xh[2]-xh[0])*1000.0 )
    
# advwx = u[:,:,:,:-1] * dwdx


# advtotal = advwx + advwz


###############################################################################################



#Calculating the terms in the the du/dt equation (navier stokes) for local change

dudt=np.ones_like(u[:,:,:,:-1])*np.nan
for k in range(1,len(time)-1):
    dudt[k,:,:,:] = ( u[k+1,:,:,:-1] - u[k-1,:,:,:-1] ) / abs(time[k-1]-time[k+1])




###############################################################################################


# #Calculating the du/dt by looking at the u equation terms outputted by cm1
# initPGF = np.ones_like(u[:,:,:,:]) * 0.0 + (0.000084 * 10.0)

# #dudtcm1 = urdamp + hadvu  + uhturb + uvturb + uidiff  + fcoru - initPGF

# dudtcm1 = urdamp + hadvu + vadvu + uhturb + uvturb + upblten + uidiff + fcoru + (PGFpertuPi - initPGF)

# ucm1=np.ones_like(u[:,:,:,:])*np.nan

# for k in range(0,len(time)-1):
#     ucm1[k+1,:,:,:] = u[k,:,:,:] + abs(time[0]-time[1])*dudtcm1[k,:,:,:] 
    

#Calculating the du/dt by looking at the u equation terms outputted by cm1 (in another way)
initPGF = np.ones_like(u[:,:,:,:]) * 0.0 + (0.000084 * 10.0)

# cor1 = v[:,:,:,:] * 0.000084 

# dudtcm1 =    - initPGF[:,:,:,:-1] + cor1[:,:,:-1,:]

# dudtcm1 = urdamp + hadvu + vadvu + uhturb + uvturb + uidiff + fcoru + (PGFpertuPi - initPGF)

# ucm1=np.ones_like(u[:,:,:,:])*np.nan

# for k in range(0,len(time)-1):
#     ucm1[k+1,:,:,:-1] = u[k,:,:,:-1] + abs(time[0]-time[1])*dudtcm1[k,:,:,:]

#Calculating the dw/dt by looking at the w equation terms outputted by cm1

# dwdtcm1 = PGFpertwPi + Bw + hadvw + vadvw + whturb + wvturb + wrdamp + hidiffw + vidiffw

# wcm1=np.ones_like(w[:,:,:,:])*np.nan

# for k in range(0,len(time)-1):
#     wcm1[k+1,:,:,:] = w[k,:,:,:] + abs(time[0]-time[1])*dwdtcm1[k,:,:,:] 








#%%    
#Function to help in the colorbar plotting
def custom_div_cmap(numcolors=26, name='custom_div_cmap',
                    mincol='blue', midcol='white', maxcol='red'):
    """ Create a custom diverging colormap with three colors
    
    Default is blue to white to red with 11 colors.  Colors can be specified
    in any way understandable by matplotlib.colors.ColorConverter.to_rgb()
    """

    from matplotlib.colors import LinearSegmentedColormap

    cmap = LinearSegmentedColormap.from_list(name=name,
                                             colors =[mincol, midcol, maxcol],
                                             N=numcolors)
    return cmap

bwr_custom = custom_div_cmap(20)

bwr_custom_thpert = custom_div_cmap(30)    

#Function to help in the colorbar plotting v2
def custom_div_cmap2(numcolors=26, name='custom_div_cmap2',
                    mincol='white', midcol='gray', maxcol='black'):
    """ Create a custom diverging colormap with three colors
    
    Default is blue to white to red with 11 colors.  Colors can be specified
    in any way understandable by matplotlib.colors.ColorConverter.to_rgb()
    """

    from matplotlib.colors import LinearSegmentedColormap

    cmap = LinearSegmentedColormap.from_list(name=name,
                                              colors =[mincol, midcol, maxcol],
                                              N=numcolors)
    return cmap

bwr_custom2 = custom_div_cmap2(20)

bwr_custom_thpert2 = custom_div_cmap2(30)
    
    
    
    

#Animation of U or V winds, potential temperature and pressure (xz section)
xm,zm=np.meshgrid(xh,z)

for k in range(0,len(time)-0,1):

    
    fig=plt.figure(figsize=(10,10))
    plt.rcParams.update({"font.size": 16})
    #fig.suptitle(time2[k],name='Arial',size=20)
    #plt.rcParams.update({"font.size": 16})
    #xposition = 0
    xposition = 328
    xposition2 = 310


    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,u[k,:,0,:-1],np.arange(-10,10.1,0.1),cmap='seismic')
    # plt.colorbar(label='Wind Speed (m/s)')
    # #plt.title(time2[k],name='Arial',weight='bold',size=20)
    # #plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-2968,2968])
    # ax.set_ylim([0,7])
    
#    plt.subplot(2,1,1)
#    plt.contourf(xm,zm,v[k,:,0,:],np.arange(-5,5.1,0.1),cmap='CMRmap')
#    plt.colorbar(label='Wind Speed (m/s)')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')

    # ax=fig.add_subplot(2,1,1)
    # wndspeed = np.sqrt(np.array(v[:,:,0:2,:])**2   +  np.array(u[:,:,0:2,:-1])**2)
    # plt.contourf(xm,zm,wndspeed[k,:,0,:],np.arange(0,20.1,0.1),cmap='CMRmap')
    # #plt.pcolormesh(xm,zm,wndspeed[k,:,0,:],cmap='CMRmap',vmin=0, vmax=8)
    # plt.colorbar(label='Wind Speed (m/s)')
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.title(time2[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_xlim([-2968,2968])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,dudx[k,:,0,:-1],np.arange(-0.2,0.205,0.005),cmap='seismic')
    # #plt.pcolormesh(xm,zm,dudx[k,:,0,:-1],cmap='seismic',vmin=-0.3, vmax=0.3)
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,dudx[k,:,0,:-1],np.arange(-0.2,0.205,0.005),cmap='seismic')
    # plt.colorbar(label='Divergence ($s^{-1}$)')
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # #plt.title(time2[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    # #ax.set_xlim([-2968,2968])
    # ax.set_xlim([-2000,2000])
    # ax.set_ylim([0,7])

    # ax=fig.add_subplot(2,1,1)
    # #plt.contourf(xm,zm,thpert[k,:,0,:],np.arange(-10,10.5,0.5),cmap='seismic')
    # #plt.pcolormesh(xm,zm,thpert[k,:,0,:],cmap='seismic',vmin=-15, vmax=15)
    # plt.pcolormesh(xm,zm,thpert[k,:,0,:],cmap=bwr_custom_thpert,vmin=-15, vmax=15)
    # #plt.pcolormesh(xm,zh[0,:,0,:]/1000.0,thpert[k,:,0,:],cmap=bwr_custom_thpert,vmin=-15, vmax=15)
    # plt.colorbar(label='Potential Temperature Perturbation (K)')
    # #plt.title(time2[k],name='Arial',weight='bold',size=20)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])),name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_xlim([-2968,2968])
    # ax.set_xlim([-2000,2000])
    # ax.set_ylim([0,7])
    
    
    ax=fig.add_subplot(2,1,1)
    #plt.contourf(xm,zm,theta[k,:,0,:],np.arange(290,330,1),cmap='Reds')
    #plt.pcolormesh(xm,zm,theta[k,:,0,:],vmin=290, vmax=350,cmap=bwr_custom_thpert2)
#    plt.contourf(xm,zm,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    plt.contourf(xm,zh[0,:,0,:]/1000.0,theta[k,:,0,:],np.arange(290,330,1),cmap='Reds')
    plt.colorbar(label='Potential temperature (K)')
    #plt.title(time1[k],name='Arial',weight='bold',size=20)
    plt.xlabel('X Domain (km)',name='Arial',size=16,style='italic')
    plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    #ax.set_ylim([0,14])
    ax.set_xlim([-2000,2000])
    ax.set_ylim([0,4])
    

  
    ax=fig.add_subplot(2,1,2)
    #plt.contourf(xm,zm,B[k,:,0,:],np.arange(-0.5,0.52,0.02),cmap='seismic')
    plt.contourf(xm,zh[0,:,0,:]/1000.0,B[k,:,0,:],np.arange(-0.5,0.52,0.02),cmap='seismic')
    #plt.pcolormesh(xm,zm,B[k,:,0,:],cmap=bwr_custom_thpert,vmin=-0.4, vmax=0.4)
    #plt.pcolormesh(xm,zh[0,:,0,:]/1000.0,B[k,:,0,:],cmap=bwr_custom_thpert,vmin=-0.4, vmax=0.4)
    plt.colorbar(label='Buoyancy ($ms^{-2}$)')
    #plt.title(time1[k],name='Arial',weight='bold',size=20)
    plt.xlabel('X Domain (km)',name='Arial',size=16,style='italic')
    plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    ax.set_xlim([-2000,2000])
    ax.set_ylim([0,4])

#    plt.subplot(2,1,2)
#    plt.contourf(xm,zh[0,:,0,:],P[k,:,0,:]-P[0,:,0,:],np.arange(-350,350,10),cmap='seismic')
#    plt.colorbar(label='Presure Perturbaion (Pa)')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')

#    plt.subplot(2,1,2)
#    plt.contourf(xm,zm,cloud[k,:,0,:],cmap='seismic')
#    plt.colorbar(label='Cloud Fraction (Pa)')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')

    # ax=fig.add_subplot(1,1,1)
    # #plt.contourf(xm,zm,w[k,:-1,0,:],np.arange(-0.1,0.11,0.01),cmap='seismic')
    # plt.pcolormesh(xm,zm,w[k,:-1,0,:],cmap='seismic',vmin=-0.05, vmax=0.05)
    # #plt.pcolormesh(xm,zh[0,:,0,:]/1000.0,w[k,:-1,0,:],cmap='seismic',vmin=-0.1, vmax=0.1)
    # plt.colorbar(label='Vertical velocity ($ms^{-1}$)')
    # #plt.title(time2[k],name='Arial',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    # #ax.set_xlim([-2968,2968])
    # ax.set_xlim([-2000,2000])
    # ax.set_ylim([0,7])

#    plt.subplot(2,1,2)
#    plt.contourf(xm,zm,qv[k,:,0,:],np.arange(0,0.0075,0.0005),cmap='CMRmap')
#    plt.colorbar(label='Water vathpor mixing ratio')
#    plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')

    # ax=fig.add_subplot(2,2,1)
    # plt.contourf(xm,zm,tke[k,:-1,0,:],np.arange(0,10.5,0.2),cmap='CMRmap')
    # plt.colorbar(label='Subgrid TKE')
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    
    
#     ax=fig.add_subplot(2,1,1)
#     plt.contourf(xm,zm,PGFx[k,:,0,:],cmap='seismic')
#     plt.colorbar(label='Pressure gradient')
#     plt.title(time1[k],name='Arial',weight='bold',size=20)
#     plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic') 
#     plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
# #    ax.set_xlim([-2968,2968])
    
    
    # ax=fig.add_subplot(2,2,2)
    # plt.plot(u[k,:,0,xposition],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # # plt.title(time2[k],name='Arial',size=20)
    # plt.xlabel('U wind ($ms^{-1}$)',name='Arial',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    # ax.set_xlim([-10,20])
    # ax.set_ylim([0,4])
    # plt.grid(True)
    
    
    # ax=fig.add_subplot(2,2,1)
    # plt.plot(u[k,:,0,xposition2],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('U wind ($ms^{-1}$)',name='Arial',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    # ax.set_xlim([-10,20])
    # ax.set_ylim([0,4])
    # plt.grid(True)
    
    # ax=fig.add_subplot(2,2,2)
    # plt.plot(v[k,:,0,xposition],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('V wind ($ms^{-1}$)',name='Arial',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    # ax.set_xlim([-10,20])
    # ax.set_ylim([0,4])
    # plt.grid(True)
    
    # ax=fig.add_subplot(3,1,3)
    # wndspeed = np.sqrt(np.array(v[:,:,0:2,:])**2   +  np.array(u[:,:,0:2,:-1])**2)
    # plt.plot(wndspeed[k,:,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('Wind Speed (m/s)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([0,20])
    # ax.set_ylim([0,3])
    
    
    # ax=fig.add_subplot(2,1,2)
    # plt.plot(ucm1[k,:,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('U wind cm1 (m/s)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-10,20])
    # ax.set_ylim([0,14])
    
    # ax=fig.add_subplot(2,1,2)
    # plt.plot(upblten[k,:,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('PBL tendency ($s^{-2}$)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-0.0015,0.0015])
    # ax.set_ylim([0,5])
    
    # ax=fig.add_subplot(2,2,4)
    # plt.plot(upblten[k,:,0,xposition],z,label='PBL tendency')
    # plt.plot(fcoru[k,:,0,xposition] - initPGF[k,:,0,xposition],z,label='Coriolis minus base PGF')
    # plt.plot(PGFpertuPi[k,:,0,xposition],z,label='Perturbation PGF')
    # plt.plot(urdamp[k,:,0,xposition],z,label='Rayleigh Damping')
    # plt.plot(hadvu[k,:,0,xposition],z,label='Horizontal advection')
    # plt.plot(vadvu[k,:,0,xposition],z,label='Vertical advection')
    # plt.plot(uidiff[k,:,0,xposition],z,label='Artificial Diffusion')
    # # plt.plot(uhturb[k,:,0,xposition],z,label='Horizontal Turbulence')
    # # plt.plot(uvturb[k,:,0,xposition],z,label='Vertical Turbulence')
    # plt.legend(fontsize=10)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('Terms in the U equation of motion ($ms^{-2}$)',name='Arial',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    # ax.set_xlim([-0.0015,0.0015])
    # ax.set_ylim([0,4])
    # plt.grid(True)
    
    # ax=fig.add_subplot(2,2,3)
    # plt.plot(upblten[k,:,0,xposition2],z,label='PBL tendency')
    # plt.plot(fcoru[k,:,0,xposition2] - initPGF[k,:,0,xposition],z,label='Coriolis minus base PGF')
    # plt.plot(PGFpertuPi[k,:,0,xposition2],z,label='Perturbation PGF')
    # plt.plot(urdamp[k,:,0,xposition],z,label='Rayleigh Damping')
    # plt.plot(hadvu[k,:,0,xposition2],z,label='Horizontal advection')
    # plt.plot(vadvu[k,:,0,xposition2],z,label='Vertical advection')
    # plt.plot(uidiff[k,:,0,xposition2],z,label='Artificial Diffusion')
    # # plt.plot(uhturb[k,:,0,xposition],z,label='Horizontal Turbulence')
    # # plt.plot(uvturb[k,:,0,xposition],z,label='Vertical Turbulence')
    # plt.legend(fontsize=10)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('Terms in the U equation of motion ($ms^{-2}$)',name='Arial',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    # ax.set_xlim([-0.0015,0.0015])
    # ax.set_ylim([0,4])
    # plt.grid(True)
    
    
    # ax=fig.add_subplot(2,2,4)
    # plt.plot(vpblten[k,:,0,xposition],z,label='PBL tendency')
    # plt.plot(fcorv[k,:,0,xposition],z,label='Coriolis minus base PGF')
    # plt.plot(PGFpertvPi[k,:,0,xposition],z,label='Perturbation PGF')
    # plt.plot(vrdamp[k,:,0,xposition],z,label='Rayleigh Damping')
    # plt.plot(hadvv[k,:,0,xposition],z,label='Horizontal advection')
    # plt.plot(vadvv[k,:,0,xposition],z,label='Vertical advection')
    # plt.plot(vidiff[k,:,0,xposition],z,label='Artificial Diffusion')
    # # plt.plot(uhturb[k,:,0,xposition],z,label='Horizontal Turbulence')
    # # plt.plot(uvturb[k,:,0,xposition],z,label='Vertical Turbulence')
    # plt.legend(fontsize=13)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('Terms in the V equation of motion ($ms^{-2}$)',name='Arial',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',size=16,style='italic')
    # ax.set_xlim([-0.0015,0.0015])
    # ax.set_ylim([0,4])
    # plt.grid(True)
    
    
    
    # ax=fig.add_subplot(2,1,1)
    # plt.plot(w[k,:-1,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('W wind',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-1.5,1.5])
    # ax.set_ylim([0,14])
    
    # ax=fig.add_subplot(2,1,2)
    # plt.plot(wcm1[k,:-1,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('W wind cm1 (m/s)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-1.5,1.5])
    # ax.set_ylim([0,14])

    
    
    # ax=fig.add_subplot(2,1,1)
    # plt.plot(v[k,:,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('V wind (m/s)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-10,20])
    # ax.set_ylim([0,2])

    # ax=fig.add_subplot(2,1,2)
    # plt.plot(vpblten[k,:,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('PBL tendency ($s^{-2}$)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-0.0008,0.0008])
    # ax.set_ylim([0,14])

    # ax=fig.add_subplot(2,1,2)
    # plt.plot(dudtcm1[k,:,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('dudtcm1 ($s^{-2}$)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-0.00052,0.0004])
    # ax.set_ylim([0,2])
    
    # ax=fig.add_subplot(2,1,2)
    # plt.plot(dudt[k,:,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('dudt ($s^{-2}$)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-0.00052,0.0004])
    # ax.set_ylim([0,2])


    
    # ax=fig.add_subplot(2,1,2)
    # plt.plot(tke[k,:-1,0,0],z)
    # #plt.title(time2[k] + '     ' +str(int(solrad[k,0,0])) ,name='Arial',weight='bold',size=20)
    # plt.xlabel('Subgrid TKE ($s^{-2}$)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([0.0,150])
    # ax.set_ylim([0,3])
    
    # ax=fig.add_subplot(2,1,2)
    # plt.plot(theta[k,:,0,0],z)
    # plt.title('Edges of domain' ,name='Arial',weight='bold',size=20)
    # plt.xlabel('Potential temperature (K)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([250,350])
    # ax.set_ylim([0,2])
    
   
    
    
    # ax=fig.add_subplot(2,2,1)
    # plt.plot(theta[k,:,0,0],z)
    # plt.title('Edges of domain' ,name='Arial',weight='bold',size=20)
    # plt.xlabel('Potential temperature (K)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([290,400])
    # ax.set_ylim([0,14])
#    
#    ax=fig.add_subplot(2,2,2)
#    plt.plot(theta[k,:,0,0],z)
#    plt.title('Center of domain' ,name='Arial',weight='bold',size=20)
#    plt.xlabel('Potential temperature (K)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    ax.set_xlim([290,400])
#    ax.set_ylim([0,14])
#    
#    ax=fig.add_subplot(2,2,3)
#    plt.plot(thetaV[k,:,0,0],z)
#    plt.title('Edges of domain' ,name='Arial',weight='bold',size=20)
#    plt.xlabel('Virtual Potential temperature (K)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    ax.set_xlim([290,400])
#    ax.set_ylim([0,14])
#    
#    ax=fig.add_subplot(2,2,4)
#    plt.plot(thetaV[k,:,0,0],z)
#    plt.title('Center of domain' ,name='Arial',weight='bold',size=20)
#    plt.xlabel('Virtual Potential temperature (K)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    ax.set_xlim([290,400])
#    ax.set_ylim([0,14])
    
    
    # ax=fig.add_subplot(2,1,2)
    # print (xparcel[k,1500]/1000.0,zparcel[k,1500]/1000.0)
    # plt.pcolormesh(xm,zm,w[k,:-1,0,:],cmap='seismic',vmin=-0.1, vmax=0.1)
    # plt.colorbar(label='Vertical velocity (m/s)')
    # xp=[]
    # zp=[]
    # for kp in range(0,6000,4):
    #     xp.append(xparcel[k,kp]/1000.0)
    #     zp.append(zparcel[k,kp]/1000.0)
    # plt.scatter(xp,zp)
    # #plt.title(time2[k],name='Arial',weight='bold',size=20)
    # #plt.scatter([xparcel[k,1497]/1000.0,xparcel[k,1500]/1000.0,xparcel[k,1503]/1000.0],[zparcel[k,1497]/1000.0,zparcel[k,1500]/1000.0,zparcel[k,1503]/1000.0])
    # #plt.scatter([xparcel[k,897]/1000.0,xparcel[k,900]/1000.0,xparcel[k,903]/1000.0],[zparcel[k,897]/1000.0,zparcel[k,900]/1000.0,zparcel[k,903]/1000.0])
    # #plt.scatter([xparcel[k,2097]/1000.0,xparcel[k,2100]/1000.0,xparcel[k,2103]/1000.0],[zparcel[k,2097]/1000.0,zparcel[k,2100]/1000.0,zparcel[k,2103]/1000.0])
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,6])

    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,dwdt[k,:,0,:],np.arange(-0.0000075,0.0000076,0.0000001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Calculated local change in W')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])  
    
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,(PGFpertwPi+Bw+hadvw+vadvw+whturb+wvturb+wrdamp)[k,:-1,0,:],np.arange(-0.0000075,0.0000076,0.0000001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Local change in W from output')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    
    
#    ax=fig.add_subplot(2,1,2)
#    plt.contourf(xm,zm,advtotal[k,:,0,:],np.arange(-0.0000075,0.0000076,0.0000001),cmap='seismic')
#    #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
#    plt.colorbar(label='Total advection of W')
#    #plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    #ax.set_ylim([0,14])
#    ax.set_xlim([-1000,1000])
#    ax.set_ylim([0,7])
    
    
#    ax=fig.add_subplot(2,1,1)
#    plt.contourf(xm,zm,advwx[k,:,0,:],np.arange(-0.0000075,0.0000076,0.0000001),cmap='seismic')
#    #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
#    plt.colorbar(label='Advection of W by U wind')
#    #plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    #ax.set_ylim([0,14])
#    ax.set_xlim([-1000,1000])
#    ax.set_ylim([0,7])
#    
#    
#    ax=fig.add_subplot(2,1,1)
#    plt.contourf(xm,zm,advwz[k,:,0,:],np.arange(-0.0000075,0.0000076,0.0000001),cmap='seismic')
#    #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
#    plt.colorbar(label='Advection of W by W wind')
#    #plt.title(time1[k],name='Arial',weight='bold',size=20)
#    plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
#    plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
#    #ax.set_ylim([0,14])
#    ax.set_xlim([-1000,1000])
#    ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,PGFw[k,:,0,:],np.arange(-9.91,-9.765,0.005),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Pressure gradient force in W')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,PGFpertw[k,:,0,:],np.arange(-0.55,0.60,0.05),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Perturbation pressure gradient force in W')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,PGFpertwPi[k,:-1,0,:],np.arange(-0.56,0.56,0.005),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Pi PFG perturbation')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,Bw[k,:-1,0,:],np.arange(-0.56,0.56,0.005),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Buoyancy')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,(PGFpertwPi + Bw)[k,:-1,0,:],np.arange(-0.0000035,0.0000036,0.0000001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Buoyancy plus PGFPipert')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,hadvw[k,:-1,0,:],np.arange(-0.0000035,0.0000036,0.0000001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Horizontal advection of w')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,vadvw[k,:-1,0,:],np.arange(-0.0000035,0.0000036,0.0000001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Vertical advection of w')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,hidiffw[k,:-1,0,:],np.arange(-0.000000015,0.000000016,0.000000001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='horizontal dissipiation')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,vidiffw[k,:-1,0,:],np.arange(-0.000000000082,0.000000000087,0.000000000005),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='vertical dissipiation')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,dudt[k,:,0,:],np.arange(-0.0013,0.0013,0.0001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Calculated local change in U')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7]) 

    
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,(-PGFpertuPi+hadvu+vadvu+fcoru+urdamp+upblten)[k,:,0,:-1],np.arange(-0.0013,0.0013,0.0001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Local change in U from output')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,PGFpertuPi[k,:,0,:-1],np.arange(-0.56,0.56,0.005),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Pi PFG perturbation for u eq')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,hadvu[k,:,0,:-1],np.arange(-0.00035,0.00036,0.00001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Horizontal advection of u')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-3000,3000])
    # ax.set_ylim([0,7])
    
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,vadvu[k,:,0,:-1],np.arange(-0.00035,0.00036,0.00001),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Vertical advection of u')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-3000,3000])
    # ax.set_ylim([0,7])
    
    # ax=fig.add_subplot(2,1,1)
    # plt.contourf(xm,zm,fcoru[k,:,0,:-1],np.arange(-0.00052,0.002,0.0001),cmap='CMRmap')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Coriolis force')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-3000,3000])
    # ax.set_ylim([0,7])
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,upblten[k,:,0,:-1],np.arange(-0.008,0.0085,0.0005),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='PBL tendency')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-1000,1000])
    # ax.set_ylim([0,7]) 
    
    
    # ax=fig.add_subplot(2,1,2)
    # plt.contourf(xm,zm,urdamp[k,:,0,:-1],np.arange(-0.0005,0.00055,0.00005),cmap='seismic')
    # #plt.contourf(xm,zh[0,:,0,:]/1000.0,T[k,:,0,:],np.arange(205,315,2),cmap='CMRmap')
    # plt.colorbar(label='Rayleigh damping')
    # #plt.title(time1[k],name='Arial',weight='bold',size=20)
    # plt.xlabel('X Domain (km)',name='Arial',weight='bold',size=16,style='italic')
    # plt.ylabel('Height (km)',name='Arial',weight='bold',size=16,style='italic')
    # #ax.set_ylim([0,14])
    # ax.set_xlim([-3000,3000])
    # ax.set_ylim([0,7])
    
    

    
    
    plt.subplots_adjust(bottom=0.07, top=0.93, hspace=0.2)
    plt.pause(0.5)
    nameoffigure = time2[k]
    string_in_string = "{}".format(nameoffigure)
    plt.savefig(string_in_string)
    plt.close()
    
    
    
#plt.show()
  
#%%   
 















 
