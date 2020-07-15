import os
import config
from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
mongo = PyMongo(app=app,uri=config.DB_URI)  # 为哪个Flask app对象创建SQLAlchemy对象，赋值为db
#db = mongo.db
cx = mongo.cx
db = cx["zhihu"]
col = db["content"]
from views.zhihu import zhihu
from scrapy import cmdline
from flask_apscheduler import APScheduler
app.register_blueprint(zhihu,url_prefix="/zhihu")
from views.index import index
app.register_blueprint(index,url_prefix="/")
app.config.from_object(config.Config())
# @app.route('/')
# def hello_world():
#     context = col.find({},{"_id": 0,"content":1})
#     print(context)
#
#     contexts = []
#     for item in context:
#         print(item)
#         contexts.append(item["content"])
#     context = {"content":contexts}
#     print(context)
#     return render_template("test.html",content = context)

if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)
