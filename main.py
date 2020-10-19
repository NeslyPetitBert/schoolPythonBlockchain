from block import Block
from flask import Flask, render_template, request # l'import du Framwork
from argparse import ArgumentParser

app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def index():
    print('Page index')
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def home():
    print('Page home')
    return ('<h>Hello world ! </h1>')

@app.route('/wallet', methods=['POST'])
def wallet():
    print('Page wallet')
    key = request.form.get('key')
    myBlock = Block(22, key, True)
    # return myBlock.getHashBlock
    # return "<h>Votre Wallet est le : "+ dataRequest.get('key') +"</h1>"
    return "<h>Votre Wallet est le : "+ myBlock.getHashBlock +"</h1>"

if __name__ =='__main__':
    parser = ArgumentParser()
    parser.add_argument('-H', '--host', default='127.0.0.1')
    parser.add_argument('-P', '--port', default=7000, type=int)
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=True)