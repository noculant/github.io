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


@app.route('/record_rental_payment', methods=['GET', 'POST'])
def record_rental_payment():
    if request.method == 'POST':
        apartment_number = request.form['apartment_number']
        month = request.form['month']
        amount = float(request.form['amount'])

        landlord.rental_income_record.add_income(month, apartment_number, amount)
        return redirect(url_for('index'))
    return render_template('record_rental_payment.html')

@app.route('/rental_income_record')
def rental_income_record():
    return render_template('rental_income_record.html', income_records=landlord.rental_income_record.income_records)

@app.route('/record_expense', methods=['GET', 'POST'])
def record_expense():
    if request.method == 'POST':
        category = request.form['category']
        payee = request.form['payee']
        amount = float(request.form['amount'])
        date = request.form['date']
        landlord.expense_record.add_expense(date, payee, amount, category) # connect front end to back end
        return redirect(url_for('index'))
    return render_template('record_expense.html')


@app.route('/expense_record')
def expense_record():
    return render_template('expense_record.html', expense_record=landlord.expense_record)

@app.route('/annual_report')
def annual_report():
    # Generate the annual report
    report = landlord.generate_annual_report()

    # Pass the 'annual_report' variable to the template
    return render_template('annual_report.html', annual_report=report)

if __name__ == '__main__':
    app.run(debug=True)
