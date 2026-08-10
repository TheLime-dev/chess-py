const board = document.getElementById("chessboard");
const filelabels = document.getElementById("file-labels");
const ranklabels = document.getElementById("rank-labels");

const files = ["a", "b", "c", "d", "e", "f", "g", "h"];

for (let row = 0; row < 8; row++) {
    const number = document.createElement("div");
    number.textContent = 8 - row;
    ranklabels.appendChild(number);
    for (let col = 0; col < 8; col++) {

        const square = document.createElement("div");

        square.classList.add("square");

        if ((row + col) % 2 === 0) {
            square.classList.add("light");
        } else {
            square.classList.add("dark");
        }

        board.appendChild(square);
    }
}

for (const file of files) {
    const letter = document.createElement("div");
    letter.textContent = file;
    filelabels.appendChild(letter);
}