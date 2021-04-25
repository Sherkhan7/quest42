impressive_twts = prev_likes = 0

with open('tweet_likes.txt', 'r') as f:
    for likes in f:
        if likes[-1] == '\n':
            likes = likes[:-1]

        likes = int(likes)
        if likes > prev_likes:
            impressive_twts += 1

        prev_likes = likes

print(impressive_twts - 1)
