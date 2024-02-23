function solve(type, grams, pricePerKg) {
    grams /= 1000
    let money = grams * pricePerKg;

    console.log(`I need $${money.toFixed(2)} to buy ${grams.toFixed(2)} kilograms ${type}.`);
}