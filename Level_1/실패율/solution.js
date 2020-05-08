function solution(N, stages) {
    var answer = [];
    var failure_ratio = new Array(N);

    for (var i = 1; i < N +1; i++) {
        var challenger_count = 0;
        var failure_count = 0;
        for (var j = 0; j < stages.length; j++) {
            if (stages[j] >= i) {
                challenger_count++;
            }
            if (stages[j] == i) {
                failure_count++;
            }
        }
        if ((challenger_count == 0) || (failure_count == 0)) {
            failure_ratio[i-1] = [i, 0];
        } else {
            failure_ratio[i-1] = [i, (failure_count / challenger_count)];
        }
    }
    // console.log(failure_ratio);
    failure_ratio.sort(function (a,b) {
        if (a[1] == b[1]) {
            return a[0] - b[0];
        }
        return b[1] - a[1];
    });
    console.log(failure_ratio);
    for (var i = 0; i < N; i++) {
        answer[i] = failure_ratio[i][0];
    }
    return answer;
}
