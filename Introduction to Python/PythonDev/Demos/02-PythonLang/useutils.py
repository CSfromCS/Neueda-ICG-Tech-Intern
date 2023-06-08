# import specific module(s) from a package
import utils.constants.metric

print("Inch to centimetre: %.4f" % utils.constants.metric.INCH_TO_CM)
print("Mile to kilometre:  %.4f" % utils.constants.metric.MILE_TO_KM)


# import specific module(s) from a package, into the current symbol namespace
from utils.constants import metric

print("Inch to centimetre: %.4f" % metric.INCH_TO_CM)
print("Mile to kilometre:  %.4f" % metric.MILE_TO_KM)


# import specific name(s_ from a specific module from a package, into the current symbol namespace
from utils.constants.metric import INCH_TO_CM, MILE_TO_KM

print("Inch to centimetre: %.4f" % INCH_TO_CM)
print("Mile to kilometre:  %.4f" % MILE_TO_KM)


# import * from a package
from utils.messages import *

print("Hello in French:   %s" % utils.messages.french.HELLO)
print("Goodbye in French: %s" % utils.messages.french.GOODBYE)
print("Hello in Norwegian:   %s" % utils.messages.norwegian.HELLO)
print("Goodbye in Norwegian: %s" % utils.messages.norwegian.GOODBYE)
