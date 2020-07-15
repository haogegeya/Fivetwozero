import json
from config import logging
from flask import Blueprint,render_template,request
zhihu = Blueprint("zhihu",__name__)
from utils.mongoUtil import MongoUtil


@zhihu.route("/index")
def index():
    ip = request.remote_addr
    logging.info(ip)
    return render_template("zhihu_search.html")


@zhihu.route("/detail")
def content():
    print(request.args)
    offset = request.args.get("offset",0)
    limit = request.args.get("limit",10)
    keys = request.args.get("keys")
    isBoy = request.args.get("isBoy")
    isGirl = request.args.get("isGirl")
    isPicture = request.args.get("isPicture")
    isQuality = request.args.get("isQuality")
    mongoutil = MongoUtil()
    count = mongoutil.getCount(keys=keys,isBoy=isBoy,isGirl=isGirl,isPicture=isPicture,isQuality=isQuality)
    print(count)
    if count%limit ==0:
        count = count//limit
    else:
        count = (count//limit+1)
    context = mongoutil.pageQuery(offset=offset,limit=limit,keys=keys,isBoy=isBoy,isGirl=isGirl,isPicture=isPicture,isQuality=isQuality)
    # contexts = []
    # for item in context:
    #     print(item)
    #     contexts.append(item["content"])
    #context = {"content":contexts}
    contents = list(context)
    print(contents)
    for i in contents:
        print(i)

    return render_template("zhihu_detail.html",content = contents,count=count,args=request.args)

@zhihu.route("/jumpPage")
def jumpPage():
    offset = request.args.get("offset",0)
    limit = request.args.get("limit",10)
    keys = request.args.get("keys")
    isBoy = request.args.get("isBoy")
    isGirl = request.args.get("isGirl")
    isPicture = request.args.get("isPicture")
    isQuality = request.args.get("isQuality")
    mongoutil = MongoUtil()
    count = mongoutil.getCount(keys=keys,isBoy=isBoy,isGirl=isGirl,isPicture=isPicture,isQuality=isQuality)
    print(count)
    context = mongoutil.pageQuery(offset=offset,limit=limit,keys=keys,isBoy=isBoy,isGirl=isGirl,isPicture=isPicture,isQuality=isQuality)
    # contexts = []
    # for item in context:
    #     print(item)
    #     contexts.append(item["content"])
    #context = {"content":contexts}
    contents = list(context)
    print(contents)
    for i in contents:
        print(i)

    return json.dumps(contents);