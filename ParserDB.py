#!/usr/bin/python2.7
# -*- coding: utf-8

from BeautifulSoup import BeautifulSoup
import psycopg2
import pdb


def parse_acta(f_handle):
  """
  Dentro de una tabla de align center esta la información de ubigeo

  Dentro de la tabla de clase "borde_tabla" estan los resultados.
  De los tr heigh="40" en el span dentro del td align left esta el nombre de la organización
  Del 2do td align=center dentro del span de class arial_contenido esta el número
  """
 
  soup = BeautifulSoup( f_handle )
  a = soup.findAll('tr',height="40")
  d_data = {}

  Organ = [u'GANA PERU',u'DESPERTAR NACIONAL', u'FUERZA 2011', u'PERU POSIBLE', u'ALIANZA SOLIDARIDAD NACIONAL', u'ALIANZA POR EL GRAN CAMBIO', u'ADELANTE', u'JUSTICIA, TECNOLOGIA, ECOLOGIA', u'FONAVISTAS DEL PERU', u'FUERZA NACIONAL', u'PARTIDO DESCENTRALISTA FUERZA SOCIAL', u'Votos Blancos', u'Votos Nulos', u'Votos Impugnados']

  T_Flag = False
  for item in soup.findAll('tr'):
    for item2 in BeautifulSoup(str(item)).findAll('span',{'class':'arial_contenido_negrita'}):
      if T_Flag == True:
        if item2.contents == []:
          votacion = 0
        else:
          votacion = int(item2.contents[0])
        d_data[curr_Organ] = int(votacion)
        T_Flag = False
      if not(item2.contents == []):
        if item2.contents[0] in Organ:
          T_Flag = True 
          curr_Organ = item2.contents[0]

    for item2 in BeautifulSoup(str(item)).findAll('span',{'class':'arial_contenido'}):
      if T_Flag == True:
        if item2.contents == []:
          votacion = 0
        else:
          votacion = int(item2.contents[0])
        d_data[curr_Organ] = int(votacion)
        T_Flag = False
      if not(item2.contents == []):
        if item2.contents[0] in Organ:
          T_Flag = True 
          curr_Organ = item2.contents[0]


  Categorias = [ u'Departamento:', u'Provincia:', u'Distrito:', u'Local de Votaci&oacute;n: ', u'Direcci&oacute;n: ', u'Electores H&aacute;biles: ', u'Total de Ciudadanos que Votaron: ']  #, u'Estado del acta: ', u'Historial del acta: ']

  Printable_Categorias = []

  T_Flag = False
  try:
    tmp_soup = BeautifulSoup( str( soup.findAll('table',{'align':'center', 'border':'0'})[0] ) )
  except IndexError:
    print soup.findAll('table',{'align':'center', 'border':'0'})

  for item in tmp_soup.findAll('td',{'class':'arial_contenido'}):
    if not(item.contents[0] == u'&nbsp;'):
      if T_Flag == True:
        d_data[curr_Categoria] = item.contents[0]
        T_Flag = False
      if item.contents[0] in Categorias:
        T_Flag = True
        curr_Categoria = item.contents[0]


  for item in tmp_soup.findAll('td',{'class':'arial_contenido_negrita'}):
    if not(item.contents[0] == u'&nbsp;'):
      pass

  for item in tmp_soup.findAll('td',{'class':'arial_titulo'}):
    if not(item.contents[0] == u'&nbsp;'):
      pass
      #print item.contents
  #b = BeautifulSoup.BeautifulSoup(str(a))
  #c = BeautifulSoup.BeautifulSoup( str( b.find('td',align="left" ) ) )

  #print b.find('td',align="left")
  #pdb.set_trace()
  #print soup.prettify()

  """
  d_data[u'Total de Ciudadanos que Votaron: '] = int( d_data[u'Total de Ciudadanos que Votaron: ']  )
  d_data[u'Electores Habiles'] = int(d_data[u'Electores H&aacute;biles: '])
  del d_data[u'Electores H&aacute;biles: ']
  d_data[u'Local de Votacion'] = d_data[u'Local de Votaci&oacute;n: '] 
  del d_data[u'Local de Votaci&oacute;n: ']
  """
  return d_data

def insert_data_SVP( num_acta, d_data,cursor):
  """
  Falta revisar si esta la data ya presente.
  """
  cursor.execute("SELECT num_mesa FROM segunda_vuelta_presidente WHERE num_mesa = '" + num_acta + "';")
  tmp_r = cursor.fetchall()
  if len(tmp_r) > 0:
    print "RECORD ALREADY THERE", num_acta, d_data
  else:
    print "NEW RECORD", num_acta, d_data
    cursor.execute("INSERT INTO segunda_vuelta_presidente (num_mesa,blancos,nulos,impugnados,gana_peru,fuerza_2011,electores_habiles,ciudadanos_total,departamento,provincia,distrito,local_de_votacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( num_acta, d_data[u'Votos Blancos'],d_data[u'Votos Nulos'],d_data[u'Votos Impugnados'], d_data[u'GANA PERU'], d_data[u'FUERZA 2011'], d_data[u'Electores H&aacute;biles: '], d_data[u'Total de Ciudadanos que Votaron: '], d_data[u'Departamento:'], d_data[u'Provincia:'], d_data[u'Distrito:'], d_data[u'Local de Votaci&oacute;n: '] )) 
  
"""
Table: PrimeraVueltaPresidente
Columns:
Número de Mesa (P) | Agrupación #1 | Blancos | Nulos | Impugnados | Depar| Prov| Dist | Local | Electores Habiles | Ciudadnos que no votaron | 
"""

def insert_post_codes(region,provincia,distrito,centro,cursor):
  """
  d_data: diccionario con ubigeos
  centro: numbre del centro de votacion
  cursor: db cursor
  """
  cursor.execute("SELECT centro FROM ubigeo WHERE centro = '" + centro + "' AND distrito = '" + distrito + "';")
  tmp_q = cursor.fetchall()
  if len(tmp_q) >:
    print "RECORD ALREADY THERE"
  else
    print "NEW RECORD"
    cursor.execute("INSERT INTO ubigeo (region,provincia,distrito,centro) VALUES (%s,%s,%s,%s)",(region,provincia,distrito,centro))

def parse_acta_congreso(f_handle):
  """
  Información a extraer:
  #Mesa
  UBIGEO + Local
  #Electores Hábiles
  #Electores Votaron
  Estado del Acta
  Resultados
  """
  pass

return d_data

  
if __name__ == "__main__":
  f_handle = open('Ejemplo_Acta_Congreso.html','r')
  data = parse_acta_congreso(f_handle)
  print data
  """conn = psycopg2.connect("dbname=eleccionesperu2011 user=pirata")
  cursor = conn.cursor()
  insert_data_SVP('test', data, cursor)
  conn.commit()
  cursor.close()
  conn.close()
  f_handle.close()
  """
