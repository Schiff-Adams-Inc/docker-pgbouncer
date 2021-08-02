def routing_rules(username, query):
    with open('/tmp/queries.txt', 'a') as fh:
        fh.write(query + '\n')
        fh.write("*" * 50 + '\n')

    if query.find('force_read_replica') != -1: # returns -1 if not in string
        return 'read_replica'
    return 'postgres'
