# Suppose we have a class:

# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().


from threading import Barrier
class Foo:
    def __init__(self):
        self.barrier1 = Barrier(2)
        self.barrier2 = Barrier(2)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.barrier1.wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.barrier1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.barrier2.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.barrier2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()