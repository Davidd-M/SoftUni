function solve(numbers) {
    numbers.sort((a, b) => a-b)
    result = []

    while (numbers.length > 0) {
        smallest = numbers.shift()
        biggest = numbers.pop()
        result.push(smallest)
        if (biggest !== undefined) {
            result.push(biggest)
        }
    }
    return result
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));