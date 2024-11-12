import torch


def show(x, desc=""):
    if desc:
        print(f"{x.shape} <- {desc}")
    else:
        print(f"{x.shape}")
