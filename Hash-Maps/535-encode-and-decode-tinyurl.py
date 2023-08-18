class Codec:
    def __init__(self):
        self.url_map={}
        self.code = 0 
        self.base_url = "http://tinyurl.com/"


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short_url = self.base_url + str(self.code)
        self.url_map[short_url] = longUrl
        self.code += 1
        return short_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_map.get(shortUrl, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))