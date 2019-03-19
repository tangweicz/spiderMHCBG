#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

#!-*-coding=utf-8-*-

from mhcbg.libs.CObject import CObject

class model():

    def query(self, sql):

        doWhat = str.upper(sql[0:6])

        if doWhat == "SELECT":  # 如果是查询数据

            result = CObject.query(sql)

            res = []

            for values in result:

                tmpres = self()

                tmpres.id = values[0]

                tmpres.ipAddr = values[1]

                res.append(tmpres)

            return res
        else:

            return CObject.query(sql)