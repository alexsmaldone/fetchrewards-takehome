from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class PayerTransaction(BaseModel):
  payer: str
  points: int
  timestamp: datetime = datetime.now()

class SpendPoints(BaseModel):
  points: int

class User():
  total_points = 0
  def __init__(self, total_points=0):
    self.total_points = total_points


user = User()
payer_points = {}
transactions = []


@app.get("/")
def get_payer_points():
    return payer_points

# DELETE THIS LATER
@app.get("/transactions")
def get_payer_points():
    return transactions



# need to create transaction and add to transactions list
# add to payer point balance if payer exists, otherwise create payer
@app.post("/payer_transactions")
def add_transaction(transaction: PayerTransaction):
  transactions.append(transaction)
  transactions.sort(key=lambda date: date.timestamp, reverse=True)

  if transaction.payer not in payer_points:
    payer_points[transaction.payer] = 0
  payer_points[transaction.payer] += transaction.points
  user.total_points += transaction.points

  return [payer_points, user.total_points]


# check if spend is greater than amount of total points for User, return error if >
# iterate backward over transactions, subtract points from payer in payerpoints
  # add payer and negative points taken to payer list
  # if total amount is greater than amount in transaction, then delete that transaction
  #
# return list of dicts with payer and points subtracted from payer
@app.post("/spend")
def spend_payer_points(spend: SpendPoints):
  if spend.points > user.total_points:
    raise HTTPException(status_code=422,
    detail=f'ERROR: Only {user.total_points} points available to spend')

  user.total_points -= spend.points

  for i in reversed(range(len(transactions))):
    pass

def validate_spend(spend, user_points):
  pass



  return {"points": user.total_points}
