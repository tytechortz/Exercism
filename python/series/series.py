def slices(series, length):
    series_length = len(series)
    results = []
    if series_length < length:
        raise ValueError('slice length too large')
    elif length <= 0:
        raise ValueError("slice can't be 0 or negative")
    elif series == '':
        raise Exception("can't use empty series")
    else:
        n=0
        while n+length < series_length + 1:
            results.append(series[n:n+length])
            n += 1
    return results
