import backtrader as bt
import yfinance as yf

# download stock data
data = yf.download(
    "AAPL",
    start="2019-01-01",
    end="2025-01-01"
)

data.columns = data.columns.droplevel(1)


class Strategy(bt.Strategy):

    def __init__(self):

        # moving averages
        self.sma1 = bt.indicators.SimpleMovingAverage(
            self.data.close,
            period=20
        )

        self.sma2 = bt.indicators.SimpleMovingAverage(
            self.data.close,
            period=50
        )

    def next(self):

        # buy condition
        if self.sma1[0] > self.sma2[0]:

            if not self.position:
                self.buy()

        # sell condition
        elif self.sma1[0] < self.sma2[0]:

            if self.position:
                self.sell()


feed = bt.feeds.PandasData(dataname=data)

cerebro = bt.Cerebro()

cerebro.addstrategy(Strategy)

cerebro.adddata(feed)

# starting amount
cerebro.broker.setcash(100000)

# drawdown analyzer
cerebro.addanalyzer(
    bt.analyzers.DrawDown,
    _name="drawdown"
)

print("Starting Value:",
      cerebro.broker.getvalue())

result = cerebro.run()

print("Final Value:",
      cerebro.broker.getvalue())

# return calculation
final_value = cerebro.broker.getvalue()

profit = (
    (final_value - 100000)
    / 100000
) * 100

print("Return:",
      round(profit, 2), "%")

# drawdown
strat = result[0]

drawdown = strat.analyzers.drawdown.get_analysis()

print(
    "Maximum Drawdown:",
    round(drawdown.max.drawdown, 2),
    "%"
)

cerebro.plot()