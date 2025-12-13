Contents:
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from config import Config
from models import db, User, Role, Contribution, Transaction

def create_app():app = Flask(__name__, template_folder='templates', static_folder='static')app.config.from_object(Config)db.init_app(app)

login = LoginManager()login.login_view = 'login'login.init_app(app)

@login.user_loaderdef load_user(user_id):return User.query.get(int(user_id))

@app.route('/')def index():return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])def login():if request.method == 'POST':phone = request.form.get('phone')password = request.form.get('password')user = User.query.filter_by(phone=phone).first()if user and user.password == password:login_user(user)return redirect(url_for('dashboard'))else:flash('Invalid credentials', 'danger')return render_template('login.html')

@app.route('/logout')@login_requireddef logout():logout_user()return redirect(url_for('index'))

@app.route('/dashboard')@login_requireddef dashboard():contrib_count = Contribution.query.count()total_contrib = db.session.query(db.func.sum(Contribution.amount)).scalar() or 0balance = db.session.query(db.func.sum(Transaction.amount)).scalar() or 0return render_template('dashboard.html', contrib_count=contrib_count, total_contrib=total_contrib, balance=balance)

@app.route('/members')@login_requireddef members():users = User.query.all()return render_template('members.html', users=users)

@app.route('/contributions')@login_requireddef contributions():contribs = Contribution.query.order_by(Contribution.date.desc()).all()return render_template('contributions.html', contribs=contribs)

@app.route('/finances')@login_requireddef finances():txs = Transaction.query.order_by(Transaction.date.desc()).all()return render_template('finances.html', txs=txs)

return app

For local runs
 
if __name__ == '__main__':app = create_app()app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
