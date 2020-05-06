function solution(board, moves) {
    var bucket = new Array(); // put picked number from board
    var count = 0;
    for (var i = 0; i < moves.length; i++) {
        var board_index = moves[i] -1;
        for (var j = 0; j < board.length; j++) {
            if (board[j][board_index] != 0) {
                // if find non-empty
                bucket.push(board[j][board_index]);
                board[j][board_index] = 0; // make empty after pick up <- important
                boom(bucket.length);
                break;
            } else {
                // data == 0
                if (j < board.length -1) {
                    continue;
                } else {
                    // bucket.push(board[j][board_index]);
                    // boom(bucket.length);
                    break;
                }
            }
        }
    }
    function boom(bucket_length) {
        if(bucket[bucket_length - 1] == bucket[bucket_length - 2]) {
            bucket.splice(bucket_length-2, 2);
            count += 2;
        }
    }
    console.log(bucket);
    return count;
}
