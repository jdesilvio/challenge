from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from forms import MyForm


app = Flask(__name__)
Bootstrap(app)
CSRFProtect(app)
app.config.from_object('dev_config')


@app.route('/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
