# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def gethost(self,s):
        return s.split('/')[2]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        host= self.gethost(startUrl)
        q=collections.deque()

        q.append(startUrl)
        vis=set()
        vis.add(startUrl)

        while q:

            for _ in range(len(q)):
                pop = q.popleft()

                newUrls = htmlParser.getUrls(pop)

                for url in newUrls:
                    if host in url and url not in vis:
                        q.append(url)
                        vis.add(url)

        return vis



