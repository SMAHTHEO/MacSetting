#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import glob


# 定义Java文件路径
java_file = "/path/to/your/file.java"


# 获取桌面文件夹路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")


total_java_lines = 0
total_py_lines = 0
total_ipynb_lines = 0

# 遍历文件夹下所有文件和子文件夹
for root, dirs, files in os.walk(desktop_path):
    for filename in glob.glob(os.path.join(root, "*.java")):
        if "test" in filename:
            continue
        with open(filename, "r") as f:
            # 读取当前Java文件的所有行
            lines = f.readlines()
            # 将当前Java文件的行数加到计数器中
            total_java_lines += len(lines)

# 遍历文件夹下所有文件和子文件夹
for root, dirs, files in os.walk(desktop_path):
    for filename in glob.glob(os.path.join(root, "*.py")):
        if "test" in filename:
            continue
        with open(filename, "r") as f:
            # 读取当前Java文件的所有行
            lines = f.readlines()
            # 将当前Java文件的行数加到计数器中
            total_py_lines += len(lines)

# 遍历文件夹下所有文件和子文件夹
for root, dirs, files in os.walk(desktop_path):
    for filename in glob.glob(os.path.join(root, "*.ipynb")):
        if "test" in filename:
            continue
        with open(filename, "r") as f:
            # 读取当前Java文件的所有行
            lines = f.readlines()
            # 将当前Java文件的行数加到计数器中
            total_ipynb_lines += len(lines)
            
            
# 显示区域
total = total_ipynb_lines+total_java_lines+total_py_lines
print("\n[XMeng] ---------- 书 写 小 程 序 ----------\n")
print("[XMeng] 共书写 java    文件 " + str(total_java_lines) + " 行！")
print("[XMeng] 共书写 python  文件 " + str(total_py_lines) + " 行！")
print("[XMeng] 共书写 ipython 文件 " + str(total_ipynb_lines) + " 行！")
print("\n[XMeng] ---------- 可 爱 分 割 线 ----------\n")
print("[XMeng] 共计 " + str(total) + " 行！")
print("\n[XMeng] ----------    E  N  D   ----------\n")






# In[ ]:




