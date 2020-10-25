#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Our flask routes"""

from flask import g
import sqlite3


DATABASE = "online_store"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def get_all_users():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return results


def create_user(user):
    sql = """INSERT INTO user (
                    id,
                    first_name,
                    last_name,
                    address,
                    billing_card,
                    phone_number)
            VALUES (?, ?, ?, ?)"""
    cursor = get_db()
    cursor.execute(sql, user)
    cursor.commit()
    return cursor.lastrowid           
    #return True                         