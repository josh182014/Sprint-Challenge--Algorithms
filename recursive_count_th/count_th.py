'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    if 'th' in word:
        return 1 + count_th(word.replace('th', '0', 1))
    else:
        return 0


if __name__ == "__main__":
    print(count_th('hellthoth'))
