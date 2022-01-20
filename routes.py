from flask import Flask,Blueprint,request,render_template,redirect,flash,url_for
from PythonProjects.forms import NamerForm
from PythonProjects.models import demo
from PythonProjects.models import db


home = Blueprint('main',__name__,template_folder='templates')
 
@home.route('/', methods=['GET'])
def main():
    detailsdata = demo.query.all()
    return render_template("main.html", detailsdata = detailsdata)

@home.route('/add', methods=['GET','POST'])
def index():
    form = NamerForm()

    if request.method=='POST':
        if form.validate_on_submit():
            # Save data to DB
            formdata = demo(
                name=form.name.data,
                password=form.password.data
            )
            db.session.add(formdata)
            db.session.commit()
    return render_template('index.html', form=form)
    
