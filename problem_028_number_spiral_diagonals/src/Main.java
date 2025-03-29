//https://projecteuler.net/problem=28
public class Main {
    public static void main(String[] args) {
        int sum = 1;//Start the sum with 1 instead of looping through i = 1.
        for (int i = 3; i < 1002; i = i + 2) {
            int difference = i-1;
            for (int j = 0; j < 4; j++) {
                sum += (i * i) - (difference * j);
            }
        }
        System.out.println(sum);
    }
}