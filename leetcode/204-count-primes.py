class Solution:
    def countPrimes(self, n: int) -> int:
        """
            TC: O(n^1.5)
            SC: O(1)
        """
        cnt_primes = 0
        for i in range(2, n):
            if self.isPrime(i):
                cnt_primes += 1
    
        return cnt_primes

    def isPrime(self, n: int) -> bool:
        if n == 2: 
            return True
        elif n <= 1 or n % 2 == 0:
            return False

        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

 
    def countPrimes(self, n: int) -> int:
        """
            Sieve of eratisthenes
            TC: O(nloglogn)
            SC: O(n)
        """
        if n < 3:
            return 0
        
        is_prime = [1] * n
        is_prime[0] = 0
        is_prime[1] = 0
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # only need to start with i * i, as i * (i - 1), i * (i - 2) ... etc are covered in previous iterations
                for j in range(i * i, n, i): 
                    is_prime[j] = 0
        
        return sum(is_prime)

