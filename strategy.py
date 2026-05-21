import backtrader as bt
import yfinance as yf

class MyStrategy(bt.Strategy):

    def __init__(self):

        self.sma20 = bt.indicators.SimpleMovingAverage(
            self.data.close,
            period=20
        )

        self.sma50 = bt.indicators.SimpleMovingAverage(
            self.data.close,
            period=50
        )

        self.crossover = bt.indicators.CrossOver(
            self.sma20,
            self.sma50
        )

    def next(self):

        if not self.position:

            if self.crossover > 0:
                self.buy()

        else:

            if self.crossover < 0:
                self.sell()


data = yf.download(
    "AAPL",
    start="2019-01-01",
    end="2025-01-01"
)

data.columns = data.columns.droplevel(1)

feed = bt.feeds.PandasData(
    dataname=data
)

cerebro = bt.Cerebro()

cerebro.addstrategy(MyStrategy)

cerebro.adddata(feed)

cerebro.broker.setcash(100000)

print("Starting Portfolio Value:",
      cerebro.broker.getvalue())

cerebro.addanalyzer(
    bt.analyzers.DrawDown,
    _name="drawdown"
)

results = cerebro.run()

print("Final Portfolio Value:",
      cerebro.broker.getvalue())

strat = results[0]

drawdown = strat.analyzers.drawdown.get_analysis()

print(
    "Maximum Drawdown:",
    round(drawdown.max.drawdown, 2),
    "%"
)

cerebro.plot()