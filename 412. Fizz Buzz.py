# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.
import threading

class Solution(object):
    class FizzBuzz(threading.Thread):
        def __init__(self, printer, gap, bound, result):
            threading.Thread.__init__(self)
            self.printer = printer
            self.gap = gap
            self.bound = bound
            self.result = result
            self.current = gap-1

        def run(self):
            while self.current < self.bound:
                self.result[self.current] = self.printer(self.current+1)
                self.current += self.gap

    def fizzBuzz(self, n):
        result = [str(i) for i in range(1, n + 1)]
        threads = [Solution().FizzBuzz(lambda i: 'FizzBuzz' if i % 15 == 0 else 'Fizz', 3, n, result),
                   Solution().FizzBuzz(lambda i: 'FizzBuzz' if i % 15 == 0 else 'Buzz', 5, n, result)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return result