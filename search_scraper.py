import json
import httpx
from parsel import Selector

session = httpx.Client(
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    },
    http2=True,
    follow_redirects=True
)

def scrape_search(response: httpx.Response) -> list:
    sel = Selector(response.text)
    css_join = lambda css: "".join(sel.css(css).getall()).strip()  # join all selected elements
    css = lambda css: sel.css(css).get("").strip() 

    searchList = []
    #id = css(s-item s-item__pl-on-bottom
    #url = sel.css("a[data-interactions]::attr(href)").get()
    # searchList.extend(sel.xpath("//div[contains(@class, 's-item_link')]/a/@href").getall()) # not working
    # searchList.extend(sel.css('.a.s-item__link').getall()) # not working

    # doing this so i dont have to use a for loop
    urls = list(map(lambda url: url.split("?")[0], sel.css("li.s-item a.s-item__link::attr(href)").getall()))

    #urls = sel.css("li.s-item a.s-item__link::attr(href)").getall().split("?")[0]

    print(urls)
    print(searchList)

response = session.get("https://www.ebay.com/sch/i.html?&_nkw=shoe")
scrape_search(response)

response = session.get("https://www.ebay.com/sch/i.html?&_nkw=hat")
scrape_search(response)
# <li data-viewport="{&quot;trackableId&quot;:&quot;01JGJP3RTP1V63AM97NQRY1XQ7&quot;}" id="item2b8152e926" class="s-item s-item__pl-on-bottom" data-view="mi:1686|iid:1" data-gr4="2" data-gr3="2" data-gr2="2"><div class="s-item__wrapper clearfix"><!--F#f_0--><div class="s-item__image-section"><div class="s-item__image"><a data-interactions="[{&quot;actionKind&quot;:&quot;NAVSRC&quot;,&quot;interaction&quot;:&quot;wwFVrK2vRE0lhQQ0MDFKR0pQM1JXTkRFQTZaSjZYV1pZWUJTRkQ0MDFKR0pQM1JUUDFWNjNBTTk3TlFSWTFYUTcAAAg3NDAwDE5BVlNSQwA=&quot;}]" tabindex="-1" target="_blank" data-carousel-tabindex="-1" aria-hidden="true" _sp="p2351460.m1686.l7400" data-s-6poq273="{&quot;eventFamily&quot;:&quot;LST&quot;,&quot;eventAction&quot;:&quot;ACTN&quot;,&quot;actionKind&quot;:&quot;NAVSRC&quot;,&quot;actionKinds&quot;:[&quot;NAVSRC&quot;],&quot;operationId&quot;:&quot;2351460&quot;,&quot;flushImmediately&quot;:false,&quot;eventProperty&quot;:{&quot;$l&quot;:&quot;1097817214838463&quot;}}" href="https://www.ebay.com/itm/186853288230?_skw=shoe&amp;itmmeta=01JGJP3RTP1V63AM97NQRY1XQ7&amp;hash=item2b8152e926:g:u3UAAOSwRzBnZ0go&amp;itmprp=enc%3AAQAJAAAAwHoV3kP08IDx%2BKZ9MfhVJKkmb1rbrlx22a94rqgb2wWbD2iuTPDlvPxFv3gTjRcyB5UM7mGwuOU9pzCEjx%2FvpyPNHx6EaiwGj8oWxsocgoeaMVs1hl7ncylrkw3qPYvHNS1JolMknXA3dRWEqTI2YlayA4oXPqPSuc%2BlHukpLxsigZ9SMdUuYZ6I0L9DPNzjT6GM1Oy0CI8ka11XIgXxTLopyS8Q%2Bj55f0jHzJcklYCkMWtcLwnD%2BNe0lpmY0Pjvnw%3D%3D%7Ctkp%3ABlBMUMKNj9aEZQ"><div class="s-item__image-wrapper image-treatment"><img src="https://i.ebayimg.com/images/g/u3UAAOSwRzBnZ0go/s-l500.jpg" loading="eager" fetchpriority="high" onerror="window.SRP.metrics.incrementCounter('imageLoadError');" style=" ;width:500px;;width:auto" alt="Boot-Fix Glue: Professional Grade Shoe Repair Glue for Boots, Shoes, and More" data-atftimer="1735793960764" data-defertimer="206"></div></a></div><span class="s-item__watchheart on-image s-item__watchheart--watch"><a aria-label="watch Boot-Fix Glue: Professional Grade Shoe Repair Glue for Boots, Shoes, and More" _sp="" data-s-6poq273="{&quot;eventFamily&quot;:&quot;LST&quot;,&quot;eventAction&quot;:&quot;ACTN&quot;,&quot;actionKind&quot;:&quot;NAVSRC&quot;,&quot;actionKinds&quot;:[&quot;NAVSRC&quot;],&quot;operationId&quot;:&quot;2351460&quot;,&quot;flushImmediately&quot;:false,&quot;eventProperty&quot;:{&quot;trackableId&quot;:&quot;01JGJP3RTP1V63AM97NQRY1XQ7&quot;,&quot;clickaction&quot;:&quot;WATCH&quot;,&quot;itm&quot;:&quot;186853288230&quot;,&quot;amdata&quot;:&quot;amclksrc=A2W&quot;,&quot;adctrl&quot;:&quot;AD_CTRL_ATW_ADD&quot;,&quot;enc&quot;:&quot;AQAJAAAAwHoV3kP08IDx+KZ9MfhVJKkmb1rbrlx22a94rqgb2wWbD2iuTPDlvPxFv3gTjRcyB5UM7mGwuOU9pzCEjx/vpyPNHx6EaiwGj8oWxsocgoeaMVs1hl7ncylrkw3qPYvHNS1JolMknXA3dRWEqTI2YlayA4oXPqPSuc+lHukpLxsigZ9SMdUuYZ6I0L9DPNzjT6GM1Oy0CI8ka11XIgXxTLopyS8Q+j55f0jHzJcklYCkMWtcLwnD+Ne0lpmY0Pjvnw==&quot;,&quot;moduledtl&quot;:&quot;p2351460.m4114.l8480&quot;,&quot;sid&quot;:&quot;p2351460.m4114.l8480&quot;}}" class="s-item__watchheart-click" href="https://www.ebay.com/myb/WatchListAdd?item=186853288230&amp;pt=null&amp;srt=01000a0000005011684253477200d351b6e906a83baa23c8048bb458334356c0161f2919003ccdafd44270afd6cefa4f4b1ba517c310c10663eaf5cdd7cf0994e4dcaa6cac6a9e87fdb146abcd4b5705cee97ebc2332db&amp;ru=https%3A%2F%2Fwww.ebay.com%2Fsch%2Fi.html%3F_nkw%3Dshoe"><span class="s-item__watchheart-icon"><svg data-marko-key="@svg s0-61-0-13-8-4-3-0-3-0-3[1]-10-1-15-6-1-7-1-0" class="icon icon--24" focusable="false" aria-hidden="true"><use href="#icon-save-24"></use></svg><svg data-marko-key="@svg s0-61-0-13-8-4-3-0-3-0-3[1]-10-1-15-6-1-7-2-0" class="icon icon--24" focusable="false" aria-hidden="true"><use href="#icon-save-filled-24"></use></svg></span></a></span></div><div class="s-item__info clearfix"><!--F#f_21--><div class="s-item__caption"></div><!--F#f_11--><a data-interactions="[{&quot;actionKind&quot;:&quot;NAVSRC&quot;,&quot;interaction&quot;:&quot;wwFVrK2vRE0lhQQ0MDFKR0pQM1JXTkRFQTZaSjZYV1pZWUJTRkQ0MDFKR0pQM1JUUDFWNjNBTTk3TlFSWTFYUTcAAAg3NDAwDE5BVlNSQwA=&quot;}]" target="_blank" _sp="p2351460.m1686.l7400" data-s-6poq273="{&quot;eventFamily&quot;:&quot;LST&quot;,&quot;eventAction&quot;:&quot;ACTN&quot;,&quot;actionKind&quot;:&quot;NAVSRC&quot;,&quot;actionKinds&quot;:[&quot;NAVSRC&quot;],&quot;operationId&quot;:&quot;2351460&quot;,&quot;flushImmediately&quot;:false,&quot;eventProperty&quot;:{&quot;$l&quot;:&quot;1097817214838463&quot;}}" class="s-item__link" href="https://www.ebay.com/itm/186853288230?_skw=shoe&amp;itmmeta=01JGJP3RTP1V63AM97NQRY1XQ7&amp;hash=item2b8152e926:g:u3UAAOSwRzBnZ0go&amp;itmprp=enc%3AAQAJAAAAwHoV3kP08IDx%2BKZ9MfhVJKkmb1rbrlx22a94rqgb2wWbD2iuTPDlvPxFv3gTjRcyB5UM7mGwuOU9pzCEjx%2FvpyPNHx6EaiwGj8oWxsocgoeaMVs1hl7ncylrkw3qPYvHNS1JolMknXA3dRWEqTI2YlayA4oXPqPSuc%2BlHukpLxsigZ9SMdUuYZ6I0L9DPNzjT6GM1Oy0CI8ka11XIgXxTLopyS8Q%2Bj55f0jHzJcklYCkMWtcLwnD%2BNe0lpmY0Pjvnw%3D%3D%7Ctkp%3ABlBMUMKNj9aEZQ"><div class="s-item__title"><span role="heading" aria-level="3"><!--F#f_0-->Boot-Fix Glue: Professional Grade Shoe Repair Glue for Boots, Shoes, and More<!--F/--></span></div><span class="clipped">Opens in a new window or tab</span></a><!--F/--><div class="s-item__subtitle"><!--F#f_0--><span class="SECONDARY_INFO">Brand New</span><!--F/--></div><!--F/--><div class="s-item__details clearfix"><div class="s-item__details-section--primary"><div class="s-item__detail s-item__detail--primary"><span class="s-item__price"><!--F#f_0--><!--F#f_0-->$9.99<!--F/--><!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><span class="s-item__dynamic s-item__formatBuyItNow"><!--F#f_0-->Buy It Now<!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><span class="s-item__shipping s-item__logisticsCost"><!--F#f_0-->+$21.71 shipping<!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><span class="s-item__location s-item__itemLocation"><!--F#f_0-->from United States<!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><div class="s-item__sme-container"><span class="s-item__sme s-item__smeInfo"><!--F#f_0--><span class="NEGATIVE BOLD">Save up to 30% when you buy more</span><!--F/--></span></div></div><div class="s-item__detail s-item__detail--primary"><span><span aria-labelledby="s-ibf3334" data-w="espdonrSo" class="s-ibf3334_s-0tkg918" role="text"><div aria-hidden="true">Sponsored</div></span></span><span class="s-item__space_bar"></span></div></div><div class="s-item__details-section--center"></div><div class="s-item__details-section--secondary"></div></div></div><!--F/--></div></li>