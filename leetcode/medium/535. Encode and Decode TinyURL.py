"""
Problem: https://leetcode.com/problems/encode-and-decode-tinyurl/
Topics: Array, Hash Table, String, Design, Hash Function
Difficulty: Medium
Youtube Explanation: https://youtu.be/TYhXtuD65f8
"""
import random
import string

class Codec:

    def __init__(self):
        self.urls = []
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl):
        self.urls.append(longUrl)
        url_position = len(self.urls) - 1
        return self.base + str(url_position)

    def decode(self, shortUrl):
        url_position = int(shortUrl.split("/")[-1])
        return self.urls[url_position]


class CodecSol2:

    def __init__(self):
        self.short_to_long = {}
        self.long_to_short = {}
        self.base = "http://tinyurl.com/"
        self.chars = string.ascii_letters + string.digits

    def encode(self, longUrl):
        short = self.base + "".join(random.choice(self.chars) for _ in range(6)) # or next(itertools.combinations(self.chars, 6)))
        if longUrl not in self.long_to_short:
            self.long_to_short[longUrl] = short
            self.short_to_long[short] = longUrl
        return self.long_to_short[longUrl]

    def decode(self, shortUrl):
        return self.short_to_long[shortUrl]

