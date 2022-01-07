from threading import Condition

class Foo:
    def __init__(self):
        self.condition = Condition()
        self.flag = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        with self.condition:
            self.condition.wait_for(lambda: self.flag == 0) # if condition is true then do not wait
            printFirst()
            self.flag = 1
            self.condition.notify_all()



    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.condition:
            self.condition.wait_for(lambda: self.flag == 1)
            printSecond()
            self.flag = 2
            self.condition.notify_all()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.condition:
            self.condition.wait_for(lambda: self.flag == 2)
            printThird()
            self.flag = 3