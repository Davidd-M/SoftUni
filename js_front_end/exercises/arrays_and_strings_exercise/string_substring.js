function solve(word_inp, text) {
    const word = word_inp.toLowerCase();
    const text_list = text.toLowerCase().split(' ');

    for (const current_word of text_list) {
        if (word === current_word) {
            return word

        }
    }
    return `${word} not found!`
}

console.log(solve(
    'python',
'JavaScript is the best programming language')
);