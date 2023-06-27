from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd
import json
import plotly
import plotly.express as px
# import plotly.graph_objects as go
from numerical_semigroups import (
    min_value_length_c,
    generate_multisets,
    calculate_max_factorization_length,
    calculate_num_of_elements_with_max_decomposition_length_k
)

maximal_length = 50
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class NumericalSemigroupForm(FlaskForm):
    generators = StringField('Generators (comma-separated)', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/numericalsemigroups', methods=['GET', 'POST'])
def numerical_semigroups():
    form = NumericalSemigroupForm()

    if form.validate_on_submit():
        generators_input = form.generators.data
        generators = [int(gen) for gen in generators_input.split(",")]
        generators.sort()

        c = min_value_length_c(generators, maximal_length)
        elements = generate_multisets(generators, c)
        max_factorization_lengths = calculate_max_factorization_length(elements, generators, c)
        length_counts = calculate_num_of_elements_with_max_decomposition_length_k(max_factorization_lengths)
        df = pd.DataFrame.from_dict(length_counts, orient='index', columns=['num'])
        df = df[df.index <= maximal_length]
        df.sort_index(inplace=True)

        # Insert a row with index 0 and num value 0
        df.loc[-1] = [0]
        df.index = df.index + 1
        df.sort_index(inplace=True)

        # fig = go.Figure()
        # fig.update_layout(responsive=True)
        #
        # graphJSON = fig.to_json()

        fig = px.line(df)
        graphjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('numerical_semigroups.html', graphJSON=graphjson, form=form)

    return render_template('numerical_semigroups.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
