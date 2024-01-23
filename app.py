from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/submit', methods=['POST'])
def submit():
    details_fields = ["OrderID", "Amount", "Profit", "Quantity", "Category", "SubCategory", "PaymentMode"]
    orders_fields = ["OrderID", "OrderDate", "CustomerName", "State", "City"]

    details_data = [request.form[field] for field in details_fields]
    orders_data = [request.form[field] for field in orders_fields]

    with open('C:/Users/swami/Downloads/Details.csv', mode='a', newline='') as details_file:
        details_writer = csv.writer(details_file)
        details_writer.writerow(details_data)

    # with open('Details.csv', mode='a', newline='') as details_file:
    #     details_writer = csv.writer(details_file)
    #     details_writer.writerow(details_data)

    with open('C:/Users/swami/Downloads/Orders.csv', mode='a', newline='') as orders_file:
        orders_writer = csv.writer(orders_file)
        orders_writer.writerow(orders_data)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
