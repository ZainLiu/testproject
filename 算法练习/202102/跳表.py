import random


class SNode(object):
    def __init__(self,key=None,value=None):
        self.key=key
        self.maxIndex=-1
        self.link=[]
        self.value=value

class SkipList(object):
    def __init__(self,size=8,larger=65535):
        self.size=size
        self.tail=SNode()
        self.head=SNode()
        self.last=[]
        self.tail.key=larger
        self.head.key=-65535

        for i in range(self.size):
            self.head.link.append(self.tail)
        self.MAX_RAND=self.size

    def randomDispenseLevel(self):
        level=1
        while random.randint(0,1)==1:
            level+=1
        return level if level<=self.MAX_RAND else self.MAX_RAND

    def getLast(self,data):
        num=self.size-1
        p=self.head
        while num>=0:
            while p.link[num].key < data:
                p = p.link[num]
            num -=1

            self.last.append(p if p != None else self.head)

        return self.last[len(self.last)-1]
