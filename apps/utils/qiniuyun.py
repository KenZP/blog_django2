# _*_ coding"utf-8 _*_
from django.http import JsonResponse

__author__ = 'Ken'
__date__ = '2019/8/22 10:36'

from qiniu import Auth, put_file
import qiniu.config

access_key = "kCgin6W4Cl8WKq8QSW9HdDMD__lcCv6LergbJYps"
secret_key = "dyfxK3mSPrvPCEzt-h_cRfJK8OQqHN42QE-9KdFG"

bucket_name = 'blog'


# 定义获取七牛服务器上的tocken

# @login_required
# @require_http_methods(['GET'])
def get_token(request):
    # 1. 先要设置AccessKey和SecretKey
    access_key = "kCgin6W4Cl8WKq8QSW9HdDMD__lcCv6LergbJYps"
    secret_key = "dyfxK3mSPrvPCEzt-h_cRfJK8OQqHN42QE-9KdFG"
    # 2. 授权
    q = Auth(access_key, secret_key)
    # 3. 设置七牛空间(自己刚刚创建的)
    bucket_name = 'blog'
    # 4. 生成token
    token = q.upload_token(bucket_name)
    # 5. 返回token,key必须为uptoken
    return JsonResponse({'uptoken': token})

def qiniuyun_upload(key, localfile):
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, key, 3600)

    ret, info = put_file(token, key, localfile)



