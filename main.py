import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
from sklearn.metrics import *

import mender
import pysodb

sodb = pysodb.SODB()
adata_dict = sodb.load_dataset("Allen2022Molecular_aging")
