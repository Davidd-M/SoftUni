const baseUrl = 'http://localhost:3030/jsonstore/games/';

const loadGamesButton = document.getElementById('load-games');
const addGameButton = document.getElementById('add-game');
const editGameButton = document.getElementById('edit-game');
const gameListElement = document.getElementById('games-list');
const nameInputElement = document.getElementById('g-name');
const typeInputElement = document.getElementById('type');
const playersInputElement = document.getElementById('players');
const formContainerElement = document.getElementById('form');

loadGamesButton.addEventListener('click', loadGames);
addGameButton.addEventListener('click', addGame);
editGameButton.addEventListener('click', editGame);
gameListElement.addEventListener('click', deleteGame);

async function loadGames() {
    try {
        const response = await fetch(baseUrl);
        const gamesResult = await response.json();

        gameListElement.innerHTML = '';

        const gameListFragment = document.createDocumentFragment();

        Object.values(gamesResult).forEach(game => {
            gameListFragment.appendChild(createGameElement(game));
        });

        gameListElement.appendChild(gameListFragment);
    } catch (error) {
        console.error('Error loading games:', error);
    }
}

function createGameElement(game) {
    const changeButtonElement = document.createElement('button');
    changeButtonElement.classList.add('change-btn');
    changeButtonElement.textContent = 'Change';
    changeButtonElement.addEventListener('click', (e) => changeGame(e, game));

    const deleteButtonElement = document.createElement('button');
    deleteButtonElement.classList.add('delete-btn');
    deleteButtonElement.textContent = 'Delete';

    const buttonsDivElement = document.createElement('div');
    buttonsDivElement.classList.add('buttons-container');
    buttonsDivElement.appendChild(changeButtonElement);
    buttonsDivElement.appendChild(deleteButtonElement);

    const namePElement = document.createElement('p');
    namePElement.textContent = game.name;

    const typePElement = document.createElement('p');
    typePElement.textContent = game.type;

    const playersPElement = document.createElement('p');
    playersPElement.textContent = game.players;

    const contentDivElement = document.createElement('div');
    contentDivElement.classList.add('content');
    contentDivElement.appendChild(namePElement);
    contentDivElement.appendChild(typePElement);
    contentDivElement.appendChild(playersPElement);

    const boardGameDivElement = document.createElement('div');
    boardGameDivElement.classList.add('board-game');
    boardGameDivElement.appendChild(contentDivElement);
    boardGameDivElement.appendChild(buttonsDivElement);

    boardGameDivElement.setAttribute('data-id', game._id);

    return boardGameDivElement;
}

async function addGame() {
    try {
        const game = getInputData();

        const response = await fetch(baseUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(game),
        });

        if (!response.ok) {
            throw new Error('Failed to add game');
        }

        clearInputFields();

        await loadGames();
    } catch (error) {
        console.error('Error adding game:', error);
    }
}

async function editGame() {
    try {
        const game = getInputData();
        const gameId = formContainerElement.getAttribute('data-id');

        const response = await fetch(`${baseUrl}${gameId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ _id: gameId, ...game }),
        });

        if (!response.ok) {
            throw new Error('Failed to edit game');
        }

        loadGames();

        editGameButton.setAttribute('disabled', 'disabled');
        addGameButton.removeAttribute('disabled');

        clearInputFields();
    } catch (error) {
        console.error('Error editing game:', error);
    }
}

function changeGame(e, game) {
    e.stopPropagation(); // Prevent event bubbling

    const gameElement = e.currentTarget.parentElement.parentElement;

    gameElement.remove();

    nameInputElement.value = game.name;
    typeInputElement.value = game.type;
    playersInputElement.value = game.players;

    formContainerElement.setAttribute('data-id', game._id);

    editGameButton.removeAttribute('disabled');
    addGameButton.setAttribute('disabled', 'disabled');
}
async function deleteGame(e) {
    if (e.target.tagName !== 'BUTTON' || !e.target.classList.contains('delete-btn')) {
        return;
    }

    const gameElement = e.target.parentElement.parentElement;
    const gameId = gameElement.getAttribute('data-id');

    try {
        const response = await fetch(`${baseUrl}${gameId}`, {
            method: 'DELETE',
        });

        if (!response.ok) {
            throw new Error('Failed to delete game');
        }

        gameElement.remove();
    } catch (error) {
        console.error('Error deleting game:', error);
    }
}

function clearInputFields() {
    nameInputElement.value = '';
    typeInputElement.value = '';
    playersInputElement.value = '';
}

function getInputData() {
    return {
        name: nameInputElement.value,
        type: typeInputElement.value,
        players: playersInputElement.value,
    };
}
