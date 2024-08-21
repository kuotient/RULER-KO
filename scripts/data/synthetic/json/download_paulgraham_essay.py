import pandas as pd
from datasets import load_dataset

dataset = load_dataset("kuotient/ruler-ko-essay", split='train')
dataset.to_json('PaulGrahamEssays.json', force_ascii=False)