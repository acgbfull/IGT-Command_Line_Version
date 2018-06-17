#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CreateFolderForResult类功能:
    创建存储程序运行结果的文件夹.
    用户有指定存储路径, 则创建指定文件夹.
    无指定, 则创建默认文件夹(位于本程序根目录下的project目录)
"""

import os
import logging


class CreateFolderForResult():
    def __init__(self, projectName, projectPathText):
        self.projectName = projectName
        self.projectPathText = projectPathText
        self.projectPath = ""
        self.logger = logging.getLogger("real_time_info")

    def start(self):
        self.mkDir()
        return self.projectPath

    def mkDir(self):
        if self.projectPathText is not "False":
            projectPath = self.projectPathText
        else:
            projectPath = os.path.abspath('.') + '\\project\\' + self.projectName      # os.path.abspath('.')#获得当前工作目录
        projectPath = projectPath.strip()                           # 去除字符串头尾空格
        projectPath = projectPath.rstrip("\\")                      # 去除尾部 \ 符号

        isExists = os.path.exists(projectPath)                      # 判断路径是否存在. 存在 True, 不存在 False

        # 判断结果
        if not isExists:
            # 目录不存在, 创建目录
            os.makedirs(projectPath)
            self.logger.info("-----------------------------------")
            self.logger.info(projectPath + u" 目录创建成功")
        else:
            # 目录存在, 不创建目录，提示目录已存在
            self.logger.info("-----------------------------------")
            self.logger.info(projectPath + u" 目录创建成功")
        self.projectPath = projectPath
