
def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    return (nums[mid - 1] + nums[mid]) / 2

def mode(numbers):
    if not numbers:
        return 0
    counts = {}
    for x in numbers:
        counts[x] = counts.get(x, 0) + 1
    max_count = max(counts.values())
    for x in numbers:
        if counts[x] == max_count:
            return x

# Main Function (Test List)
def main():
    data = [10, 20, 20, 30, 40] 
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))

if __name__ == "__main__":
    main()