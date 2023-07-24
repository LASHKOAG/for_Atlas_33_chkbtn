class delftstack(object):
    def __init__(self, a):
        self.ans = 'a'
        
    @classmethod
    def first(cls):
        return "first"

    @classmethod
    def second(cls):
        return "second"

s1 = delftstack.first()

print(s1)

s2 = delftstack.second()

print(s2)