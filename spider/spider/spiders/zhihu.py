# -*- coding: utf-8 -*-
import re
import json
import scrapy
from spider.globalValue import QUESTION
from spider.items import ContentItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/question/275359100']
    def __init__(self):
        self.baseAnswerUrl = "https://www.zhihu.com/api/v4/questions/{}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset={}&limit=20&sort_by=updated"

    def parse(self, response):
        html = response.text
        pattern = re.compile('www.zhihu.com\\\\u002Fquestion\\\\u002F(\d*).*?的你')
        questionIdList  = list(set(re.findall(pattern,html)))
        questionIdList.append("275359100")
        for itemQuestionId in questionIdList:
            answerUrl = self.baseAnswerUrl.format(itemQuestionId,0)
            yield scrapy.Request(
                answerUrl,
                callback=self.getDataFromJson,
                meta = {"itemQuestionId":itemQuestionId,'offset': 0}
            )

    def getDataFromJson(self,response):
        data = json.loads(response.text)
        data = data.get("data",[])
        if data:
            itemQuestionId = response.meta["itemQuestionId"]
            if itemQuestionId not in QUESTION:
                print(len(set(QUESTION)))
                print(set(QUESTION))
                print(itemQuestionId)
                offset = response.meta["offset"]
                offset += 20
                answerUrl = self.baseAnswerUrl.format(itemQuestionId,offset)
                yield scrapy.Request(
                    answerUrl,
                    callback=self.getDataFromJson,
                    meta={"itemQuestionId":itemQuestionId,'offset': offset}
                )

        contentItem = ContentItem()
        for item in data:
            contentItem["questionId"] = item["question"]["id"]
            contentItem["city"] = item["question"]["title"].split("的")[0].split("在")[-1].strip()
            contentItem["answerId"] = item["id"]
            contentItem["author"] = item["author"]["name"]
            contentItem["headUrl"] = item["author"]["avatar_url"]
            contentItem["authorId"] = item["author"]["url_token"]
            contentItem["gender"] = item["author"]["gender"]
            contentItem["voteupCount"] = item["voteup_count"]
            contentItem["commentCount"] = item["comment_count"]
            contentItem["createTime"] = item["created_time"]
            contentItem["updateTime"] = item["updated_time"]
            content = item["content"]
            content = ("").join(content.split("\n"))
            pattern = re.compile(r'<noscript>[\s\S]*?src=\"([\s\S]*?)"')
            result1 = re.findall(pattern, content)
            if result1:
                result2 = re.sub(r'<figure[\s\S]*?</figure>', "{}", content)
                imgList = []
                for item in result1:
                    str = "<img src='{}'>".format(item)
                    imgList.append(str)
                result2 = result2.format(*imgList)
                contentItem["content"] = result2
                contentItem["isPicture"] = 1
            else:
                contentItem["content"] = content
                contentItem["isPicture"] = 0
            yield contentItem



