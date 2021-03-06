
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, redirect

from stock_model import Stock

app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True

@app.route(r'/marquesitas', methods=['GET'])
def contact_book():
    contacts = Contact.query().fetch()
    return render_template('contact_book.html', contacts=contacts)

@app.route(r'/paco', methods=['GET'])
def stock_list():
    stocks = Stock.query().fetch()
    return render_template('stock_update.html', stocks=stocks)


# return render_template('contact_book.html')
    #return 'PP Marquesitas, tradición familiar desde 1853'

@app.route(r'/marquesitas/agregar', methods=['GET','POST'])
def add_contact():
    if request.form:
         contact = Contact(name=request.form.get('name'),precio=request.form.get('precio'))
         contact.put()
         flash('¡Se añadió la marquesita!')


@app.route(r'/paco/agregar', methods=['GET','POST'])
def add_stock():
    if request.form:
    #    stock = Stock(name=request.form.get('name'),quantity=float(request.form.get('quantity')), price=float(request.form.get('price')), amount=float(request.form.get('amount')),
    #                  commission=float(request.form.get('commission')), tax=float(request.form.get('tax')), total_amount=float(request.form.get('total_amount')),
    #                  operacion=request.form.get('operacion'), poi=float(request.form.get('poi')), actual_price=float(request.form.get('actual_price')),
    #                  profit=float(request.form.get('profit')), price_sold=float(request.form.get('price_sold')), sold_amount=float(request.form.get('sold_amount')), profit_money=float(request.form.get('profit_money')))
        stock = Stock(name=request.form.get('name'),quantity=validate_request(request.form.get('quantity')), price=validate_request(request.form.get('price')), amount=validate_request(request.form.get('amount')),
                      commission=validate_request(request.form.get('commission')), tax=validate_request(request.form.get('tax')), total_amount=validate_request(request.form.get('total_amount')),
                      operacion=request.form.get('operacion'), poi=validate_request(request.form.get('poi')), actual_price=validate_request(request.form.get('actual_price')),
                      profit=validate_request(request.form.get('profit')), price_sold=validate_request(request.form.get('price_sold')), sold_amount=validate_request(request.form.get('sold_amount')), profit_money=validate_request(request.form.get('profit_money')))
    #contact = Contact(name=request.form.get('name'),precio=request.form.get('precio'))
        stock.put()
        flash('¡Se añadió la acción!')
    return render_template('paco.html')

def validate_request(value):
    if value.isdigit():
        return float(value)
    else:
        return float(0)
#  print(request.form.get('name'))
      #  print(request.form.get('phone'))
      #  print(request.form.get('email'))

@app.route(r'/contacts/<uid>',methods=['GET'])
def contact_details(uid):
    contact = Contact.get_by_id(int(uid))

    if not contact:
        return redirect('/marquesitas', code=301)

    return render_template('contact.html', contact=contact)

@app.route(r'/delete', methods=['POST'])
def delete_contact():
    contact = Contact.get_by_id(int(request.form.get('uid')))
    contact.key.delete()

