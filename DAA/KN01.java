public class KN01 {
    public static void main(String[] args) {
        int[] w = {1, 3, 4, 5};
        int[] p = {1, 4, 5, 7};

        int Cap = 7, n= w.length;
        int[][] dp = new int[n+1][Cap+1];

        for(int i=1; i<=n; i++){
            for(int j=0;j<=Cap;j++){
                dp[i][j] = dp[i-1][j];
                if(j>=w[i-1]){
                    dp[i][j] = Math.max(dp[i][j], p[i-1] + dp[i-1][j - w[i-1]]);
                }
            }
        }
        System.out.println("Max profit : "+ dp[n][Cap]);

        int j = Cap;
        for(int i=n; i>0; i--){
            if(dp[i][j] != dp[i-1][j]){
                System.out.println("Item "+ i+ " selected");
                j-=w[i-1];
            }
        }
    }
}
