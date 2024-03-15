function solve(num) {
    const renderProgressBar = (num) => `[${'%'.repeat(num / 10)}${'.'.repeat(10 - num / 10)}]`
    if (num === 100) {
        console.log('100% Complete!');
        console.log(renderProgressBar(num))
    } else {
        console.log(`${num}% ` + renderProgressBar(num))
        console.log("Still loading...");
    }
}

solve(30);
solve(100);