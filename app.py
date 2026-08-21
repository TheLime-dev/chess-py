from flask import Flask, render_template, jsonify, request

from main import Game

app = Flask(__name__)

game = Game()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/board')
def get_board():
    return jsonify(game.board.position)


@app.route('/turn')
def get_turn():
    return jsonify(game.turn)

@app.route('/moves')
def get_moves():
    return jsonify(game.moves)

@app.post('/move')
def move():
    data = request.get_json()
    player_move = data['move']
    if game.move(player_move):
        return jsonify({
            'ok' : True
        })
    else:
        return jsonify({
            'ok' : False
        })


if __name__ == '__main__':
    app.run(debug=True)
