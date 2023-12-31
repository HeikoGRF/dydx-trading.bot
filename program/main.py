from func_connections import connect_dydx
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_private import abort_all_positions
from func_public import construct_market_prices

if __name__ == "__main__":

  # Connect to client
  try:
    print("Connecting to Client...")
    client = connect_dydx()
  except Exception as e:
    print("Error connecting to client: ", e)
    exit(1)

  # Abort all open positions
  if ABORT_ALL_POSITIONS:
    try:
      print("Closing all positions...")
      close_orders = abort_all_positions(client)
    except Exception as e:
      print("Error closing all positions: ", e)
      exit(1)
      
  # Finding Cointegrated Pairs
  if FIND_COINTEGRATED:
    
    # Coonstruct Market Prices
    try:
      print("Fetching market prices, please await 3 mins...")
      df_market_prices = construct_market_prices(client)
    except Exception as e:
      print("Error construct market prices: ", e)
      exit(1) 
      