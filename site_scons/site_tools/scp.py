import SCons.Builder

scp = '/usr/bin/scp'

def generate(env):
  env['SCP']            = scp
  env['SCP_TARGET']     = 'remotehost:/home/user'
  
  ScpBuilder = SCons.Builder.Builder(action = SCons.Action.Action('$SCP $SOURCE $SCP_TARGET'))
  env['BUILDERS']['Scp'] = ScpBuilder
  
def exists(env):
  return env.Detect(scp);