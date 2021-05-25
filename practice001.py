from django.forms import models


class BuriedPointLog(models.Model):
    """用户访问埋点记录"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(CourseOrder, on_delete=models.SET_NULL, null=True)
    ident = models.ForeignKey('BuriedPointIdent', on_delete=models.SET_NULL, null=True)
    flag = models.CharField('公众号标识', max_length=32, default='')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    course_group = models.ForeignKey(CourseGroup, on_delete=models.SET_NULL, null=True)
    banner_id = models.IntegerField('banner_id', default=0)
    grand_id = models.IntegerField('祖宗id', default=0)
    parent_id = models.IntegerField('父级id', default=0)


class BuriedPointIdent(models.Model):
    """埋点标识"""
    name_info = (
        ('mall_home', '商城首页'),
        ('mall_earn', '商城赚钱'),
        ('mall_learn', '商城学习'),
        ('mall_mine', '商城我的'),
        ('mall_mine_rank', '商城我的同学'),
        ('mall_mine_withdrawal', '商城我的前往提现'),
        ('mall_mine_reward', '商城我的收益明细'),
        ('mall_home_banner', '商城轮播图'),
        ('mall_home_shelf', '商场货架'),
        ('card_list', '大课预约'),
        ('classroom', '手机上课端'),
        ('formal_landing_live', '活数据单课'),
        ('course_cart', '购物车'),
        ('ppt_introduction', 'PPT单课落地页'),
        ('excel_plan', 'Excel单课'),
        ('excel_landing_live', 'Excel活数据小课'),
        ('excel_landing', 'Excel小课'),
        ('word_introduction', 'word单课'),
        ('analysis_introduction', '数据分析精进单课'),
        ('excel_compose_introduction', 'excel+数据分析精进组合'),
        ('red_packet_home', '红包首页'),
        ('red_packet_list', '红包列表页'),
        ('red_packet_record', '红包记录页'),
        ('red_packet_send', '红包发送页'),
    )
    name = models.CharField('名称', max_length=32, default='')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True)