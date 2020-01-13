class Solution {
  public double solution(int[] arr) {
      double answer = 0;
      int length = arr.length;
      double sum = 0;
      for (int i = 0; i<length; i++) {
          sum += arr[i];
      }
      answer = sum/length;
      return answer;
  }
}