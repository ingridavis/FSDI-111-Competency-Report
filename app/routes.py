#!/usr/bin/env python3
# -*-coding utf8 -*-

"""Routes file"""

from app import app  # importing app variable
from flask import g, request, render_template, redirect, url_for, session, flash#g is global 
from app.forms.name import ProductForm
from app.forms.user import NameForm
from app.forms.admin import AdminForm
from app.userDB import get_db, get_all_users, create_user

#global var


# functions
def get_all_products(): #GET/SCAN/
    cursor = get_db().execute("SELECT * FROM product", ()) 
    results = cursor.fetchall() # returning all the data, PUT, POST
    cursor.close()
    return results

"""

def get_user(): #GET/READ
    cursor = get_db().execute("SELECT * FROM user where last_name=", ()) 
    if user is None:
        print ('No such user exists')
    results = cursor.fetchall() # returning all the data, PUT, POST
    cursor.close()
    return results
"""

def create_product(product):
    sql = """INSERT INTO product (
                    id, 
                    product_title,
                    brand_name, 
                    product_descrip, 
                    product_price, 
                    ship_price, 
                    sku
                    )
            VALUES (?, ?, ?, ?, ?, ?)""" # ? are placeholders, applies to creating data
    cursor = get_db()
    cursor.execute(sql, product) 
    # takes user and match up to the columns
    cursor.commit()
    return cursor.lastrowid      
        

def delete_product(product): 
    
    sql = """DELETE from product where id=?"""
    cursor = get_db()
    cursor.execute(sql, product)
    cursor.commit()# commit = save it in the database
    cursor.close()
    # return cursor.lastrowid           # We could do this, but we won't for now because our app doesn't need it.
    return True        


# connecting to html page
@app.route("/catalog")
def scan_products():
    product = get_all_products()
    return render_template("catalog.html", products=product)


# Closing when app is shut down
@app.teardown_appcontext 
def close_connection(exception): 
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

# index page
# @ = decorator that tells flask that when / route is requested, function is called
@app.route('/')
def index():  # function
    return "Hello world"

# Products on Catalog route 
@app.route('/login', methods=["GET", "POST"])
def login():
    
    if "POST" in request.method:
        #request.form = AdminForm()
        password = request.form.get("password")
        if password == "111":
            flash("Successful login")
            return redirect (url_for("get_products"))
        else:
            flash("Invalid Admin Password")
            return redirect (url_for("login"))
    return render_template("login.html")

@app.route('/admin/product', methods=["GET", "POST"]) #SESSION 3 complete at end of class
def get_products():
    # creating an output dictionary 
    out= {"ok": True, "body": ""} # standard formart for our restful API
    body_list = [] # temp list to hold the records we are creating
    if "GET" in request.method:
        form = ProductForm()
        raw_data= get_all_products() # getting all users from database, returned to raw data as tuples
        for item in raw_data: # for each item in list of tuples
            temp_dict = {
                "id": item[0],
                "product_title": item[1],
                "brand_name": item[2],
                "product_descrip": item[3],
                "product_price": item[4],
                "ship_price": item[5],
                "sku": item[6]
            }
            body_list.append(temp_dict) # body list will have all tuples
        out["body"] = body_list # putting body list in body field
        return render_template(
            "admin.html",
            id = out["body"][0].get("id"),
            product_title = out["body"][0].get("product_title"),
            brand_name = out["body"][0].get("brand_name"),
            product_descrip = out["body"][0].get("product_descrip"),
            product_price = out["body"][0].get("product_price"),
            ship_price = out["body"][0].get("ship_price"),
            sku = out["body"][0].get("sku"),
            form=form
        )
    if "POST" in request.method:
        id = request.form.get("id")
        product_title = request.form.get("product_title")
        brand_name = request.form.get("brand_name")
        product_descrip = request.form.get("product_descrip")
        product_price = request.form.get("product_price")
        ship_price = request.form.get("ship_price")
        sku = request.form.get("sku")

        create_product((id, product_title, brand_name, product_descrip, product_price, ship_price, sku))
        return redirect(url_for("get_products"))


@app.route('/product/delete', methods=["POST"])
def product_delete():
    if "POST" in request.method: 
        id = request.form.get("id")
        product_title = request.form.get("product_title")
        brand_name = request.form.get("brand_name")
        product_descrip = request.form.get("product_descrip")
        product_price = request.form.get("product_price")
        ship_price = request.form.get("ship_price")
        sku = request.form.get("sku")

        # if sumbit(delete) button is clicked, delete user
        delete_product((id, product_title, brand_name, product_descrip, product_price, ship_price, sku))   
        return redirect(url_for("scan_products")) 


    

@app.route('/users', methods=["GET", "POST"])
def get_users():
    # Creating an output dictionary
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        # get_all_users() returns all records from the user table
        form = NameForm()
        raw_data = get_all_users()
        for item in raw_data:
            temp_dict = {
                "id": item[0],
                "first_name": item[1],
                "last_name": item[2],
                "address": item[3],
                "billing_card": item[4], 
                "phone_number":item[5],
            }
            body_list.append(temp_dict)
        if not body_list:
            body_list.append({})            # This is done so that when we reference the 0th index on lines 47-50 the code doesn't break
        out["body"] = body_list
        return render_template(
            "user_signin.html",
            first_name=out["body"][0].get("first_name"),    
            last_name=out["body"][0].get("last_name"),      
            address=out["body"][0].get("address"),
            billing_card=out["body"][0].get("billing_card"),
            phone_number=out["body"][0].get("phone_number"),
            form=form)
    if "POST" in request.method:
        flash("Created new user!")
        return redirect(url_for("get_users"))
      

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p> your user agent is %s</p>" % user_agent

@app.errorhandler(404)
def page_not_found(exception):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(exception):
    return render_template("500.html"), 500

