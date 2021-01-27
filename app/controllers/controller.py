from flask import render_template
from app import app
from app.models.order_list import orders

@app.route("/orders")
def home_page():
    return render_template('index.html', title="Cheese Shop", orders=orders)

@app.route("/orders/<index>")
def order_page(index):
    return render_template('order.html', index=index, title="Orders", order=orders[int(index)])
    

