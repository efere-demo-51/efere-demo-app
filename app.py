Contents:
import os
from app import create_app
from models import db, Role, User, Contribution, Transaction

app = create_app()
app.app_context().push()

def reset_db():db.drop_all()db.create_all()

def seed():Roles
 r_super = Role(name='Super Admin')r_admin = Role(name='Admin')r_manager = Role(name='Manager')db.session.add_all([r_super, r_admin, r_manager])db.session.commit()

Users (Super Admin and 3 members). Passwords are plaintext for demo convenience.
 super_admin = User(name='Super Admin', phone='+2348083884445', password='EfereDemo!2025$', role=r_super)ada = User(name='Ada Okoro', phone='+2348000000001', password='password1', role=r_manager)chidi = User(name='Chidi Umeh', phone='+2348000000002', password='password2', role=r_manager)funke = User(name='Funke Afolayan', phone='+2348000000003', password='password3', role=r_manager)db.session.add_all([super_admin, ada, chidi, funke])db.session.commit()

Contributions (5)
 contribs = [Contribution(member=ada, amount=5000, note='January contribution'),Contribution(member=ada, amount=3000, note='February contribution'),Contribution(member=chidi, amount=4500, note='January contribution'),Contribution(member=funke, amount=2000, note='One-off'),Contribution(member=funke, amount=2500, note='March contribution'),]db.session.add_all(contribs)

Transactions (10 sample transactions)
 txs = [Transaction(description='Office rent', amount=-15000),Transaction(description='Stationery', amount=-2000),Transaction(description='Member payouts', amount=-5000),Transaction(description='Donation', amount=10000),Transaction(description='Interest income', amount=500),Transaction(description='Deposit', amount=20000),Transaction(description='Withdrawal', amount=-3000),Transaction(description='Utilities', amount=-1200),Transaction(description='Transport', amount=-800),Transaction(description='Misc', amount=-400),]db.sessiondb.session.commitprint('Seed complete. Super Admin phone: +2348083884445 password: EfereDemo!2025$')

if __name__ == '__main__':reset_db()seed()
