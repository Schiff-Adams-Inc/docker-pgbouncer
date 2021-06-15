import sqlparse

def is_subscription(query):
    parsed = sqlparse.parse(query.strip())[0]
    first_token = parsed.token_first(skip_ws=True)
    if first_token.normalized != "SELECT":
        return False
    first_index = parsed.token_index(first_token)
    _index, token = parsed.token_next(first_index, skip_ws=True)
    return token.normalized.startswith("\"_subs\"")

def routing_rules(username, query):
    if 'hdb_catalog.event_log' in query:
        return 'MDB'
    if is_subscription(query):
        return 'RR'
    return 'MDB'
