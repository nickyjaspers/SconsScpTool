SCons Secure Copy Tool
----------------------
The scons secure copy tool can be added to an environment in SCons.
What it can do for you is to copy a source to the scp target. 
For instance when you made a build of a binary and as the final step you want to deploy it to a remote system.
This tool can do that for you.


Installation
------------
To make use of the scp tool, the most easy way is to put the scp.py file into the directory site_scons/site_tools.
So the following directory structure will be made.

  +- ProjectDir
  |  +-SConstruct
  
  |  +-main.cpp
  
  |  +-site_scons
  
  |  | +-site_tools
  
  |  | | +-scp.py

You can also place in to global site_scons directory if that is preferred.
For more information, see http://www.scons.org/doc/production/HTML/scons-user/x3713.html


How to use
----------

### start SConstruct file
import os

### Create environment with default tools and the scp tool
env = Environment(tools=['default', 'scp'])
### Provide the scp target
env['SCP_TARGET'] = 'remotehost:/home/user'

### Define binary executable
binary = env.Program(target = 'MyTarget', source = [main.cpp])

### Only scp when deploy is true
### Dummy target while no target is necessary, only an action.
if (ARGUMENTS.get('deploy', 0) == 'true'):
  env_arm.Alias('deploy', env.Scp(target = ['dummy'], source=[binary]));

### end SConstruct file

Now browse to the projectdir and enter 'scons deploy=true'
The created binary will be copied to the scp target.

Probably you want to add additional options to scp, feel free to add, modify, enhance the scp tool.

Cheers!
