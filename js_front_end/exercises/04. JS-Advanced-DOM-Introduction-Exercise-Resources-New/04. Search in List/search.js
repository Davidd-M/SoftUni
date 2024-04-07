function search() {
    const townsElement = document.getElementById("towns");
    const resultElement = document.getElementById("result");
    let searchedText = document.getElementById("searchText").value;
    
    let townsList = Array.from(townsElement.children)
    let matches = 0

    for (let town of townsList) {
            town.style.textDecoration = "none";
            town.style.fontWeight = "normal";
        if (town.textContent.toLowerCase().includes(searchedText.toLowerCase())) {
            town.style.textDecoration = "underline";
            town.style.fontWeight = "bold";
            matches++
        }
    }
    
    resultElement.textContent = `${matches} matches found`
}
