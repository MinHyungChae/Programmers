function solution(n) {
    var answer = 0;
    if (Number.isInteger(Math.sqrt(n)) == true) {
        answer = Math.pow(Math.sqrt(n)+1, 2);
    } else {
        answer = -1;
    }
    return answer;
}