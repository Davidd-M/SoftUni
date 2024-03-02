function solve(inpString){
    const pattern = /#([a-zA-Z]+)/g
    matches = inpString.matchAll(pattern)
    for (const match of matches) {
        console.log(match[1]);
    }
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia')