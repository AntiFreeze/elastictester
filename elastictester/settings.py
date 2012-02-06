
# ELASTICSEARCH_BASE and ELASTICSEARCH_PORT
# must be defined in local_settings
# BASE is the root under which /bin, /data
# and /config live
try:
    from local_settings import *    
except ImportError:
    pass
