#!/usr/bin/python
# -*- coding:utf-8 -*-
#    Copyright(c) 2015-2016 JmGo Company
#    All rights reserved.
#
#    文件名 : yoke_template_method.py
#    作者   : YuanRong
#  电子邮箱 : ryuan@jmgo.com
#    日期   : 2017/5/3 16:52
#
#     描述  : 模板模式 —— 将公共部分抽离出来作为框架，具体的实现逻辑抽象成一个模板
#             交叉式的拼盘
#             例子 : 组合生成一个单据需要的元素——单据号、基础信息、展示商品信息
import datetime
import random


# 组合单据信息模板
class GroupInvoiceInfoTemplate:
    def __init__(self):
        pass

    @staticmethod
    def template_framework(skeleton, t_number, t_pro_info, t_base_info):
        return skeleton.get_invoice_info(i_number=t_number,
                                         i_pro_info=t_pro_info,
                                         i_base_info=t_base_info)


# 单据抽象类
class AbstractInvoice:
    def __init__(self):
        self.i_number = None

    def get_invoice_info(self, **kwargs):
        self.i_number = kwargs.get("i_number", None)

    def show_invoice(self):
        pass


# 生成销售单据模板
class CreateSaleInvoice(AbstractInvoice):
    def __init__(self):
        AbstractInvoice.__init__(self)
        self.sale_money = None  # 销售总额
        self.sale_pro_info = None  # 销售商品展示信息
        self.base_info = None  # 销售商品基础展示信息

    def get_invoice_info(self, **kwargs):
        self.i_number = kwargs.get("i_number", None)
        self.sale_pro_info = kwargs.get("i_pro_info", None)
        self.base_info = kwargs.get("i_base_info", None)
        return self

    def show_invoice(self):
        print self.i_number
        print self.sale_pro_info
        print self.base_info


# 生成入库单据模板
class CreateInWarehouseInvoice(AbstractInvoice):
    def __init__(self):
        AbstractInvoice.__init__(self)
        self.put_num = 0  # 入库总数
        self.put_pro_info = None  # 入库商品展示信息
        self.put_base_info = None  # 入库基础展示信息

    def get_invoice_info(self, **kwargs):
        self.i_number = kwargs.get("i_number", None)
        self.put_pro_info = kwargs.get("i_pro_info", None)
        self.put_base_info = kwargs.get("i_base_info", None)


# 生成出库单据模板
class CreateOutWarehouseInvoice(AbstractInvoice):
    def __init__(self):
        AbstractInvoice.__init__(self)
        self.out_num = 0  # 出库总数
        self.out_pro_info = None  # 出库商品展示信息
        self.out_base_info = None  # 出库基础展示信息

    def get_invoice_info(self, **kwargs):
        self.i_number = kwargs.get("i_number", None)
        self.out_pro_info = kwargs.get("i_pro_info", None)
        self.out_base_info = kwargs.get("i_base_info", None)


# 生成单据号抽象类
class CreateInvoiceNumber:
    def __init__(self):
        self.prefix = None

    def get_number(self, t_prefix=None):
        if t_prefix:
            self.prefix = t_prefix
        else:
            self.prefix = 'XX'

        # 因为这边根据前缀不一样，可能创建单据号的规则不一样，这边可以预留做判断
        # if self.prefix == 'sale':
        date_str = datetime.datetime.now().strftime("%Y%m%d")
        serial_number = str(random.randint(100, 1000))
        return self.prefix + date_str + serial_number

    def get_sale_number(self):
        pass


class InvoiceProductInfo:
    """
    单据商品信息类
    不同的单据需要展示的商品信息不一样，设置不一样，获取内容不一样
    """
    def __init__(self):
        self.p_name = None
        self.p_price = None
        self.p_sn = None
        self.p_code = None

    def get_sale_pro_info(self):
        pass

    def get_put_warehouse_pro_info(self):
        pass

    def get_out_warehouse_pro_info(self):
        pass


class InvoiceBaseInfo:
    """
    单据基础信息
    不同的单据所要填写的基础信息也不一样，设置不一样，获取内容不一样
    """
    def __init__(self):
        self.i_handler = None
        self.c_time = None

    def get_sale_base_info(self):
        pass

    def get_put_warehouse_base_info(self):
        pass

    def get_out_warehouse_base_info(self):
        pass


if __name__ == '__main__':
    sale_obj = CreateSaleInvoice()
    number_obj = CreateInvoiceNumber()
    pro_info_obj = InvoiceProductInfo()
    base_info_obj = InvoiceBaseInfo()

    template_obj = GroupInvoiceInfoTemplate()
    a = template_obj.template_framework(sale_obj,
                                        number_obj.get_number('sale'),
                                        pro_info_obj.get_sale_pro_info(),
                                        base_info_obj.get_sale_base_info())
    print a, type(a)
    a.show_invoice()
