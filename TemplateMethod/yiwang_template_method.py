#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-02 17:45:15
# @Author  : Yi Wang (gzytemail@126.com)
# @Link    : https://github.com/wang2222qq
# @des     : 模板方法


class AbstructInvoice(object):
    """ 
    单据模板 
    """
    def __init__(self):
        self.invoice_list = []

    def _check_input(self, **kwargs):
        """ 
        检测单据必填项
        """
        pass

    def _check_unique_item(self, **kwargs):
        """ 
        检测唯一项
        """
        pass

    def _create_invoice(self, **kwargs):
        """ 
        创建单据
        """
        pass

    def save(self, **kwargs):
        """ 
        保存单据步骤
        """
        self._check_input(**kwargs)
        self._check_unique_item(**kwargs)
        self._create_invoice(**kwargs)

    def show(self):
        """ 
        展示单据内容
        """
        for index, content in enumerate(self.invoice_list):
            print("第%d条单据信息内容:%s" % (index, content))


class SaleInvoice(AbstructInvoice):
    """ 
    销售单据
    """
    exist_number_list = []
    
    def _check_input(self, **kwargs):
        if not kwargs.get('name', None):
            raise ValueError(u"售后单据中客户姓名必填")
        if not kwargs.get('invoice_number', None):
            raise ValueError(u"售后单据中单据号必填")

    def _check_unique_item(self, **kwargs):
        invoice_number = kwargs.get('invoice_number', '')
        if invoice_number in self.exist_number_list:
            raise ValueError("invoice of sale repeat.")

    def _create_invoice(self, **kwargs):
        self.invoice_list.append({'name': kwargs.get('name', None),
                                  'invoice_number': kwargs.get('invoice_number', None)})
        self.exist_number_list.append(kwargs.get('invoice_number', None))


class InventoryInvoice(AbstructInvoice):
    """
    库存单据
    """
    def _check_input(self, **kwargs):
        if not kwargs.get('inventory', None):
            raise ValueError(u"库存单据中库存数量必填")
        if not kwargs.get('warehouse_name', None):
            raise ValueError(u"库存单据中仓库名称必填")

    def _create_invoice(self, **kwargs):
        self.invoice_list.append({'inventory': kwargs.get('inventory'),
                                  'warehouse_name': kwargs.get('warehouse_name')})


if __name__ == "__main__":
    paraments_1 = {'name': u'张三',
                   'invoice_number': u'Test0001'}
    s = SaleInvoice()
    # 插入一个销售单据
    s.save(**paraments_1)

    # 重复插入一个销售单据
    try:
        s.save(**paraments_1)
    except Exception as e:
        print e.message.encode()

    paraments_2 = {'inventory': 10,
                   'warehouse_name': u'测试仓'}
    i = InventoryInvoice()
    # 插入一条库存数据
    i.save(**paraments_2)

    # 展示单据内容
    s.show()
    i.show()

