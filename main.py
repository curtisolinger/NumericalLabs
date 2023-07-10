from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd
import json
import plotly
import plotly.express as px
from semigroups import (
    min_value_length_c,
    create_semigroup,
    calculate_max_factorization_length,
    calculate_num_of_elements_with_max_length_k,
    create_invariants,
)

maximal_length = 50
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

class GeneratorForm(FlaskForm):
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
    form = SemigroupForm()

    if form.validate_on_submit():
        generators_input = form.generators.data
        generators = [int(gen) for gen in generators_input.split(",")]
        generators.sort()
        c = min_value_length_c(generators, maximal_length)
        semigroup = create_semigroup(generators, c)
        invariant_dict = create_invariants(semigroup, generators)
        max_factorization_lengths = calculate_max_factorization_length(semigroup, generators, c)
        length_counts = calculate_num_of_elements_with_max_length_k(max_factorization_lengths)
        df = pd.DataFrame.from_dict(length_counts, orient='index', columns=['num'])
        df = df[df.index <= maximal_length]
        df.sort_index(inplace=True)
        # Insert a row with index 0 and num value 0
        df.loc[-1] = [0]
        df.index = df.index + 1
        df.sort_index(inplace=True)
        fig = px.line(df)
        graphjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('semigroups.html', graphJSON=graphjson, form=form, invariant_dict=invariant_dict)

    generators = [2, 3]
    c = min_value_length_c(generators, maximal_length)
    semigroup = create_semigroup(generators, c)
    invariant_dict = create_invariants(semigroup, generators)
    max_factorization_lengths = calculate_max_factorization_length(semigroup, generators, c)
    length_counts = calculate_num_of_elements_with_max_length_k(max_factorization_lengths)
    df = pd.DataFrame.from_dict(length_counts, orient='index', columns=['num'])
    df = df[df.index <= maximal_length]
    df.sort_index(inplace=True)
    # Insert a row with index 0 and num value 0
    df.loc[-1] = [0]
    df.index = df.index + 1
    df.sort_index(inplace=True)
    fig = px.line(df)
    graphjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    exe0 = [3, 5, 6, 8, 9, 10, 11, 12, 13, 14]

    return render_template('semigroups.html',
                           graphJSON=graphjson,
                           form=form,
                           invariant_dict=invariant_dict,
                           exe0=exe0
                           )


if __name__ == '__main__':
    app.run(debug=True)
