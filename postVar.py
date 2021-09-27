from wtforms import Form, StringField, SubmitField, SelectField, TextAreaField, IntegerField, validators

class Post(Form):
    title = StringField('Title',[validators.DataRequired()])
    text = TextAreaField('Text', [validators.DataRequired()])
    submit = SubmitField('', [validators.DataRequired()])

class Announcement(Form):
    announcement = StringField('Announcement', [validators.DataRequired()])
    content = TextAreaField('Content', [validators.DataRequired()])
    submit = SubmitField('', [validators.DataRequired()])

class Contact(Form):
    email = StringField('Email Address:', [validators.DataRequired()])
    subject = StringField('Subject:', [validators.DataRequired()])
    message = TextAreaField('Your message:', [validators.DataRequired()])
    submit = SubmitField('', [validators.DataRequired()])

class User_recipe(Form):
    name = StringField('Food Name', [validators.DataRequired()])
    type = SelectField('Type', [validators.DataRequired()], choices=[('Healthy', 'Healthy'), ('Unhealthy', 'Unhealthy')])
    prep_time = IntegerField('Preparation Time (in minutes)', [validators.DataRequired()])
    cooking_time = IntegerField('Cooking Time (in minutes)', [validators.DataRequired()])
    calories = IntegerField('Calories (per serving)', [validators.DataRequired()])
    ingredients = StringField('Ingredients', [validators.DataRequired()])
    recipes = TextAreaField('Recipes', [validators.DataRequired()])
    submit = SubmitField('', [validators.DataRequired()])

class Recipes(Form):
    name = StringField('Food Name:')#add placeholder
    photo = StringField('Photo URL:')
    prep = IntegerField('Preparation Time (in minutes):')
    cook = IntegerField('Cooking Time (in minutes):')
    cal = IntegerField('Calories (per serving):')
    serves = IntegerField('Number of Servings:')
    healthy = SelectField('Type:', choices=[('Healthy', 'Healthy'), ('Unhealthy', 'Unhealthy')], default='Healthy')
    speed = SelectField('Speed:', choices=[('Fast', 'Fast'), ('Normal', 'Normal')], default='Normal')
    forBMI = StringField('BMI range:')#add placeholder
    prepItem = StringField('Preparation Ingredients:')#add placeholder
    item = StringField('Ingredients:')#add placeholder
    method = TextAreaField('Recipe:')
    submit = SubmitField('')#add value="Add"

class Add_workout(Form):
    name = StringField('Name:')
    photo = StringField('Image URL:')
    duration = IntegerField('Duration: ')
    kcal_burn = IntegerField('Calories burnt:')
    forBMI = StringField('Recommended for BMI range of:')
    submit = SubmitField('')