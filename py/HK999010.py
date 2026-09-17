import futuquant as ft
import time


def hk_warrant(quote_ctx,code,warrant):
    #计算窝轮价格

    #获得正股市场快照
    ret, data= quote_ctx.get_market_snapshot(code)
    #拿到牛能证价格
    ret_b, boll = quote_ctx.get_market_snapshot(warrant)
    if ret== 0 and ret_b== 0:
        #拿到当前正股价格
        price = data.loc[0,"last_price"]
        #正股最小变动价格
        price_spread_stock = data.loc[0,"price_spread"]

    #-------------------------------------------------------    
        #拿到换股比例
        wrt_ratio = boll.loc[0,"wrt_conversion_ratio"]
        #窝轮价格
        price_b = boll.loc[0,"last_price"]
        #拿到行使价
        wrt_strike_price=boll.loc[0,"wrt_strike_price"]
        #溢价
        wrt_premium = boll.loc[0,"wrt_premium"]
        #窝轮最小变动价格
        price_spread_b= boll.loc[0,"price_spread"]
        #窝轮类型

    #----------------------------------------------------------------
        #正股每跳动多少点窝轮变价
        change_minprice = wrt_ratio *price_spread_b
        #计算还有归零多少距离
        distence = price - wrt_strike_price
        #正股还有多少格
        huw_tiao = distence//price_spread_stock
        #窝轮正常价
        wlzc_price = distence/wrt_ratio
       
        print(f"现在窝轮应该是{wlzc_price},溢价是{wrt_premium}现在价格是{price_b}")
        print(f"换股比较是{wrt_ratio}\n所以正股每变动{change_minprice}窝轮变动{price_spread_b}元")
        print("距离行使价还有{:.2f}元".format(distence))
        time.sleep(10)
    else:
        print("出错了",ret,data)
        time.sleep(20)

    
def compute_wrt(quote_ctx,wl_price,code):
    #分析窝轮跳价

    #获得正股市场快照
    ret, data= quote_ctx.get_market_snapshot(code)
    #拿到牛能证价格
    ret_b, boll = quote_ctx.get_market_snapshot(warrant)
    if ret== 0 and ret_b== 0:
        #拿到当前正股价格
        price = data.loc[0,"last_price"]
      #-------------------------------------------------------    
        #拿到换股比例
        wrt_ratio = boll.loc[0,"wrt_conversion_ratio"]
        #窝轮价格
        price_b = boll.loc[0,"last_price"]
        #拿到行使价
        wrt_strike_price=boll.loc[0,"wrt_strike_price"]
        #溢价
        wrt_premium = boll.loc[0,"wrt_premium"]
        #是牛还是熊
        wrt_type = boll.loc[0,"wrt_type"]

    #-----------------------------------------------------
    #计算牛证人价格
    #得到牛熊证类型字段进行判断
    if wrt_type == ft.WrtType.BULL:
        #牛窝轮价格=(溢价/100*正股当前价)+行使价-正股当前价/换股比例
        wrt_bull_price = ((wrt_premium/100*wl_price) + wrt_strike_price - wl_price)/wrt_ratio
        print("当价格达到{}时,溢价{}牛证应该是{:.3f}".format(wl_price, wrt_premium, abs(wrt_bull_price)))

    if wrt_type == ft.WrtType.BEAR:
        #熊窝轮价格=(溢价/100*正股当前价)-行使价+正股当前价/换股比例    
        wrt_bear_price = ((wrt_premium/100*wl_price) - wrt_strike_price + wl_price)/wrt_ratio
        print("当价格达到{}时,溢价{}熊正对应的价格应该是{:.3f}".format(wl_price, wrt_premium ,abs(wrt_bear_price)))
   



#实例化API对象
quote_ctx = ft.OpenQuoteContext(host='127.0.0.1', port=11111)    

code = 'HK_FUTURE.999010' #期货
warrant = "HK.61376" #窝轮代码
wl_price = 27808 #正股当前价格
#计算窝轮价格
compute_wrt(quote_ctx,wl_price,warrant)

#分析窝轮跳价
hk_warrant(quote_ctx,code,warrant)
    

quote_ctx.close()