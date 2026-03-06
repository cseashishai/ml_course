import logging 

logging.basicConfig(  
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # its br creat date time or such or more such of directory
    datefmt='%Y-%m-%d %H:%M:%S', # its be creating year , month,hourse,minute
    # force=True
     handlers= [
         logging.FileHandler('app.log'),
         logging.StreamHandler()

     ]
)

logger=logging.getLogger("AithmaticAPP")

def add(a,b):
    result =a+b
    logger.debug(f'Adding : {a}+{b}={result}')
    return result

def subtract(a,b):
    result =a-b
    logger.debug(f'subtract : {a}-{b}={result}')
    return result

def multi(a,b):
    result =a*b
    logger.debug(f'mltiplication: {a}*{b}={result}')
    return result

def div(a,b):
    try:
          result =a/b
          logger.debug(f'Adding : {a}/{b}={result}')
          return result
    except ZeroDivisionError:
        logger.error("Divison by Zero error")
        return None
          
    
add(10,15)
subtract(10,10)
multi(5,6)
div(6,6)