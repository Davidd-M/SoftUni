function solve(wordsInput, template = '') {
    const words = wordsInput.split(", ");

    for (let word of words) {
        template = template.replace("*".repeat(word.length), word)
    }
    return template
}

console.log(solve('great',
'softuni is ***** place for learning new programming languages'
));