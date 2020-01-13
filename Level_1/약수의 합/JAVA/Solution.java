class Solution {
  public int solution(int n) {
      int answer = 0;
      int avg = n/2;
      for (int i=1; i<= avg; i++) {
          if(n%i == 0) {
              answer += i;
          }
      }
      answer = answer + n;
      return answer;
  }
}