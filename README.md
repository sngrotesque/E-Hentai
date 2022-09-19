# E-Hentai - Web crawler❤

> 由SN-Grotesque开发并维护<br>
> v3.0版本更新了代码结构，重构了整个代码，并简化了用户操作。<br>
> 更新原因：本人实在看不下去以前写的狗屎代码了。

### 功能
> 程序简化成了傻瓜式操作<br>
> 只需要用户添加对应链接与目录名称即可

#### 特别说明：世界上任何事物都有滞后性，如果此程序后续无法使用了，请和我联络。
#### 联络方式在我的Github主页

```text
使用方法:
    ehentai(url, r18g = r18g, proxyinfo = ProxyInfo)
        url       为爬取的作品链接，数据类型为str，格式一般为'https://e-hentai.org/g/123456/123456abc'
        r18g      为作品类型，数据类型为布尔值，默认为False
        proxyinfo 为代理服务器，类型dict
    
    ehentai类
        getTotalPages       是用于获取作品总页数的
        getTotalArtworkList 是用于获取图片页面链接的
        download            是用来下载图片的，不完整获取链接后再一个个下载的原因请看"错误排除"
```

# 错误排除

```bash
如果在保存图片的过程中发生了错误，请查看对应图片的URL是否已刷新
因为E-Hentai的反爬机制为定时刷新所有图片的URL
```