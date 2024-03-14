function solve(number) {
    odd_sum = 0
    even_sum = 0
    number_str = number.toString();
    for (const item of number_str) {
        if (Number(item) % 2 === 0) {
            even_sum += Number(item)
        } else {
            odd_sum += Number(item)
        };
    }
    console.log(`Odd sum = ${odd_sum}, Even sum = ${even_sum}`);
}

solve(1000435)