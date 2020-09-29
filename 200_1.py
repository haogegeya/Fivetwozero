# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 20:41
# @Author  : lagelanren
# @Email   : forhaogege@163.com
# @File    : 200.py
# @Software: PyCharm

import re, os, time
# 正则匹配待替换得代码
re_str = "TCP_ERROR[\S\s]*?TCP_BIN_ERR[\S\s]*?\);"
# 正则匹配参数
re_str_params = "\(([\S\s]*)?\);"
# 匹配注释
re_str_notes = "/\*[\S\s]*?\*/"
# 替换代码模板
new_code_template_one = 'TcpErrLog({}, {}, {}, {}, {}, {});'
new_code_template_two = 'TcpErrLog({}, {}, {}, {}, "");'

def work(base_dir):
    # result_dir = os.path.join(base_dir, "result")
    # print(base_dir)
    for item_file in os.listdir(base_dir):
        # 遍历文件夹目录，如果是还是文件夹，递归
        if os.path.isdir(os.path.join(base_dir, item_file)):
            work(os.path.join(base_dir, item_file))
        elif item_file.endswith("c"):
            # if not os.path.exists(result_dir):
            #     os.mkdir(result_dir)
            with open(os.path.join(base_dir, item_file), "r") as file:
                code = file.read()
                code_new = code
                waiter_code = re.findall(re_str, code)
                for item in waiter_code:
                    part_excess = []
                    item = item.replace("%d,", "%@")
                    item = item.replace("%u,", "%#")
                    item_shadow = re.sub(re_str_notes, "", item)
                    if ("%s" in item_shadow):
                        continue
                    if(len(re.findall('TCP_', item_shadow)) > 2):
                        part_excess = item_shadow.split(";")[0:-3]
                        part_one, part_two = item_shadow.split(";")[-3:-1]
                    else:
                        part_one, part_two, _ = item_shadow.split(";")
                    part_one = part_one.strip() + ";"
                    part_two = part_two.strip() + ";"
                    part_one_params = re.findall(re_str_params, part_one)[0].split(",")
                    part_two_params = re.findall(re_str_params, part_two)[0].split(",")
                    part_one_params = [item_params.strip() for item_params in part_one_params]
                    part_two_params = [item_params.strip() for item_params in part_two_params]
                    # print("+++++++++++++++++++++++++++++++")
                    # print(part_one_params)
                    # print(part_two_params)
                    # print(len(part_one_params[4:]))
                    # print("++++++++++++++++++++++++++++++++")
                    if (len(part_one_params[4:]) <= 4):
                        if ("%" in part_one_params[3]):
                            item_new_code = new_code_template_one.format(part_two_params[0], part_two_params[2],
                                                                         part_one_params[2], part_one_params[3],
                                                                         '"' + "%"+"%".join(part_one_params[3].split("%")[1:]).strip(),
                                                                         ", ".join(part_one_params[4:]))
                        else:
                            # print(part_two_params)
                            item_new_code = new_code_template_two.format(part_two_params[0], part_two_params[2],
                                                                         part_one_params[2], part_one_params[3])
                        item = item.replace("%@", "%d,")
                        item_new_code = item_new_code.replace("%@", "%d,")
                        item = item.replace("%#", "%u,")
                        item_new_code = item_new_code.replace("%#", "%u,")
                        if part_excess:
                            part_excess = ";".join(part_excess) + ";"
                            item_new_code = part_excess + item_new_code
                        print(item_new_code)
                        code_new = code_new.replace(item, item_new_code)
                    else:
                        print(part_one_params)
                        print(part_two_params)

                with open(os.path.join(base_dir, item_file), "w", encoding="GB2312") as file:
                    file.write(code_new)
                print(item_file + "--------处理完成")

if __name__ == '__main__':
    base_dir = input("输入文件夹")
    work(base_dir)






