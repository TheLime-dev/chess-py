const boardElement = document.getElementById("chessboard");
const filelabels = document.getElementById("file-labels");
const ranklabels = document.getElementById("rank-labels");

const BOARD = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"], ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"], ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"], ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"], ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"], ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"], ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"], ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],];

const pieces = {
    "1": "p", "2": "b", "3": "n", "4": "r", "5": "q", "6": "k"
};

const files = ["a", "b", "c", "d", "e", "f", "g", "h"];

let selectedSquare = null;
let selectedPosition = null;
let board = [];
let curTurn = 0;


// squares
for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {

        const square = document.createElement("div");

        square.classList.add("square");

        if ((row + col) % 2 === 0) {
            square.classList.add("light");
        } else {
            square.classList.add("dark");
        }
        square.addEventListener("click", () => {

            const value = board[7 - row][col];
            let pieceColor = null;
            if (value !== 0) {
                pieceColor = value > 0 ? 0 : 1;
            }
            if (selectedSquare === null) {
                selectedSquare = null;
                selectedPosition = null;
                document.querySelectorAll(".selected").forEach(square => square.classList.remove("selected"))

                if (value === 0) {
                    return;
                }

                if (pieceColor !== curTurn) {
                    return;
                }

                selectedSquare = square;
                square.classList.add("selected");
                selectedPosition = {
                    row: 7 - row, col: col
                };
            } else {
                if (pieceColor === curTurn) {
                    document.querySelectorAll(".selected").forEach(square => square.classList.remove("selected"))
                    selectedSquare = square;
                    square.classList.add("selected");
                    selectedPosition = {
                        row: 7 - row, col: col
                    };

                } else {
                    const target = {
                        row: 7 - row, col: col
                    };
                    makeMove(selectedPosition, target);
                    selectedSquare = null;
                    selectedPosition = null;
                    document.querySelectorAll(".selected").forEach(square => square.classList.remove("selected"))

                }
            }

        })
        boardElement.appendChild(square);
    }
}


//rank labels
for (let row = 0; row < 8; row++) {
    const number = document.createElement("div");
    number.textContent = 8 - row;
    ranklabels.appendChild(number);
}


// file labels

for (const file of files) {
    const letter = document.createElement("div");
    letter.textContent = file;
    filelabels.appendChild(letter);
}

// display pieces

async function showPieces() {
    const boardResponse = await fetch('/board');
    board = await boardResponse.json();

    const squares = boardElement.querySelectorAll(".square");

    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            const value = board[7 - row][col];
            const square = squares[row * 8 + col];
            square.replaceChildren();

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

function makeMove(starting, target) {

//    const piece = pieces[Math.abs(board[7 - row][col])].upper();
    showPieces();

}

showPieces();



