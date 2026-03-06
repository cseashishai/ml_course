import logging

logging.basicConfig(
    filename ='app.log', # It be use to crat a file 
    filemode='w',
     
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # its br creat date time or such or more such of directory
    datefmt='%Y-%m-%d %H:%M:%S', # its be creating year , month,hourse,minute
    force=True
)