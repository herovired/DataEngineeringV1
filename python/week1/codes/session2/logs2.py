import logging 
logging.basicConfig(level=logging.INFO,
                    filename="sample.log",
                    format='%(name)s - %(levelname)s - %(message)s')
def hypotenuse(a:int, b:int):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5
c = hypotenuse(a=4,b=5)
logging.info(f"Hypotenuse is {c}")