# side1 السطر التالي يطلب من المستخدم إدخال طول الضلع الأول ويخزنه في المتغير 
side1 = float(input("الرجاء إدخال طول الضلع الأول: "))

# side2 السطر التالي يطلب من المستخدم إدخال طول الضلع الثاني ويخزنه في المتغير 
side2 = float(input("الرجاء إدخال طول الضلع الثاني: "))

# side3 السطر التالي يطلب من المستخدم إدخال طول الضلع الثالث ويخزنه في المتغير 
side3 = float(input("الرجاء إدخال طول الضلع الثالث: "))

# السطر التالي يقوم بحساب محيط المثلث باجماع الأضلاع الثلاثة
perimeter = side1 + side2 + side3

# السطر التالي يطبع قيمة محيط المثلث
print("محيط المثلث هو:", perimeter)
