from flask import Flask, render_template, jsonify

from main import Game

app = Flask(__name__)

game = Game()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/board')
def get_board():
    return jsonify(game.board)


@app.route('/turn')
def get_turn():
    return jsonify(game.turn)

if __name__ == '__main__':
    app.run(debug=True)
