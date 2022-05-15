import argparse

from .train import run as train

import fire


def main():
  fire.Fire({
      'train': train,
  })

if __name__=="__main__":
    main()
