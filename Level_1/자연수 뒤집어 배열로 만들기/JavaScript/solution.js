function solution(n) {
    var answer = [];
    var stringN = n.toString();
    for(let i= 0; i<stringN.length; i++) {
        answer[i] = parseInt(n%10);
        n = n/10;
    }
    return answer;
}