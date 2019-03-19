#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

#!-*-coding=utf-8-*-

import pymysql

class CObject(object):

    def __init__(self):

        self.conn = pymysql.connect(host="localhost", user="root", password="root", db="mhcbg", port=3306)

        self.cur = self.conn.cursor()

    @staticmethod
    def query(sql):

        db = CObject()

        doWhat = str.upper(sql[0:6])

        if doWhat == "SELECT":#如果是查询数据

            db.cur.execute(sql)

            res = db.cur.fetchall()

            return res

        else:

            try:

                db.cur.execute(sql)

            except:

                db.conn.rollback()

                db.conn.close()

                db.cur.close()

                return False

            else:

                db.conn.commit()

                db.conn.close()

                db.cur.close()

                return True


