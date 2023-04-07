import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return (2 * x - 0.017).mean() + 2 * uniform.ppf(alpha / 2) * np.sqrt(np.var(2 * x - 0.017))/ np.sqrt(len(x)), \
    (2 * x - 0.017).mean() + 2 * uniform.ppf(1 - alpha / 2) * np.sqrt(np.var(2 * x - 0.017))/ np.sqrt(len(x))
