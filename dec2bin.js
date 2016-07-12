// input - decimal number (int)
// output - binary number (str)

// until number == 0
// first time through, just subtract 1 from odds
// determine if multiple of 2^i
// if so, add 0 to beginning of str
// else, add 1
//   subtract 2^i

// if input == 9
// output should be '101'

// num = 8
// i   = 3
// 2^i = 8
// out = '101'

function dec2bin(num) {
    var isEven = num % 2;
    var bin = isEven.toString();
    num = num - isEven;
    var i = 2;
    while (num > 0) {
        // console.log(num);
        if (num % Math.pow(2, i) === 0) {
            bin = "0" + bin;
        } else {
            bin = "1" + bin;
            num = num - Math.pow(2, i);
        }
        i++;
    }
    return bin
}