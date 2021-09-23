# Position Size Calculator
# Adaptation of Gogole Sheets file

# initial setup
account_equity = 10000 #currency
stock_symbol = 'DIS' #ticker
entry_price = 175.35 #currency
max_pos_size = 0.10 #percent
stop_loss_price = 165 #currency
risk_per_trade = 50 #currency
target_price = 210 #currency

# market data (need to implement API)
current_price = 176.05 # get from API
current_volume = 1469555 # get from API

# calculations
risk_per_trade_pct = risk_per_trade / account_equity
open_gain_loss = (current_price - entry_price) / entry_price
target_profit = (target_price - entry_price) / entry_price

print('POSITION SIZE CALCULATOR')
print(f'Account Equity     : ${account_equity:,.2f}')
print(f'Stock Symbol       : {stock_symbol}')
print(f'Entry Price        : ${entry_price:,.2f}')
print(f'Max. Position Size : {max_pos_size:,.2%}')
print(f'Current Price      : ${current_price:,.2f}')
print(f'Stop Loss Price    : ${stop_loss_price:,.2f}')
print(f'Risk per Trade ($) : ${risk_per_trade:,.2f}')
print(f'Volume             : {current_volume}')
print(f'Target Price ($)   : ${target_price:,.2f}')
print(f'Risk per Trade (%) : {risk_per_trade_pct:,.2%}')
print(f'Open Gain/Loss     : {open_gain_loss:,.2%}')
print(f'Target Profit (%)  : {target_profit:,.2%}')
print('--------------------------------------------------------')

# print(f'Value is: ${value:,.2f}'.replace('$-', '-$'))
# Position Size Using Stop Price
sp_stop_loss_pct = (entry_price - stop_loss_price) / entry_price
sp_risk_reward = target_profit / sp_stop_loss_pct
sp_position_size = risk_per_trade / (1 - (stop_loss_price / entry_price))
sp_position_size_pct = sp_position_size / account_equity
sp_risk_per_trade_pct = ( sp_position_size * sp_stop_loss_pct) / account_equity
sp_risk_per_trade = account_equity * sp_risk_per_trade_pct
sp_num_shares = int(sp_position_size / entry_price)

print("Position Size Using Stop Price:")
print(f'Stop Loss ($)     : ${stop_loss_price:,.2f}')
print(f'Stop Loss (%)     : {sp_stop_loss_pct:,.2%}')
print(f'Risk/Reward Ratio : 1:{sp_risk_reward:,.2f}')
print(f'Position Size ($) : ${sp_position_size:,.2f}')
print(f'Position Size (%) : {sp_position_size_pct:,.2%}')
print(f'Risk per Trade ($): ${sp_risk_per_trade:,.2f}')
print(f'Risk per Trade (%): {sp_risk_per_trade_pct:,.2%}')
print(f'Number of Shares  : {sp_num_shares}')