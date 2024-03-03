function solve(input) {
    result = input.split(/(?=[A-Z])/)
    console.log(result.join(", "));
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan')