#@d_m_y_t_r_o_19
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Dmytro Bober TZ-82'

@app.route('/first')
def kuku():
    a = "qwerty"
    b = 123
    c = None
    return f'{a}.{b}.{c}'
    
if name == '__main__':
  app.run('0.0.0.0')
