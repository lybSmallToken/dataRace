## JData算法大赛
### 符号定义：
##### S：提供的商品全集；
##### P：候选的商品子集（JData_Product.csv），P是S的子集；
##### U：用户集合；
##### A：用户对S的行为数据集合；
##### C：S的评价数据。

#### 训练数据部分：
&emsp;&emsp;提供2016-02-01到2016-04-15日用户集合U中的用户，对商品集合S中部分商品的行为、评价、用户数据；提供部分候选商品的数据P。
选手从数据中自行组成特征和数据格式，自由组合训练测试数据比例。

#### 预测数据部分：
&emsp;&emsp;2016-04-16到2016-04-20用户是否下单P中的商品，每个用户只会下单一个商品；抽取部分下单用户数据，A榜使用50%的测试数据来计算分数；B榜使用另外50%的数据计算分数(计算准确率时剔除用户提交结果中user_Id与A榜的交集部分)。

#### 任务描述：
&emsp;&emsp;参赛者需要使用京东多个品类下商品的历史销售数据，构建算法模型，预测用户在未来5天内，对某个目标品类下商品的购买意向。对于训练集中出现的每一个用户，参赛者的模型需要预测该用户在未来5天内是否购买目标品类下的商品以及所购买商品的SKU_ID。评测算法将针对参赛者提交的预测结果，计算加权得分。

#### 评分规则
&emsp;&emsp;参赛者需要使用京东多个品类下商品的历史销售数据，构建算法模型，预测用户在未来5天内，对某个目标品类下商品的购买意向。对于训练集中出现的每一个用户，参赛者的模型需要预测该用户在未来5天内是否购买目标品类下的商品以及所购买商品的SKU_ID。评测算法将针对参赛者提交的预测结果，计算加权得分。
参赛者提交的结果文件中包含对所有用户购买意向的预测结果。对每一个用户的预测结果包括两方面：

1、该用户2016-04-16到2016-04-20是否下单P中的商品，提交的结果文件中仅包含预测为下单的用户，预测为未下单的用户，无须在结果中出现。若预测正确，则评测算法中置label=1，不正确label=0；</br>
2、如果下单，下单的sku_id （只需提交一个sku_id），若sku_id预测正确，则评测算法中置pred=1，不正确pred=0。</br>
对于参赛者提交的结果文件，按如下公式计算得分：
###### Score=0.4*F11 + 0.6*F12
此处的F1值定义为：
#### F11=6\*Recall\*Precise/(5\*Recall+Precise)</br>
##### F12=5\*Recall\*Precise/(2\*Recall+3\*Precise)</br>
其中，Precise为准确率，Recall为召回率.F11是label=1或0的F1值，F12是pred=1或0的F1值.

#### 1.用户数据
|user_id|用户ID|脱敏|
|:------|:-------|:----|
|age|年龄段|-1表示未知|
|sex|性别| 0表示男，1表示女，2表示保密|
| user_lv_cd	|用户等级	 |有顺序的级别枚举，越高级别数字越大|
|user_reg_tm	|用户注册日期	 |粒度到天|

#### 2.商品数据
 |sku_id|	 商品编号	| 脱敏|
 |:------|:--------|:-------|
 |a1	| 属性1	| 枚举，-1表示未知|
 |a2	| 属性2	| 枚举，-1表示未知|
 |a3	| 属性3	| 枚举，-1表示未知|
 |cate	| 品类ID	| 脱敏|
 |brand	| 品牌ID	| 脱敏|

 #### 3.评价数据
 |dt	| 截止到时间	| 粒度到天|
 |:----|:---------|:-------|
 |sku_id	| 商品编号	| 脱敏|
 |comment_num	| 累计评论数分段	| 0表示无评论，1表示有1条评论，2,3,4递增|
 |has_bad_comment	|是否有差评	| 0表示无，1表示有|
 |bad_comment_rate	| 差评率	| 差评数占总评论数的比重|

 #### 4.行为数据
 |user_id	| 用户编号	| 脱敏|
 |:----|:---------|:-------|
 |sku_id	| 商品编号	| 脱敏|
 |time	| 行为时间	| |
 |model_id	| 点击模块编号，如果是点击	| 脱敏|
 |type|1.浏览（指浏览商品详情页）；2.加入购物车；3.购物车删除；4.下单；5.关注；6.点击||
 |cate	|品类ID	| 脱敏|
 |brand	| 品牌ID	| 脱敏|
