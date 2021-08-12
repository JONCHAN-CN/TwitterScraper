# Star Project
下载某个TW ACCT的所有图片

## notes
1. 在Star.py下，把账号放到target中即可运行。
2. chromedriver 是92， 其他版本自行下载替换。
3. 有两个CSS TEMP, 适用于20210812的网页CSS版本，网页改版后不可用的。
    - 默认使用缩略图的CSS TEMP
    - 大图的CSS TEMP流水未走通，但元素就是这个。#TODO
4. 有时会有元素过期错误，是因为卷太快了，目前先在DEBUG MODE下多运行几次scrapeInfo。#TODO
5. 首次运行后，可以导出cookies,下次直接导入就可以免登录。