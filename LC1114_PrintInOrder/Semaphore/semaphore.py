from threading import Semaphore

class Foo:
    def __init__(self):
        self.s1 = Semaphore(0)
        self.s2 = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s1.release()
        


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.s1.acquire()
        printSecond()
        self.s2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.s2.acquire()
        printThird()