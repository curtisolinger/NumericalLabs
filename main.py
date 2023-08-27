import os
import re
from flask import Flask, render_template, session, request, jsonify
# from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email, Optional
from flask_wtf.csrf import CSRFProtect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from semigroups import (
    create_semigroup,
    calc_num_of_elements_of_len_k,
    create_invariants,
    create_factorization_fig,
    create_example_1,
    create_invariants_for_single_element,
)

# Set the max factorization length to which you wish to examine
N = 20

load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL = os.environ.get('EMAIL')

print(SECRET_KEY)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)


class ContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name  = StringField('Last Name', validators=[Optional()])
    email = EmailField('Email', validators=[Email(message='Please enter a valid email')])
    subject = StringField('Subject', validators=[InputRequired()])
    message_to_send = StringField('Message', validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/semigroups')
def semigroups():
    return render_template('semigroups.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        data = request.form
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        subject = data['subject']
        message_to_send = data['message_to_send']

        print(first_name)
        print(type(first_name))
        print('\n')

        print(last_name)
        print(type(last_name))
        print('\n')

        print(email)
        print(type(email))
        print('\n')

        print(subject)
        print(type(subject))
        print('\n')

        print(message_to_send)
        print(type(message_to_send))
        print('\n')

        message = Mail(
            from_email=EMAIL,
            to_emails=EMAIL,
            subject=subject,
            # html_content=message_to_send)
            html_content = f"""
                Message from NumericalLabs.com contact form<br>
                From: {first_name} {last_name}<br>
                Email: {email}<br>
                Subject: {subject}<br>
                Message: {message_to_send}
                """)
        
        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

        
        return render_template('contact.html', msg_sent=True, form=form)
    
    return render_template('contact.html', msg_sent=False, form=form)



@app.route('/calculateSemigroup', methods=['POST'])
def calculate_semigroup():
    data = request.form['gen01']

    # Validate the input
    if not re.match(r"^(\d+)(,\s*\d+)*$", data):
        return jsonify(error="Invalid input. Please enter comma-separated integers only.")

    gen01 = [int(x) for x in data.split(',')]
    print("I'm working!")

    semigroup = create_semigroup(gen01, 5)

    semigroup_list = []
    for element in semigroup:
        semigroup_list.append(element.number())
    
    semigroup_set = set(semigroup_list)
    semigroup_list = sorted(list(semigroup_set))
    semigroup_list = semigroup_list[:20]
    print(semigroup_list)

    return jsonify(result=semigroup_list)


@app.route('/calculateFactorizationLengths', methods=['POST'])
def calculate_factorization_lengths():
    data = request.form['gen02']
    
    # Validate the input
    if not re.match(r"^(\d+)(,\s*\d+)*$", data):
        return jsonify(error="Invalid input. Please enter comma-separated integers only.")
    gen02 = [int(x) for x in data.split(',')]

    element_data = request.form['element01']

    # Validate the single integer input
    if not re.match(r"^\d+$", element_data):
        return jsonify(error="Invalid input. Please enter a valid integer.")
    
    element = int(element_data)
    semigroup2 = create_semigroup(gen02, N)
    single_element_invariant_list = create_invariants_for_single_element(semigroup2, element, gen02)
    
    return jsonify(result2=single_element_invariant_list)



@app.route('/createSecondFrobeniusGraph', methods=['POST'])
def create_second_frobenuis_graph():
    data = request.form['gen03']

    # Validate the input
    if not re.match(r"^(\d+)(,\s*\d+)*$", data):
        return jsonify(error="Invalid input. Please enter comma-separated integers only.")
    gen03 = [int(x) for x in data.split(',')]

    semigroup3 = create_semigroup(gen03, N)
    length_counts = calc_num_of_elements_of_len_k(semigroup3, gen03, N)
    df = create_factorization_fig(N, length_counts)
    
    # Convert the dataframe to a list of dictionaries
    data_for_vega = df.reset_index().to_dict(orient="records")

    # print(data_for_vega)
    # return jsonify(data_for_vega)

    labels = list(df.index)
    values = list(df['num'])



    data_for_chartjs = {
        "labels": labels,
        "datasets": [{
            "label": "Sample Data",
            "data": values,
            "fill": False,
            "borderColor": "rgb(75, 192, 192)"
        }]
    }

    print(data_for_chartjs)

    return jsonify(data_for_chartjs)


if __name__ == '__main__':
    app.run(debug=True)
