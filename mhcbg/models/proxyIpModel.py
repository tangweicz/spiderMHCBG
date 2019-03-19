#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

# !-*-coding=utf-8-*-

from mhcbg.models.model import model


class proxyIpModel(model):
    table = "crawlerIp"

    """

        按ID排序获取到前200条数据

    """

    @staticmethod
    def getTwoHundredIp():
        sql = "select * from " + proxyIpModel.table + " order by id asc limit 0,200"

        res = model.query(proxyIpModel, sql=sql)

        return res

    def deleteOne(self):
        sql = "delete from " + proxyIpModel.table + " where id = " + str(self.id)

        res = model.query(self, sql=sql)

        return res

    def insertOne(self):

        sql = "insert into "+proxyIpModel.table + " (`ipAddr`) values ('"+self.ipAddr+"')"

        res = model.query(self, sql=sql)

        return res


if __name__ == "__main__":
    res = proxyIpModel.getTwoHundredIp()

    r = res[0]

    r.deleteOne()