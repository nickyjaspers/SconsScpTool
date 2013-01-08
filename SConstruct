### -----start SConstruct file
import os

### Create environment with default tools and the scp tool
env = Environment(tools=['default', 'scp'])
### Provide the scp target
env['SCP_TARGET'] = 'remotehost:/home/user'

### Define binary executable
binary = env.Program(target = 'MyTarget', source = ['main.cpp'])

### Only scp when deploy is true
### Dummy target while no target is necessary, only an action.
if (ARGUMENTS.get('deploy', 0) == 'true'):
  env.Alias('deploy', env.Scp(target = ['dummy'], source=[binary]));

### -----end SConstruct file