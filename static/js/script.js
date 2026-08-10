// Display the board


const boardElement = document.getElementById("chessboard");
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

        boardElement.appendChild(square);
    }
}

for (const file of files) {
    const letter = document.createElement("div");
    letter.textContent = file;
    filelabels.appendChild(letter);
}

// display pieces


const pieces = {
    "1": "p",
    "2": "b",
    "3": "n",
    "4": "r",
    "5": "q",
    "6": "k"
};

async function showPieces() {
    const response = await fetch('/board');
    const board = await response.json();
    const squares = boardElement.querySelectorAll(".square");

    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            const value = board[7 - row][col];
            const square = squares[row * 8 + col];

            if (value === 0) {
                continue;
            }
            const color = value > 0 ? "w" : "b";
            const pieceValue = color + pieces[Math.abs(value)];
            const piece = document.createElement("img");
            piece.src = "static/pieces/" + pieceValue + ".png";

            square.appendChild(piece);

        }
    }

}

showPieces();
