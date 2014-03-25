import os
import urllib2, sys,urllib,os

os.environ["http_proxy"]='http://lester:xxxx@server:port'
os.environ["https_proxy"]='http://lester:xxxx@server:port' 

def funcionprogreso(bloque, tamano_bloque, tamano_total):
    cant_descargada = bloque * tamano_bloque
    sys.stdout.write('\rCantidad descargada: %s bytes / %s bytes totales' % (cant_descargada, tamano_total))


from datetime import date
d = str(date.today())
year=d.split('-')[0]
month=d.split('-')[1] 
day=d.split('-')[2]
forecast_time='00' #What time the forecast is (00, 06, 12, 18)
forecast_hour='00' 
forecast_hours=['00','03','06','09','12','15','18','21','24','27','30','33','36','39','42','45','48','51'] #How many hours ahead to forecast (2 or 3 digits)
#forecast_hours=['00']
if not os.path.isdir(year+month+day+forecast_time): os.mkdir(year+month+day+forecast_time)
if os.path.isdir(year+month+day+forecast_time): os.chdir(year+month+day+forecast_time)

for x in forecast_hours:
    forecast_hour=x
    #&leftlon=0&rightlon=360&toplat=90&bottomlat=-90
    top_lat=90 #Top of bounding box (North)
    bottom_lat=-90 #Bottom of bounding box (South)
    left_lon=0 #Left of bounding box (West)
    right_lon=360 #Right of bounding box (East)

    #http://nomads.ncep.noaa.gov/cgi-bin/filter_nam_crb.pl?file=nam.t00z.afwaca00.grb2.tm00&lev_10_m_above_ground=on&lev_250_mb=on&lev_2_m_above_ground=on&lev_500_mb=on&var_PRES=on&var_TMP=on&var_UGRD=on&var_VGRD=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=/nam.20140305
    #griburl='http://nomads.ncep.noaa.gov/cgi-bin/filter_nam_crb.pl?'
    griburl='http://nomads.ncep.noaa.gov/cgi-bin/filter_gfs.pl?'
	
    #griburl=griburl+'file=nam.t'+str(forecast_time)+'z.afwaca'+str(forecast_hour)+'.grb2'+'tm00'
    griburl=griburl+'file=gfs.t'+str(forecast_time)+'z.pgrbf'+str(forecast_hour)+'.grib2'

    #Select atmospheric levels
    #griburl=griburl+'&lev_10_mb=on'    #10 mb level
    #griburl=griburl+'&lev_70_mb=on'    #70 mb level
    griburl=griburl+'&lev_250_mb=on'   #250 mb level
    griburl=griburl+'&lev_500_mb=on'
    griburl=griburl+'&lev_mean_sea_level=on'
    #griburl=griburl+'&lev_700_mb=on'   #700 mb level
    #griburl=griburl+'&lev_850_mb=on'   #850 mb level
    #griburl=griburl+'&lev_1000_mb=on'  #1000 mb level
    griburl=griburl+'&lev_2_m_above_ground=on'
    griburl=griburl+'&lev_10_m_above_ground=on'    
    #griburl=griburl+'&lev_entire_atmosphere_\(considered_as_a_single_layer\)=on'
    #griburl=griburl+'&lev_975_mb=on'   #975 mb level
    #griburl=griburl+'&lev_950_mb=on'   #950 mb level
    #griburl=griburl+'&lev_925_mb=on'   #925 mb level
    #griburl=griburl+'&lev_900_mb=on'   #900 mb level
    
    #griburl=griburl+'&lev_800_mb=on'   #800 mb level
    #griburl=griburl+'&lev_750_mb=on'   #750 mb level
   
    #griburl=griburl+'&lev_650_mb=on'   #650 mb level
    #griburl=griburl+'&lev_600_mb=on'   #600 mb level
    #griburl=griburl+'&lev_550_mb=on'   #550 mb level
    #griburl=griburl+'&lev_500_mb=on'   #500 mb level
    #griburl=griburl+'&lev_450_mb=on'   #450 mb level
    #griburl=griburl+'&lev_400_mb=on'   #400 mb level
    #griburl=griburl+'&lev_350_mb=on'   #350 mb level
    #griburl=griburl+'&lev_300_mb=on'   #300 mb level
    
    #griburl=griburl+'&lev_200_mb=on'   #200 mb level
    #griburl=griburl+'&lev_150_mb=on'   #150 mb level
    #griburl=griburl+'&lev_100_mb=on'   #100 mb level
    
    #griburl=griburl+'&lev_30_mb=on'    #30 mb level
    #griburl=griburl+'&lev_20_mb=on'    #20 mb level
    

    #Select variables
    #&var_CWAT=on
    #&var_PRMSL=on
    #&var_PWAT=on
    #&var_TMP=on
    #&var_UGRD=on
    #&var_VGRD=on
    #griburl=griburl+'&var_HGT=on'  #Height (geopotential m)
    #griburl=griburl+'&var_RH=on'  #Relative humidity (%)
    #griburl=griburl+'&var_TMP=on' #Temperature (K)
    #griburl=griburl+'&var_CWAT=on'
    griburl=griburl+'&var_PRMSL=on'#Presion
    #griburl=griburl+'&var_RH=on'#Hmedad Relativa
    #griburl=griburl+'&var_PWAT=on'
    griburl=griburl+'&var_TMP=on'  #Temperatura
    griburl=griburl+'&var_UGRD=on' #East-West component of wind (m/s)
    griburl=griburl+'&var_VGRD=on' #North-South component of wind (m/s)
    #griburl=griburl+'&var_VVEL=on' #Vertical Windspeed (Pa/s)


    #Select bounding box
    #&leftlon=0&rightlon=360&toplat=90&bottomlat=-90
    griburl=griburl+'&leftlon='+str(left_lon)
    griburl=griburl+'&rightlon='+str(right_lon)
    griburl=griburl+'&toplat='+str(top_lat)
    griburl=griburl+'&bottomlat='+str(bottom_lat)

    #griburl= griburl +'&dir=/nam.'+year+month+day
    griburl= griburl +'&dir=/gfs.'+year+month+day+forecast_time

    #gfs.t00z.pgrbf00.grib2
    filename = 'gfs.t'+forecast_time+'z.pgrbf'+forecast_hour+'.grib2'
    print griburl
    print filename
    archivo = urllib.urlretrieve(griburl, filename, reporthook=funcionprogreso) 
