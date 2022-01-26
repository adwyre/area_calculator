# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(5, 10)

rect.set_width(7)
rect.set_height(52)
rect.get_picture()

# Run unit tests automatically
main(module='test_module', exit=False)
