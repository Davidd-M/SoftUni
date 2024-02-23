function solve(number) {
    let number_str = number.toString();
    let sum = 0

    for (let i =0; i < number_str.length; i++) {
        sum += Number(number_str[i]);
    }
    console.log(sum);
}

solve(245678)