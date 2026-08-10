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


if __name__ == '__main__':
    app.run(debug=True)
