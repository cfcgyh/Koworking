from telegram import Update
from telegram.ext import ContextTypes
from config import price
import time
import database
from datetime import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    database.add_user(update.message.from_user.id, 0, 0.0)
    await update.message.reply_text(f'Hi! {update.effective_user.first_name} this is a coworking price counter bot. \n \nType /enter when you join coworking. \nOr /exit when you leaving it. \n \n Price is 10€ per hour.')
    

async def enter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    start = time.time()
    context.user_data['start'] = start
    await update.message.reply_text(f"{update.effective_user.first_name}, you enter the coworking space. The price of your stay here begins to be calculated now.")


async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        _, to_pay, time_inside = database.get_user_data(update.message.from_user.id)
        duration,time_string = colculate_time
        cost = calculate_cost(duration,price)
        # print(f'cost: {cost:.2f}, duration: {duration:.2f}')
#database
        database.add_user_data(update.message.from_user.id, cost + to_pay, duration + time_inside)
#exit
        await update.message.reply_text(f"You are leaving the coworking space.\nFor spending {time_string} sec there you have to pay {to_pay+cost:.2f}€")
    except KeyError:
        await update.message.reply_text("You cant exit coworking because you didnt entered it yet.")

def colculate_time(time_inside:time, context: ContextTypes.DEFAULT_TYPE):
        duration = time.time() - context.user_data['start'] 
        struct_time = datetime.fromtimestamp(duration + time_inside)
        time_string = struct_time.strftime("%M:%S")
        return duration,time_string

def calculate_cost(duration: float,
                   price: float,
                   ) -> float:     
    cost = duration * price

    return cost