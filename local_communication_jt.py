from uagents import Agent, Context,Model,Bureau
import random

class Message(Model):
    message: str
    value: int
  
dante = Agent(name="dante", seed="nel mezzo del cammin di nostra vita")
virgilio = Agent(name="virgilio", seed="Tempus fugit")
 
@virgilio.on_event("startup")
async def hello(ctx: Context):
    ctx.logger.info(f"Hello, I'm agent and latin poet {virgilio.name} and my address is {virgilio.address}.")
    print("Fetch network address: ", virgilio.wallet.address())

@dante.on_event("startup")
async def hello(ctx: Context):
    ctx.logger.info(f"Hello, I'm agent and italian poet {dante.name} and my address is {dante.address}.")
    print("Fetch network address: ", dante.wallet.address())
    print(dante.address)

@virgilio.on_interval(period=3.0)
async def message_sender(ctx: Context):
   await ctx.send(dante.address, Message(message="Hello my friend! I'm Virgilio and We're at hell circle number:",value=random.randint(1,9)))

@dante.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message} {msg.value}")

bureau = Bureau()
bureau.add(dante)
bureau.add(virgilio)
 
if __name__ == "__main__":
    bureau.run()
