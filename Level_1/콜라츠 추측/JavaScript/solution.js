function solution(num) {
    var answer = 0;
    var count = 0;
    if (num == 1) {
        answer = 0;
    } else {
        while(num != 1) {
            if(count >= 500) {
                answer = -1;
                break;
            } else {
                count ++;
                if (num%2 == 0) {
                    num = num/2;
                } else {
                    num = (num*3) +1;
                }
                answer = count;
            }
        }
    }
    return answer;
}