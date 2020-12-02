// Preprocessed input:
const input =[[1, 7, "j", "vrfjljjwbsv"]]


//Part 1
function validate(min, max, letter, string) {
    var re = new RegExp(letter, 'g');
    var arr = (string.match(re) || []).length;
    return (min <= arr && arr <= max);
}

// Part 2
function validate2(first, second, letter, string) {
    var fst = string.charAt(first - 1) === letter;
    var snd = string.charAt(second - 1) === letter;
    return (fst ^ snd);
}

function getSum(total, elem) {
    return total + validate(elem[0], elem[1], elem[2], elem[3]);
}

function getSum2(total, elem) {
    return total + validate2(elem[0], elem[1], elem[2], elem[3]);
}

console.log(input.reduce(getSum, 0));
console.log(input.reduce(getSum2, 0));