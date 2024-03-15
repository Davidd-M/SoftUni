function solve(num) {
    function getDivisors(num) {
        let divisors = [];
        for (let i = 0; i < num; i++) {
            if (num % i === 0) {
                divisors.push(i);
            }
        }
        return divisors;
    }

    const divisors = getDivisors(num);

    const sum = divisors.reduce((a, b) => a + b, 0);
    if (sum === num) {
        console.log("We have a perfect number!");
    } else {
        console.log("It's not so perfect.");    
    }
}

solve(6);