"""Pet Adoption app"""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pets
from forms import AddPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "thesecretekey898912"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
with app.app_context():
    connect_db(app)

    
@app.route('/')
def home():
    return redirect('/pets')

@app.route('/pets')
def user_list():
    """route main user list"""
    pets = Pets.query.all()
    return render_template('list_pets.html',pets = pets)


@app.route('/add', methods=['GET','POST'])
def add_user_form():

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        img_url = form.img_url.data
        age = form.age.data
        comment = form.comment.data
        available = form.available.data
        pet = Pets(name=name,species=species,img_url=img_url,age=age,comment=comment,available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template(
            "add_pet.html", form=form)


@app.route('/pets/<user_id>')
def pet_detail(user_id):
    pet = Pets.query.get_or_404(user_id)
    return render_template('pet_detail.html', pet = pet)



@app.route('/pets/<pet_id>/edit', methods=["GET","POST"])
def edit_pet(pet_id):
    pet = Pets.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
       pet.name = form.name.data
       pet.species = form.species.data
       pet.img_url = form.img_url.data
       pet.age = form.age.data
       pet.comment = form.comment.data
       pet.available = form.available.data
       db.session.commit()
       return redirect ('/')
    else:
        return render_template('edit_pet.html', form=form)

