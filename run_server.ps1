# 繝・・繧ｿ繝吶・繧ｹ繝槭う繧ｰ繝ｬ繝ｼ繧ｷ繝ｧ繝ｳ
python manage.py makemigrations
python manage.py migrate

# 繧ｹ繝ｼ繝代・繝ｦ繝ｼ繧ｶ繝ｼ菴懈・・亥ｯｾ隧ｱ蝙具ｼ・
Write-Host "邂｡逅・・Θ繝ｼ繧ｶ繝ｼ繧剃ｽ懈・縺励∪縺・.." -ForegroundColor Yellow
python manage.py createsuperuser

# 髢狗匱繧ｵ繝ｼ繝舌・襍ｷ蜍・
Write-Host "髢狗匱繧ｵ繝ｼ繝舌・繧定ｵｷ蜍輔＠縺ｾ縺・.." -ForegroundColor Green
Write-Host "繝悶Λ繧ｦ繧ｶ縺ｧ http://127.0.0.1:8000/ 縺ｫ繧｢繧ｯ繧ｻ繧ｹ縺励※縺上□縺輔＞" -ForegroundColor Cyan
python manage.py runserver
