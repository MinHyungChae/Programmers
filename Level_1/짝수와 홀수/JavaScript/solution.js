function solution(num) {
    var answer = '';
    answer = check(num);
    return answer;
}

function check(num) {
    return (num % 2 === 0) ? 'Even' : 'Odd';
}