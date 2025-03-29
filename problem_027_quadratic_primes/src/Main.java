//https://projecteuler.net/problem=27
import java.util.ArrayList;

public class Main{
    public static void main(String[] args) {
        int highestNumOfPrimes = 0;
        int highestProduct = 0;
        int n;
        ArrayList<Integer> bValues = primesSmallerThanNum(1000);
        for (int b : bValues){
            for (int a = -999; a < 1000; a++) {
                n = 0;
                    while (isPrime((n * n) + (a * n) + b)){
                        n++;
                    }
                if (n> highestNumOfPrimes) {
                    highestNumOfPrimes = n;
                    highestProduct = a * b;
                }
            }
        }
        System.out.println(highestProduct);
    }
    private static boolean isPrime(int number){
        //Check if the number is prime.
        if (number > 0) {//If the number is negative, it cannot be prime.
            ArrayList<Integer> primeList = primesSmallerThanNum(number);
            for (int prime : primeList) {
                if (number != prime && number % prime == 0)
                    return false;
            }
            return true;
        }
        else {
            return false;
        }
    }

    private static ArrayList<Integer> primesSmallerThanNum(int num){
        ArrayList<Integer> primes = new ArrayList<>();
        if (num < 2) return primes;

        // Create boolean array where index represents number
        boolean[] isPrime = new boolean[num + 1];
        for (int i = 0; i <= num; i++) {
            isPrime[i] = true;
        }
        isPrime[0] = isPrime[1] = false;

        // Mark non-prime numbers
        for (int i = 2; i * i <= num; i++) {
            if (isPrime[i]) {
                // Mark multiples of i starting from i^2
                for (int j = i * i; j <= num; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        // Collect remaining primes
        for (int i = 2; i <= num; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }

        return primes;

    }

}