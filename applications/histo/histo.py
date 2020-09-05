# Your code here
def histogram(file):
    ignored = '";:,.-+=/|\[]{}()*^&'
    cache = {}

    with open(file) as file:
        text = file.read().strip().split()
    
    for word in text:
        new_word = word.strip(ignored).lower()
        
        if new_word not in cache:
            cache[new_word] = 1
        else:
            cache[new_word] += 1

    sort_by_count = sorted(cache.items(), key = lambda item: item[1], reverse = True)
    largest_num = len(sorted(cache.keys(), key = lambda x: len(x))[-1])

    for i, k in sort_by_count:
        hist = " " * (largest_num - len(i)) + k * "#"

        print(f"{i} {hist}")

h = histogram("robin.txt")
print(h)
