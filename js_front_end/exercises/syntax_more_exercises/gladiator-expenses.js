function solve(lost_fights, helmet_price, sword_price, shield_price, armor_price){
    let total_price = 0
    let shield_breaks = 0
    for (let index = 1; index <= lost_fights; index++) {
        if (index % 2 === 0){
            total_price += helmet_price
        } 
        if (index % 3 === 0) {
            total_price += sword_price
        }
        if (index % 2 === 0 && index % 3 === 0) {
            total_price += shield_price
            shield_breaks += 1
        }
        if (shield_breaks % 2 === 0 && shield_breaks !== 0) {
            total_price += armor_price
            shield_breaks = 0
        }
    }
    console.log(`Gladiator expenses: ${total_price.toFixed(2)} aureus`);
}

solve(23
    12.50
    21.50
    40
    200
    )