import futuquant as ft
import talib as tb
import pandas as pd
import time
from BarCTM import (BarGenerator,ArrayManager)
from Vtc import (VtBaseData,VtBarData)
from datetime import datetime,timedelta
from queue import Queue, Empty




class FutuGateway(VtGateway):
    """富途接口"""

    #----------------------------------------------------------------------
    def __init__(self, eventEngine, gatewayName='FUTU'):
        """Constructor"""
        super(FutuGateway, self).__init__(eventEngine, gatewayName)
        
        self.quoteCtx = None
        self.tradeCtx = None
        
        self.host = '127.0.0.1'
        self.ip = 11111
        self.market = ''
        self.password = ''
        self.env = ft.TrdEnv.SIMULATE        # 默认仿真交易
        
        #self.fileName = self.gatewayName + '_connect.json'
        #self.filePath = getJsonPath(self.fileName, __file__)
        
        self.tickDict = {}
        #self.tradeSet = set()      # 保存成交编号的集合，防止重复推送
        
        # self.qryEnabled = True
        # self.qryThread = Thread(target=self.qryData)

    def connectQuote(self):
        """连接行情功能"""
        self.quoteCtx = ft.OpenQuoteContext(self.host, self.port)
        
        # 继承实现处理器类
        class QuoteHandler(StockQuoteHandlerBase):
            """报价处理器"""
            gateway = self  # 缓存Gateway对象
            
            def on_recv_rsp(self, rsp_str):
                ret_code, content = super(QuoteHandler, self).on_recv_rsp(rsp_str)
                if ret_code != RET_OK:
                    return RET_ERROR, content
                self.gateway.processQuote(content)
                return RET_OK, content     
               

        self.quoteCtx.set_handler(QuoteHandler())
        #订单报价处理类
        self.quoteCtx.start()
         # 启动行情
    def processQuote(self, data):
    """报价推送"""
        for ix, row in data.iterrows():
            symbol = row['code']

            tick = self.tickDict.get(symbol, None)
            if not tick:
                tick = VtTickData()
                tick.symbol = symbol
                tick.vtSymbol = tick.symbol
                tick.gatewayName = self.gatewayName
                self.tickDict[symbol] = tick
                
            tick.date = row['data_date'].replace('-', '')
            tick.time = row['data_time']
            tick.datetime = datetime.strptime(' '.join([tick.date, tick.time]), '%Y%m%d %H:%M:%S')
            tick.openPrice = row['open_price']
            tick.highPrice = row['high_price']
            tick.lowPrice = row['low_price']
            tick.preClosePrice = row['prev_close_price']
            
            tick.lastPrice = row['last_price']
            tick.volume = row['volume']
            
            if 'price_spread' in row:
                spread = row['price_spread']
                tick.upperLimit = tick.lastPrice + spread * 10
                tick.lowerLimit = tick.lastPrice - spread * 10
            
            newTick = copy(tick)
            self.onTick(newTick)

    def onTick(self, tick):
        """市场行情推送"""
        # 通用事件
        event1 = Event(type_=EVENT_TICK)
        event1.dict_['data'] = tick
        self.eventEngine.put(event1)

class Event:
    """事件对象"""

    #----------------------------------------------------------------------
    def __init__(self, type_=None):
        """Constructor"""
        self.type_ = type_      # 事件类型
        self.dict_ = {}         # 字典用于保存具体的事件数据
    






code = 'HK_FUTURE.999010'
#股指当月期货

