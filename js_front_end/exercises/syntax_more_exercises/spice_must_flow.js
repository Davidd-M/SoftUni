function solve(starting_yield){
    let days = 0;
    let storage = 0;
    while (starting_yield >= 100) {
        storage += starting_yield - 26
        days += 1
        starting_yield -= 10
        }
    console.log(days);
    if (storage >= 26){
        console.log(storage - 26);
    } else {
        console.log(storage);
    }
}

solve(450)