uur = 0

while uur < 24:
    if uur < 12:
        tijd = "AM"
    else:
        tijd = "PM"

    if uur == 0:
        geformateerd_uur = 12
    elif uur <= 12:
        geformateerd_uur = uur
    else:
        geformateerd_uur = uur - 12

    if uur >= 16 and uur <= 20:
        dinner_time = "dinner time"
    else:
        dinner_time = ""
        
    
 



    print(f"{geformateerd_uur}:00 {tijd} {dinner_time }")
    uur += 1



# de_tijd = 1
# while de_tijd <= 12:
#     print(f"{de_tijd} AM")
#     de_tijd += 1

# de_tijd = 1
# while de_tijd <= 12:
#     print(f"{de_tijd} PM")
#     de_tijd += 1
