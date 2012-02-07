import settings
import eshelper

# needed:
  # a way to specify index variance
  # a way to specify query variance

if __name__ == '__main__':
    es = eshelper.elasticsearch(settings.ELASTICSEARCH_URL, settings.ELASTICSEARCH_BASE)

    # stop elasticsearch if running
    # move its database somewhere temporary
    # start it up
    if es.is_running():
        es.stop()

    es.save_data()
    es.start()

    rs = eshelper.resultSet()
    expected = None
    query_text = 'test'

    # set up a base query to test against each index
    # of course, we need to use the same query for each index
    # or else we won't be able to compare results meaningfully
    query = eshelper.query(query_text)

    # one test per set of index parameters
    for my_index in eshelper.possibleIndices():
        # ingest all documents using new index
        eshelper.insertPayload(es, my_index)

        # test and record each possible query against the index
        for my_query in eshelper.possibleQueries(query):
            result = es.query(my_query)
            rs.addResult(my_index, my_query, result)

        # clean up the mess we made
        es.clear_index(my_index)

    # compare results with expectations
    eshelper.compareResultSet(expected, rs)

    # restore the original db (if moved)
    es.restore_data()
