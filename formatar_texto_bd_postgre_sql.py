# -*- coding: utf-8 -*-

def encontrar_entre_aspas(string):
    novo_texto = ''
    contador = 0
    for x in range(len(string)):
        letra = string[x]
        if string[x+1:x+7] == "var = ":
            sigla = string[x+7:x+13]
        if ord(letra) == 34:
            contador += 1
            if contador % 2 != 0:
                if string[x+1:x+7] == "public":
                    novo_texto += '"'
                else:
                    novo_texto += letra + sigla 
            else:
                novo_texto += letra
        else:
            if contador % 2 != 0:
                parte_1 = transformar_maiusculas(letra)
                parte_2 = tirar_acentos_dos_es(parte_1)
                parte_3 = tirar_acentos_dos_as(parte_2)
                parte_4 = tirar_acentos_dos_is(parte_3)
                parte_5 = tirar_acentos_dos_os(parte_4)
                parte_6 = tirar_acentos_dos_us(parte_5)
                parte_7 = tirar_cedilhas(parte_6)
                parte_8 = tirar_espacos_e_hifens(parte_7)
                novo_texto += parte_8
            else:
                novo_texto += letra
    return novo_texto


def transformar_maiusculas(letra):
    nova_letra = ''
    if 65 <= ord(letra) <= 90:
        nova_letra = chr(ord(letra) + 32)
    else:
        nova_letra = letra
    return nova_letra


def tirar_acentos_dos_es(letra):
    nova_letra = ''
    if letra in 'éèêëÉÈÊË':
        nova_letra = 'e'
    else:
        nova_letra = letra
    return nova_letra


def tirar_acentos_dos_as(letra):
    nova_letra = ''
    if letra in 'ÀàáÁäÄãÃâÂ':
        nova_letra = 'a'
    else:
        nova_letra = letra
    return nova_letra


def tirar_acentos_dos_is(letra):
    nova_letra = ''
    if letra in 'ÍíìÌïÏîÎ':
        nova_letra = 'i'
    else:
        nova_letra = letra
    return nova_letra


def tirar_acentos_dos_os(letra):
    nova_letra = ''
    if letra in 'óÓÒòöÖõÕ':
        nova_letra = 'o'
    else:
        nova_letra = letra
    return nova_letra


def tirar_acentos_dos_us(letra):
    nova_letra = ''
    if letra in 'ùÙÚúüÜûÛ':
        nova_letra = 'u'
    else:
        nova_letra = letra
    return nova_letra


def tirar_cedilhas(letra):
    nova_letra = ''
    if letra in 'çÇ':
        nova_letra = 'c'
    else:
        nova_letra = letra
    return nova_letra


def tirar_espacos_e_hifens(letra):
    nova_letra = ''
    if letra in ' -':
        nova_letra = '_'
    else:
        nova_letra = letra
    return nova_letra
                 
#texto = 'TABLE "ÀàáÁäÄãÃâÂ ùÙÚúüÜûÛ SÈCO-NDÁ óÓÒ-òöÖõÕ çÇÍíìÌïÏîÎ éèêëÉÈÊË" çÇùÙ   Úú- -üÜ ûÛ ó - Ó-ÒòöÖõÕÍíìÌïÏîÎÀàáÁäÄãÃâÂéèêëÉÈÊË'

texto = """

"""

text = encontrar_entre_aspas(texto)
print(text)