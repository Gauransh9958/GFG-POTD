class Solution:

    def findPrimes(self, n):
        primes = [1] * (n + 1)
        primes[0] = 0
        primes[1] = 0
        i = 2
        while i * i <= n:
            if primes[i]:
                j = i * i
                while j <= n:
                    primes[j] = 0
                    j += i
            i += 1
        return primes

    def primeList(self, head):
        maxNum = 0
        temp = head
        while temp is not None:
            maxNum = max(maxNum, temp.val)
            temp = temp.next

        primes = self.findPrimes(2 * maxNum)

        temp = head
        while temp is not None:
            num = temp.val

            if num == 1:
                temp.val = 2
            else:
                num1, num2 = num, num
                while not primes[num1]:
                    num1 -= 1
                while not primes[num2]:
                    num2 += 1

                if num - num1 > num2 - num:
                    temp.val = num2
                else:
                    temp.val = num1

            temp = temp.next

        return head