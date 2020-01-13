class Solution {
  public int[] solution(long n) {
      String stringN = "" + n;
      int[] answer = new int[stringN.length()];
      int cnt = 0;
      while(n>0) {
          answer[cnt]=(int)(n%10);
          n/=10;
          cnt++;
      }
      return answer;
  }
}