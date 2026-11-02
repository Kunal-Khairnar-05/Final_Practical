public class Fibonacci {
    static int steps = 0;

    static int fibRec(int n) {
        steps++;
        if (n <= 1) return n;
        return fibRec(n - 1) + fibRec(n - 2);
    }

    public static void main(String[] args) {
        int n = 10;

        // Non-recursive
        int a = 0, b = 1, count = 0;
        System.out.print("Series: " + a + " " + b);
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
            count++;
            System.out.print(" " + c);
        }
        System.out.println("\nIterative: F(" + n + ") = " + b + ", steps = " + count);

        // Recursive
        System.out.println("Recursive: F(" + n + ") = " + fibRec(n) + ", steps = " + steps);
    }
}
