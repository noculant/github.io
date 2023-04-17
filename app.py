from landlord_class import Landlord
from tenant_class import Tenant
from rental_income_record_class import RentalIncomeRecord
from expense_record_class import ExpenseRecord
from annual_report_class import AnnualReport

from flask import Flask, render_template, request, redirect, url_for

# Create the web application
app = Flask(__name__)

# Create the landlord object(tenant list, income record, expense record, annual report)
landlord = Landlord('tenants.txt')

# Display the home page
@app.route('/')
def index():
    return render_template('index.html')
    
"""
--------------------------------- ADD TENANT PAGE ---------------------------------
"""
@app.route('/add_tenant', methods=['GET', 'POST']) 
def add_tenant():
    if request.method == 'POST':
        # Get user input from webpage
        apartment_number = request.form['apartment_number']
        name = request.form['name']
        rate = float(request.form['rate'])

        # Add tenant to tenant list
        landlord.add_tenant(apartment_number, name, rate)

        # Send back to home page when finished
        return redirect(url_for('index'))
    return render_template('add_tenant.html')

"""
--------------------------------- TENANT LIST PAGE ---------------------------------
"""
@app.route('/tenant_list')
def tenant_list():
    # Display tenants in a sorted list accessed the tenant information from landlord object
    # PASSING DATA AS "tenants" to HTML file
    return render_template("tenant_list.html", tenants=sorted(landlord.tenant_list, key=lambda x: x.apartment_number))

"""
--------------------------------- INPUT RENTAL PAYMENT PAGE ---------------------------------
"""
@app.route('/record_rental_payment', methods=['GET', 'POST'])
def record_rental_payment():
    if request.method == 'POST':
        # Get user input from webpage
        apartment_number = request.form['apartment_number']
        month = request.form['month']
        amount = float(request.form['amount'])

        # Add rental payment to income list
        landlord.rental_income_record.add_income(month, apartment_number, amount)

        # Send back to home page when finished
        return redirect(url_for('index'))
    return render_template('record_rental_payment.html')

"""
--------------------------------- RENTAL INCOME RECORD PAGE ---------------------------------
"""
@app.route('/rental_income_record')
def rental_income_record():
    # Display income record in a list
    # PASSING DATA AS "income_records" to HTML file
    return render_template('rental_income_record.html', income_records=landlord.rental_income_record.income_records)


"""
--------------------------------- INPUT EXPENSE PAGE ---------------------------------
"""
@app.route('/record_expense', methods=['GET', 'POST'])
def record_expense():
    if request.method == 'POST':
        # Get user input from webpage
        category = request.form['category']
        payee = request.form['payee']
        amount = float(request.form['amount'])
        date = request.form['date']

        # Add expense data to expense record
        landlord.expense_record.add_expense(date, payee, amount, category)

        # Send back to home page when finished
        return redirect(url_for('index'))
    return render_template('record_expense.html')


"""
--------------------------------- EXPENSE RECORD PAGE ---------------------------------
"""
@app.route('/expense_record')
def expense_record():
    # Display expense record in a list
    # PASSING DATA AS "expense_records" to HTML file
    return render_template('expense_record.html', expense_record=landlord.expense_record)

@app.route('/annual_report')
def annual_report():
    # Generate the annual report in the landlord object
    report = landlord.annual_report.generate_annual_report()

    # Display annual report data
    # PASSING DATA AS "annual_report" to HTML file
    return render_template('annual_report.html', annual_report=report)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
