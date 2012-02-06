import pyes
import simplejson as json

# stop elasticsearch if running
# move its database somewhere temporary
# start it up

# for each test:
  # set index parameters
  # index all documents in payload/
  # query a gajillion ways
    # save results
  # delete db

# compare results with expectations

# restore the original db (if moved)

# needed:
  # a way to specify index variance
  # a way to specify query variance
