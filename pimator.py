from flask import Flask
from flask import render_template
from flask import redirect
import transmitter
app = Flask(__name__)

@app.route('/')
def index_pimator():
    return render_template('index.html')

@app.route('/outlet/<string:outlet>/<string:state>', methods=['POST'])
def apply_state_to_one_outlet(outlet, state):
    transmitter.apply_state_to_one_outlet(outlet, state)
    return redirect('/', code=302)

@app.route('/outlet/all/<string:state>', methods=['POST'])
def apply_state_to_all_outlets(state):
    transmitter.apply_state_to_all_outlets(state)
    return redirect('/', code=302)

#if __name__ == "__main__":
#    app.run(debug=True, host="0.0.0.0")
