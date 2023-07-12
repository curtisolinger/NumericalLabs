from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from semigroups import (
    create_semigroup,
    calc_num_of_elements_of_len_k,
    create_invariants,
    create_factorization_fig,
    create_example_1,
)

# Set the max factorization length to which you wish to examine
N = 50
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

gen1 = [2, 3]
gen2 = [3, 5]

class GeneratorForm1(FlaskForm):
    generators1 = StringField('Generators1 (comma-separated)', validators=[
        DataRequired()])
    submit = SubmitField('Submit')

# generators1 = StringField('Generators1 (comma-separated)', validators=[
        # DataRequired()], default=', '.join(str(x) for x in gen1))

class GeneratorForm2(FlaskForm):
    generators2 = StringField('Generators2 (comma-separated)', validators=[
        DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/semigroups', methods=['GET', 'POST'])
def semigroups():
    example_0 = [3, 5, 6, 8, 9, 10, 11, 12, 13, 14]

    form1 = GeneratorForm1()
    form2 = GeneratorForm2()

    global gen1
    global gen2

    print(f'Initial gen1: {gen1}, gen2: {gen2}')

    if form1.validate_on_submit():
        # gen1_str = form1.generators1.data
        gen1 = sorted([int(gen) for gen in form1.generators1.data.split(",")])
        # form1.generators1.data = ', '.join(str(x) for x in gen1)
        print(f'gen1 form submission {gen1} and gen2 is {gen2}')

    if form2.validate_on_submit():
        gen2 = sorted([int(gen) for gen in form2.generators2.data.split(",")])
        # form2.generators2.data = ', '.join(str(x) for x in gen2)
        print(f'gen2 form submission {gen2} and gen1 is {gen1}')

    semigroup1 = create_semigroup(gen1, N)
    semigroup2 = create_semigroup(gen2, N)
    example_1 = create_example_1(semigroup1)
    invariant_dict = create_invariants(semigroup2, gen2)
    length_counts = calc_num_of_elements_of_len_k(semigroup2, gen2, N)
    graphjson = create_factorization_fig(N, length_counts)

    return render_template('semigroups.html',
                           example_0=example_0,
                           form1=form1,
                           example_1=example_1,
                           form2=form2,
                           graphJSON=graphjson,
                           invariant_dict=invariant_dict,
                           )


if __name__ == '__main__':
    app.run(debug=True)
