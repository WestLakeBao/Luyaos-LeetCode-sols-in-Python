class Vector2D(object):
    def __init__(self, vec2d):
        self.vec = vec2d
        self.indexList = 0
        self.indexElement = 0
        self._moveToValid()

    def _moveToValid(self):
        while self.indexList < len(self.vec) and self.indexElement >= len(
                self.vec[self.indexList]):  # reset when reaching the end of the sublist
            self.indexList += 1
            self.indexElement = 0

    def next(self):
        result = self.vec[self.indexList][self.indexElement]
        self.indexElement += 1
        self._moveToValid()
        return result

    def hasNext(self):
        return self.indexList < len(self.vec)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())