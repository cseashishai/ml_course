from loge import logging

def add(a,b):
    logging.debug("Given data in place")

    return a+b

logging.debug("Data inplaced are true")
print(add(10,5))