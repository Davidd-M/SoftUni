function solve(a_str) {
    let a_list = a_str.match(/\w+/g)
    console.log(a_list.join(", ").toUpperCase());
}

solve("hi, how")