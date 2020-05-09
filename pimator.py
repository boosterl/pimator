from flask import Flask
from flask import render_template
from flask import redirect
from transmitter import Transmitter
from config import Config
app = Flask(__name__)
config = Config()
transmitter = Transmitter(config)


@app.route('/')
def index_pimator():
    return render_template('index.html', codes=config.codes, application_prefix=config.application_prefix)


@app.route('/outlet/<string:outlet>/<string:state>', methods=['POST'])
def apply_state_to_one_outlet(outlet, state):
    transmitter.apply_state_to_one_outlet(outlet, state)
    return redirect(config.application_prefix, code=302)


@app.route('/outlet/all/<string:state>', methods=['POST'])
def apply_state_to_all_outlets(state):
    transmitter.apply_state_to_all_outlets(state)
    return redirect(config.application_prefix, code=302)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")
