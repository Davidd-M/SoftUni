function solve() {
    document.querySelector('#searchBtn').addEventListener('click', onClick);

    function onClick() {

        const tableElement = document.querySelectorAll(".container tbody tr")
        const searchedTextElement = document.getElementById("searchField")
        let searchedText = searchedTextElement.value

        for (let elRow of tableElement) {
            elRow.className = ''

            let tdElements = elRow.querySelectorAll('td')

            for (let elCol of tdElements) {
                if (elCol.textContent.includes(searchedText)) {
                    console.log(searchedText)
                    console.log(elCol.textContent)
                    elRow.className = "select"
                }
            }
        }
    }
}