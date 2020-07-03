def slices(series, length):
    if length <= 0 or length > len(series):
        raise ValueError('Invalid length')
    stop_index = len(series) - length + 1
    return [series[i:i+length] for i in range(stop_index)]
