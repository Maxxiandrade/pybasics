ingreso_mensual = 10000
gasto_mensual= 6000

#if anidados y else if (elif)

if(ingreso_mensual)>=10000:
    if(ingreso_mensual - gasto_mensual )<0:
        print('Estas en deficit')
    elif (ingreso_mensual - gasto_mensual)>3000:
        print('Estas bien')
    else:
        print('Estas gastando mucho')
elif ingreso_mensual > 1000:
    print('Estas bien en latinoamerica')
elif ingreso_mensual > 500:
    print('Estas bien en Argentina')
else:
    print('Sos pobre')
    
