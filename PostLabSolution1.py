from collections import Counter

def mean(data):
    if not data:
        raise ValueError("mean requires at least one data point")
    return sum(data) / len(data)

def median(data):
    n = len(data)
    if n == 0: 
        raise ValueError("median requires at least one data point")
    s = sorted(data)
    mid = n // 2
    if n % 2 == 1:  
        return s[mid]
    else:
        return (s[mid - 1] + s[mid]) / 2

def mode(data):
    if not data:
        raise ValueError("mode requires at least one data point")
    counts = Counter(data)
    max_count = max(counts.values())
    tied = [val for val, cnt in counts.items() if cnt == max_count]
    return min(tied)
