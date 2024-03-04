function solve(input){
    let username = input.shift();
    let tries = 0;
    for (const usernameElement of input) {
        tries += 1
        if (username === usernameElement.split('').reverse().join('')){
            console.log(`User ${username} logged in.`)
            break
        } else if (tries < 4) {
            console.log("Incorrect password. Try again.")
        } else if (tries === 4) {
            console.log(`User ${username} blocked!`)
            break
        }
    }
}

solve(['sunny','rainy','cloudy','sunny','not sunny'])