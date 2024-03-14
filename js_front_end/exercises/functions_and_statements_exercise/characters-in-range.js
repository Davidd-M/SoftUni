function solve(a, b) {
    result = []

    if (a.charCodeAt() < b.charCodeAt()) {
        for (let index = a.charCodeAt() + 1; index < b.charCodeAt(); index++) {
            result.push(String.fromCharCode(index))
            
        }
        console.log(...result);    
    } else {
        for (let index = b.charCodeAt() + 1; index < a.charCodeAt(); index++) {
            result.push(String.fromCharCode(index))
            
        }
        console.log(...result); 
    }
}

solve(
    'C',
    '#'
)