function toggle() {
    let buttonElement = document.querySelector(".button");
    let extraTextElement = document.getElementById("extra");

    let buttonText = buttonElement.textContent
    if (buttonText === "More") {
        extraTextElement.style.display = "block";
        buttonElement.textContent = "Less";
    } else {
        extraTextElement.style.display = "none";
        buttonElement.textContent = "More";
    }
}