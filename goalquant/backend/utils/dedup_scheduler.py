def deduplicate(data):
    seen = set()
    unique = []
    for item in data:
        key = str(item)
        if key not in seen:
            seen.add(key)
            unique.append(item)
    return unique
