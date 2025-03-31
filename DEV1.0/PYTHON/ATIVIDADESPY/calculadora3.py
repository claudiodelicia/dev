raio = float(input("qual e o raio"))

area = f"{(3.141516 * raio *raio):_.2f}"
area = area.replace("." , ",")
area = area.replace("_" , ".")


print(f"a area da circunferencia de raio {raio} e :{area}")
