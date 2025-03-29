//https://projecteuler.net/problem=26
import java.util.HashMap;
//I've used the fact that the longest recurring mod set's length is the same as the longest recurrence in the decimal place.
public class Main {
    public static void main(String[] args) {
        int highestRecurrence = 0;
        int maxDenominator = 0;

        for (int d = 2; d < 1000; d++) {
            int currentRecurrence = findRecurrence(d);
            if (currentRecurrence > highestRecurrence) {
                highestRecurrence = currentRecurrence;
                maxDenominator = d;
            }
        }

        System.out.printf("The longest recurrence is for denominator %d with a cycle length of %d.%n", maxDenominator, highestRecurrence);
    }

    private static int findRecurrence(int denominator) {
        HashMap<Integer, Integer> modMap = new HashMap<>();
        int numerator = 10;
        int counter = 0;

        while (true) {
            int mod = numerator % denominator;
            if (mod == 0)
                return 0; //No recurrence
            if (modMap.containsKey(mod))// Current position - first occurrence position gives cycle length
                return counter - modMap.get(mod);
            modMap.put(mod, counter);
            numerator = mod * 10;
            counter++;
        }
    }
}