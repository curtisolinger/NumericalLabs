from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from semigroups import (
    create_semigroup,
    calc_num_of_elements_of_len_k,
    create_invariants,
    create_factorization_fig,
)

# Set the max factorization length to which you wish to examine
N = 50
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class Example2Form(FlaskForm):
    generators = StringField('Generators (comma-separated)', validators=[
        DataRequired()], default="3, 5")
    submit = SubmitField('Submit')


class SemigroupForm(FlaskForm):
    generators = StringField('Generators (comma-separated)', validators=[
        DataRequired()], default="2, 3")
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/semigroups', methods=['GET', 'POST'])
def semigroups():
    example_1 = [3, 5, 6, 8, 9, 10, 11, 12, 13, 14]
    form = SemigroupForm()
    example2form = Example2Form()

    if form.validate_on_submit():
        gen = sorted([int(gen) for gen in form.generators.data.split(",")])
        semigroup = create_semigroup(gen, N)
        invariant_dict = create_invariants(semigroup, gen)
        length_counts = calc_num_of_elements_of_len_k(semigroup, gen, N)
        graphjson = create_factorization_fig(N, length_counts)

        return render_template('semigroups.html',
                               graphJSON=graphjson,
                               form=form,
                               invariant_dict=invariant_dict,
                               example_1=example_1,
                               )

    gen = [2, 3]
    semigroup = create_semigroup(gen, N)
    invariant_dict = create_invariants(semigroup, gen)
    length_counts = calc_num_of_elements_of_len_k(semigroup, gen, N)
    graphjson = create_factorization_fig(N, length_counts)

    return render_template('semigroups.html',
                           graphJSON=graphjson,
                           form=form,
                           invariant_dict=invariant_dict,
                           example_1=example_1,
                           )


if __name__ == '__main__':
    app.run(debug=True)
