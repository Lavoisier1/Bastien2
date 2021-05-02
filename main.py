from discord.ext import commands
import random

def sum_list(l):
    sum = 0
    for x in l:
        sum += x
    return sum

bot = commands.Bot(command_prefix="%")


@commands.command()
async def combat(ctx, arg, arg2):

    encounter = (random.randint(1, 100))
    await ctx.send(f"rouler100 = {encounter} vs le % de chance {arg}")
    bareme = float(arg)
    if encounter <= bareme :
      await ctx.send(f"Il y a une rencontre sur la route")
      modif= float(arg2)
      await ctx.send(f"Modificateur est de : {modif}")
      de= abs(modif)+1
      await ctx.send(f"Nombres de d20 = {de}")

      if modif <= -1:
            await ctx.send(f"Désavantage")
            n = de
            n = abs(int( n ))
            diceList = []
            for row in range(0, n):
                diceList.append(random.randint(1, 20))
            cr=min(diceList)
            await ctx.send(f"Le CR total de encounter est de {cr}, {diceList}")
            
      else:
            await ctx.send(f"Avantage")
            n = de
            n = abs(int( n ))
            diceList = []
            for row in range(0, n):
                diceList.append(random.randint(1, 20))
            cr=max(diceList)
            await ctx.send(f"Le CR total de encounter est de {cr}, {diceList}")

      if n == 1:
               individus = random.randint(1, 4)
               Crindividus = round(cr/individus)
      elif n==2:
                individus = random.randint(1, 6)
                Crindividus = round(cr/individus)
      elif n==3:
                individus = random.randint(1, 8)
                Crindividus = round(cr/individus)
      elif n==4:
                individus = random.randint(1, 10)
                Crindividus = round(cr/individus)
      elif n==5:
                individus = random.randint(1, 12)
                Crindividus = round(cr/individus)
      else:
                individus = random.randint(1, 20)
                Crindividus = round(cr/individus)
      await ctx.send(f"Nb.individus={individus}")
      await ctx.send(f"Cr par individu = {Crindividus}")
      outcome = random.randint(1, 20)
      await ctx.send(f"Outcome (1d20) ={outcome}")
      if outcome >= cr:
          if (outcome - cr) >= 5:
            await ctx.send("Rencontre positive")
            
          else:
              await ctx.send("Rencontre Neutre")
      else:
          await ctx.send("Rencontre Negative")
      await ctx.send(f"LOOT - LOOT - LOOT")
      
      listeloot= []

      for x in range(individus):
        loot_individu = round(Crindividus * random.randint(1,20)) * Crindividus
        listeloot.append(loot_individu)
    
      await ctx.send(f"Chaque individu a {loot_individu} gp pour un total de XXX gp")
      await ctx.send(f"ITEM MAGIQUE - LOOT - ITEM MAGIQUE")
      
    else:
      await ctx.send("Chemin tranquille")
    
bot.add_command(combat)

bot.run('ODMzODY0OTEwNjQ3MzI4Nzk4.YH4jNw.tvFL-3AELwg7WJdUJ_9E8qiiJWE')