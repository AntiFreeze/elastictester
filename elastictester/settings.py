TEST_QUERY = {
    'title'  : 'test',
    'body'   : 'test'
}

# ELASTICSEARCH_BASE and ELASTICSEARCH_URL
# must be defined in local_settings
#
# BASE is the root under which /bin, /data
# and /config live if you want the tester
# to touch this data
#
# URL is where to POST/GET data do

try:
    from local_settings import *    
except ImportError:
    pass
