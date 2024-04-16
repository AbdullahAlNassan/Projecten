for uur in range(1,25):
    if uur <= 12:
        print(f'{uur} AM')
    else:
        uur = uur -12
        print(f'{uur} PM')