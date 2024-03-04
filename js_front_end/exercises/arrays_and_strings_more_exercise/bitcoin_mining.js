function solve(gold_per_days){
    const one_bitcoin = 11949.16;
    const gram_of_gold = 67.51;
    let my_money = 0
    let my_bitcoins = 0
    let day = 0

    for (let [index, shifts_gold] of gold_per_days.entries()) {

        if ((index + 1) % 3 === 0){
            shifts_gold *= 0.7
        }

        my_money += shifts_gold * gram_of_gold

        while (my_money >= one_bitcoin){
            (day === 0) ? day = index + 1 : ''; 
            my_money -= one_bitcoin
            my_bitcoins += 1
        }

    }

    console.log(`Bought bitcoins: ${my_bitcoins}`);
    (day !== 0) ? console.log(`Day of the first purchased bitcoin: ${day}`) : '';
    console.log(`Left money: ${my_money.toFixed(2)} lv.`);
}

solve([3124.15, 504.212, 2511.124])