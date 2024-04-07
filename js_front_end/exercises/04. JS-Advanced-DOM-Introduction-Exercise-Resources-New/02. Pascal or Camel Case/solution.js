function solve() {
    const textElement = document.getElementById('text');
    const namingConventionElement = document.getElementById('naming-convention');
    const resultElement = document.querySelector('#result');

    const text = textElement.value;
    const namingConvention = namingConventionElement.value;

    let converter = {
        "Pascal Case": text => text.toLowerCase()
            .split(" ")
            .map(word => word[0].toUpperCase()
                + word.slice(1)).join(""),

        "Camel Case": text => text.toLowerCase()
            .split(" ")
            .map((word, index) => index === 0 ? word : word[0].toUpperCase() + word.slice(1))
            .join("")
    }

    let result = ""
    if (!(Object.keys(converter).includes(namingConvention))) {
        result = "Error!"
    } else {
        result = converter[namingConvention](text)
    }

    resultElement.textContent += result

}