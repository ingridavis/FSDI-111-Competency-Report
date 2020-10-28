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


def get_all_reviews():
    cursor = get_db().execute("SELECT * FROM review", ())
    results = cursor.fetchall()
    cursor.close()
    return results


def create_review():
    sql = """INSERT INTO review (
                    id,
                    review,
                    author
                    )
            VALUES (?, ?)"""  
    cursor = get_db()
    cursor.execute(sql)
    # takes user and match up to the columns
    cursor.commit()
    return True                  