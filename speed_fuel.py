speed=0
fuel=50
limit=60
while fuel>0 :
   if speed <limit:
       speed+=10
   fuel-=5
   print("speed:",speed)
   print("fuel :",fuel)
   