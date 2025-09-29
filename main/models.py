from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name='莨夂､ｾ蜷・')
    address = models.TextField(verbose_name='菴乗園')
    phone = models.CharField(max_length=20, verbose_name='髮ｻ隧ｱ逡ｪ蜿ｷ')
    email = models.EmailField(verbose_name='繝｡繝ｼ繝ｫ繧｢繝峨Ξ繧ｹ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = '莨夂､ｾ諠・ｱ'
        verbose_name_plural = '莨夂､ｾ諠・ｱ'
    
    def __str__(self):
        return self.name

class Recruitment(models.Model):
    title = models.CharField(max_length=200, verbose_name='蜍滄寔繧ｿ繧､繝医Ν')
    description = models.TextField(verbose_name='蜍滄寔蜀・ｮｹ')
    requirements = models.TextField(verbose_name='蠢懷供雉・ｼ')
    is_active = models.BooleanField(default=True, verbose_name='蜈ｬ髢狗憾諷・')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = '謗｡逕ｨ諠・ｱ'
        verbose_name_plural = '謗｡逕ｨ諠・ｱ'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
