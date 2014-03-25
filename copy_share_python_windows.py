#-*- coding: utf-8 -*-
import os
import shutil
import subprocess
networkPath = "\\server\share"
user="lester"
password="xxxxxx"

winCMD = 'NET USE ' + networkPath + ' /User:' + user + ' ' + password
subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True)

shutil.copy("file.png", "\\\\server\share")
