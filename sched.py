from subprocess import call
import sys
from os import listdir
from os.path import isfile, join


# Schedule multiple SfM tests

# Version numbers for each version to run
#vers_to_run = [44,45,46,47,48,49,50,51,52]
#vers_to_run = [53,54,55,56,57,58,59,60,61]
vers_to_run = [62,63,64,65,66,67,68,69,70]
#vers_to_run = [71,38,39,40,41,42,43]


for index in range(0,len(vers_to_run)):

  # Remove previous run if it existed
  call('rm -rf /datasets/strecha-mvs/v'+str(vers_to_run[index])+'/out'
    , shell=True)

  # Perform SfM
  call('python EvaluationLauncher.py'
    +' /opt/openMVG_Build/Linux-x86_64-RELEASE/'
    +' /datasets/strecha-mvs/v'+str(vers_to_run[index])
    +' /datasets/strecha-mvs/v'+str(vers_to_run[index])+'/out/'
    +' > log_'+str(vers_to_run[index])+'.txt', shell=True)
