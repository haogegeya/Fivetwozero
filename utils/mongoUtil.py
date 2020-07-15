import pymongo
from app import col
class MongoUtil:
    def findAll(self):
        return col.find({},{"_id":0})


    def pageQuery(self,**kwargs):
        """
        分页查询
        :param page:
        :return:
        """
        print(kwargs)
        keys = kwargs.get("keys","")
        isBoy = kwargs.get("isBoy",1)
        isGirl = kwargs.get("isGirl",1)
        isPicture = kwargs.get("isPicture",0)
        isQuality = kwargs.get("isQuality",0)
        print(kwargs.get("offset"))
        offset = int(kwargs.get("offset",1))
        limit = int(kwargs.get("limit",20))
        sql = {}
        print(isBoy)
        if isBoy=="0":
            sql["gender"] = {"$ne":1}
        if isGirl == "0":
            sql["gender"] = {"$ne":0}
        if isPicture == "1":
            sql["isPicture"] = 1
        if isQuality == "1":
            sql["$or"] = [
                {"voteupCount":{"$gte":10}},
                {"commentCount": {"$gte": 10}}
            ]
        if keys:
            sql["$and"] = []
            for item in keys.split(" "):
                sql["$and"].append({"content":{"$regex":item.strip()}})
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(sql)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        return  col.find(sql,{"_id":0}).skip(offset*limit).limit(limit)

    def getCount(self,**kwargs):
        """
        获取数量
        :param kwargs:
        :return:
        """
        keys = kwargs.get("keys", "")
        isBoy = kwargs.get("isBoy", 1)
        isGirl = kwargs.get("isGirl", 1)
        isPicture = kwargs.get("isPicture", 0)
        isQuality = kwargs.get("isQuality", 0)
        sql = {}
        if isBoy == "0":
            sql["gender"] = {"$ne": 1}
        if isGirl == "0":
            sql["gender"] = {"$ne": 0}
        if isPicture == "1":
            sql["isPicture"] = 1
        if isQuality == "1":
            sql["$or"] = [
                {"voteupCount": {"$gte": 10}},
                {"commentCount": {"$gte": 10}}
            ]
        if keys:
            sql["$and"] = []
            for item in keys.split(" "):
                sql["$and"].append({"content": {"$regex": item.strip()}})
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(sql)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        return col.find(sql).count()
