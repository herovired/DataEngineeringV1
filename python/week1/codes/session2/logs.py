import logging 
logging.basicConfig(level=logging.INFO)
def hypotenuse(a:int, b:int):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5
c = hypotenuse(a=4,b=5)
logging.info(f"Hypotenuse is {c}")