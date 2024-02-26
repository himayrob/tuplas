name = input("deme su nombre completo")
edad = input("ingrese su edad")
altura = input("dame tu estatura")
informacion_personal = tuple((name, edad, altura))
print (informacion_personal)

pais = input("pais de origen")
departamento = input("departamento de origen")
ciudad = input("ciudad")
direccion = tuple((pais,departamento,ciudad))
print (direccion)

primaria = input("dime donde estudiaste") 
bachiller = input("donde estudiaste")
universidad = input("universidad")
cursos =tuple ((primaria, bachiller, universidad))
print (cursos)

primer_campo = input("muestarme algo de etu experiencia laboral")
segundo_campo = input("muestrame mas de tu experiencia laboral")
tercer_campo = input("sergiodame aun mas de tu experiencia experiencia_laboral")
experiencia_laboral = tuple((primer_campo, segundo_campo, tercer_campo))

print (experiencia_laboral)
