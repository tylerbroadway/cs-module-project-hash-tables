def word_count(s):
    # Your code here
    cache = dict()
    ignored = '"":;.,-+=/\|[]{}()*^&'

    words = s.lower().replace("\r", " ").replace(
        "\t", " ").replace("\n", " ").split(" ")

    for word in words:
        new_word = word.strip(ignored)

        if new_word not in cache and new_word != "":
            cache[new_word] = 1
        elif new_word != "":
            cache[new_word] +=1

    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
