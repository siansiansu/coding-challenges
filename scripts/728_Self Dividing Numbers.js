/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
function isDividingNumber(num) {
    var digit = num.toString();

    for (var i = 0; i < digit.length; i++) {
        if (digit[i] == 0) {
            return false;
        } else if (num % digit[i] != 0) {
            return false;
        }
    }
    return true;
}

var selfDividingNumbers = function (left, right) {
    var answer = [];
    for (var i = left; i <= right; i++) {
        if (isDividingNumber(i)) {
            answer.push(i);
        }
    }
    return answer;
}; 