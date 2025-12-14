import generate_password_hash

def run_seed():app = create_app()with app.app_context():db.create_all()try:from models import Userexcept Exception:from app.models import User

if not User.query.filter_by(phone='+2348083884445').first():user = User(phone='+2348083884445')if hasattr(user, 'password'):user.password = generate_password_hash('EfereDemo!2025$')else:if hasattr(user, 'set_password'):user.set_password('EfereDemo!2025$')db.session.add(user)db.session.commit()print("Demo user created: +2348083884445 / EfereDemo!2025$")else:print("Demo user already exists.")

if __name__ == '__main__':run_seed()
