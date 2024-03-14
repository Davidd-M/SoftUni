function solve(numbers) {
    function isPalindrome(number) {
        let array_num = number.toString().split('');
        const reversed_numbers = array_num.slice().reverse().join('');
        if (number.toString() === reversed_numbers) {
            return true;
        }
        return false;
    }
    for (const item of numbers) {
        console.log(isPalindrome(item));
    }
}

solve([123, 312, 121])