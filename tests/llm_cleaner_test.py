from utils.llm import get_llm
from agents.component_cleaner import ComponentCleaner

cleaner = ComponentCleaner()

component = '4500 5615 O X HOME OFFICE/STUDY TI 14"-9" 18"-5" BENCH X 5395 5215 DRESSER DRESSER MIRROR MIRROR X'

cleaned_component = cleaner.clean(component)
print("Original Component:", component)
print("Cleaned Component:", cleaned_component)

# python -m tests.llm_cleaner_test