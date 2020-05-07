function solution(n, arr1, arr2) {
    var arr1_binary = parseBinary(arr1);
    var arr2_binary = parseBinary(arr2);
    // console.log(arr1_binary);
    // console.log(arr2_binary);
    var temp = new Array(n);
    for (var i = 0; i < n; i++) {
        for(var j = 0; j < n; j++) {
            var arr1_char = String(arr1_binary[i]).charAt(j);
            var arr2_char = String(arr2_binary[i]).charAt(j);
            if ((arr1_char == '0') && (arr2_char == '0')) {
                temp[i] = temp[i] + ' ';
            } else {
                temp[i] = temp[i] + '#';
            }
        }
        temp[i] = temp[i].replace('undefined', ''); // cannot find solutions not to get undefined
    }
    console.log(temp);
    return temp;
}

function parseBinary (arr) {
    for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i].toString(2);
        if (arr[i].length != arr.length) {
            while(arr[i].length != arr.length) {
                arr[i] = '0' + arr[i];
            }
        }
    }
    return arr;
}
