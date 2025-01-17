import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 243149489 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    eps = alpha * 0.0001

    return (2 * x - 0.017).mean() + 2 * uniform.ppf(alpha / 2 - eps) * np.sqrt(np.var(2 * x - 0.017))/ np.sqrt(len(x)), \
    (2 * x - 0.017).mean() + 2 * uniform.ppf(1 - alpha / 2 + eps) * np.sqrt(np.var(2 * x - 0.017))/ np.sqrt(len(x))
