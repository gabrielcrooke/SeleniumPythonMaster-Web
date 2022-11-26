import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class funcionesGlobales:

    def __init__(self, driver):
        self.driver = driver

    # Funcion tiempo. Dar unicamente tiempo.
    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    # Funcion navegar, tomar URL de prueba.
    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Pagina Abierta: " + str(Url))
        t = time.sleep(Tiempo)
        return t

    # Funcion para tomar elemento por Xpath y id
    def Texto_Mixto(self, tipo, selector, texto, Tiempo):
        if tipo == "xpath":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('xpath', selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element('xpath', selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {}".format(selector, texto))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
        elif tipo == "id":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('id', selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element('id', selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {}".format(selector, texto))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)

    # Funcion clic por Xpath y id
    def Click_Mixto(self, tipo, selector, Tiempo):
        if tipo == "xpath":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('xpath', selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element('xpath', selector)
                val.click()
                print("Damos click en el elemento {}".format(selector))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return t
        elif tipo == "id":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('id', selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element('id', selector)
                val.click()
                print("Damos click en el elemento {}".format(selector))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return t

    # Funcion Select por tipo(Listas-xpath)
    def Select_Xpath_Type(self, xpath, tipo, dato, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('xpath', xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element('xpath', xpath)
            val = Select(val)
            if tipo == "text":
                val.select_by_visible_text(dato)
            elif tipo == "index":
                val.select_by_index(dato)
            elif tipo == "value":
                val.select_by_value(dato)
            print("El campo Seleccionado es -> {}".format(dato))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + " " + xpath)

    # CARGAR ARCHIVOS POR XPATH
    def Upload_xpath(self, xpath, ruta, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('xpath', xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element('xpath', xpath)
            val.send_keys(ruta)
            print('Se carga la imagen {}'.format(ruta))
            t = time.sleep(Tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + " " + xpath)

    # Funcion Radio y Check
    def Check_Xpath(self, xpath, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('xpath', xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element('xpath', xpath)
            val.click()
            print('Click en el elemento {}'.format(xpath))
            t = time.sleep(Tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + " " + xpath)
            return t

    # Funcion Radio y check multiples
    def Check_Xpath_Multiples(self, Tiempo, *args):
        try:
            for num in args:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('xpath', num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element('xpath', num)
                val.click()
                print('Click en el elemento {}'.format(num))
                t = time.sleep(Tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el elemento" + " " + num)
                return t

    # Funcion para salida de exito por la prueba
    def Salida(self):
        print("Se termina la prueba exitosamente")
