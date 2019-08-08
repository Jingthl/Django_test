from django.db import models
from django.contrib.auth.models import AbstractUser


class Staff(AbstractUser):
    staff_id = models.CharField(max_length=32, verbose_name='工号')
    department = models.CharField(max_length=16, verbose_name='部门')
    position = models.CharField(max_length=16, verbose_name='职位')
    username = models.CharField(max_length=32, unique=True, verbose_name='姓名')
    # password = models.CharField(max_length=32, verbose_name='密码', default='')  # Gyq123!@#
    telephone = models.CharField(max_length=16, verbose_name='电话')

    # USERNAME_FIELD = 'telephone'  # 登录时用工号登录
    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工系统'

    def __str__(self):
        return self.username


class Client(models.Model):
    cid = models.CharField(max_length=32, primary_key=True, verbose_name='客户编码')
    client_name = models.CharField(max_length=128, verbose_name='客户名称')
    user_name = models.CharField(max_length=128, verbose_name='使用客户')
    standard_address = models.CharField(max_length=256, verbose_name='标准地址')
    client_address = models.CharField(max_length=256, verbose_name='客户地址')

    def __str__(self):
        return self.cid

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = '客户系统'


class Product(models.Model):
    # 状态0，1，2，3，4分别对应状态正常、拆机、单停、双停、停机保号
    STATUS_NORMAL = 0
    STATUS_DELETE = 1
    STATUS_ONE_WAY_STOP = 2
    STATUS_STOP = 3
    STATUS_STORE_NUMBER = 4
    STATUS_OTHER = 5
    # 状态选项
    item = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '拆机'),
        (STATUS_ONE_WAY_STOP, '单停'),
        (STATUS_STOP, '双停'),
        (STATUS_STORE_NUMBER, '停机保号'),
        (STATUS_OTHER, '其他'),
    )
    sid = models.CharField(max_length=32, primary_key=True, verbose_name='专线号')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=item,
                                         blank=True, verbose_name='状态')
    MKT_CHNL_NAME = models.CharField(max_length=128)
    MKT_GRID_NAME = models.CharField(max_length=128)
    receive_org = models.CharField(max_length=128, verbose_name='揽收组织')
    PRODUCT_NAME = models.CharField(max_length=128)
    main_set = models.CharField(max_length=256, verbose_name='主套餐')
    add_set = models.CharField(max_length=256, verbose_name='加装包')
    CRM = models.CharField(max_length=32)
    product_quality = models.CharField(max_length=64, verbose_name='产品性质')
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    staff = models.ForeignKey(to=Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.sid

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品系统'


class Contract(models.Model):
    contract_amount = models.FloatField(verbose_name='合同金额')
    contract_id = models.CharField(max_length=32, verbose_name='合同编码')
    contract_date = models.DateField(verbose_name='合同签订时间')
    contract_expire = models.DateField(verbose_name='合同到期时间')
    allowance = models.FloatField(verbose_name='交叉补贴')
    product = models.OneToOneField(to=Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.contract_id

    class Meta:
        verbose_name = '合同'
        verbose_name_plural = '合同系统'


class Resource(models.Model):
    bandwidth = models.IntegerField(verbose_name='套餐带宽')
    true_bandwidth = models.IntegerField(verbose_name='实际带宽')
    net_management = models.CharField(max_length=16, verbose_name='集团网管监控')
    product = models.OneToOneField(to=Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.sid

    class Meta:
        verbose_name = '资源'
        verbose_name_plural = '资源系统'
