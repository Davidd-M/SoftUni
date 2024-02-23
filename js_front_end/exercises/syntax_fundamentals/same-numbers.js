function solve (number) {
    let number_str = number.toString();
    let firstDigit = number_str[0]
    let result = true
    let sum = 0


    for (let i = 0; i < number_str.length; i++) {
        if (firstDigit !== number_str[i]) {
            result = false
        }
        sum += Number(number_str[i])
    }
    console.log(result);
    console.log(sum);
}