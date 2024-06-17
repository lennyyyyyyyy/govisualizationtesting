function setup_board() {
    var board = new WGo.Board(document.getElementById("board"), {
        width: 600,
    });
    return board;
}

function clear_board(board) {
    board.removeAllObjects();
}

function overlay_position(board, position) {
    for (let i=0; i<19; i++) {
        for (let j=0; j<19; j++) {
            if (position[i][j] == "BLACK") {
                board.addObject({x: i, y: j, c: Wgo.B});
            } else if (position[i][j] == "WHITE") {
                board.addObject({x: i, y: j, c: Wgo.W});
            }
        }
    }
}

function overlay_statistics(board, statistics) {
}

export { setup_board, clear_board, overlay_position, overlay_statistics }