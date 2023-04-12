from landlord_class import Landlord
from tenant_class import Tenant
from rental_income_record_class import RentalIncomeRecord
from expense_record_class import ExpenseRecord
from annual_report_class import AnnualReport

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
landlord = Landlord()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_tenant', methods=['GET', 'POST'])
def add_tenant():
    if request.method == 'POST':
        apartment_number = request.form['apt_number']
        name = request.form['name']
        rate = float(request.form['rate'])
        landlord.add_tenant(apartment_number, name, rate)
        return redirect(url_for('index'))
    return render_template('add_tenant.html')


@app.route('/tenant_list')
def tenant_list():
    return render_template("tenant_list.html", tenants=sorted(landlord.tenant_list, key=lambda x: x.apartment_number))


@app.route('/record_rental_income', methods=['GET', 'POST'])
def record_rental_income():
    if request.method == 'POST':
        apartment_number = request.form['apt_number']
        amount = float(request.form['amount'])
        date = request.form['date']
        landlord.record_rental_income(apartment_number, amount, date)
        return redirect(url_for('rental_income_record'))
    return render_template('record_rental_income.html', tenants=landlord.tenant_list)

@app.route('/rental_income_record')
def rental_income_record():
    return render_template('rental_income_record.html', rental_income_record=landlord.rental_income_record)

@app.route('/record_expense', methods=['GET', 'POST'])
def record_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = request.form['date']
        landlord.record_expense(description, amount, date)
        return redirect(url_for('expense_record'))
    return render_template('record_expense.html')

@app.route('/expense_record')
def expense_record():
    return render_template('expense_record.html', expense_record=landlord.expense_record)

@app.route('/annual_report', methods=['GET', 'POST'])
def annual_report():
    if request.method == 'POST':
        year = int(request.form['year'])
        report = landlord.get_annual_report(year)
        return render_template('annual_report.html', report=report)
    return render_template('annual_report.html', report=None)

if __name__ == '__main__':
    app.run(debug=True)
