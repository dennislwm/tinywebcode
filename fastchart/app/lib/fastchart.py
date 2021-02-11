#-------------
# Data library
import pandas as pd
from ta.momentum import RSIIndicator
import yfinance
#---------------
# Custom library
from pyfxgit.ChartCls import ChartCls
#-----------------
# Standard library
from datetime import date, datetime, timedelta; today = date.today()
import os

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                    M A I N   C L A S S                                   |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
class FastChart():

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                   C O N S T R U C T O R                                  |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def __init__(self):
    #----------------------------
    # initialize class _CONSTANTS
    self._init_meta()

    #----------------
    # Class variables
    self.out = 'png'
    self.symbol = ''
    self.main = None
    self.sub = None
    self.df = None
    self.chart = None

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                 C L A S S   M E T H O D S                                |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def get_symbol(self, symbol, main, sub):
    #-----------------------
    # Assign class variables
    self.symbol = symbol
    self.main = self.parse_query_main(main)
    self.sub = self.parse_query_sub(sub)
    self.df = yfinance.download(symbol, start=today-timedelta(weeks=52), end=today)
    self.chart = ChartCls(self.df, intSub=len(self.sub))

    #------------
    # Build chart
    if 'rsi' in sub:
      taRsi = RSIIndicator(close=self.df["Close"])
      dfRsi = pd.concat([taRsi.rsi()], axis=1)
      self.chart.BuildOscillator(sub.index('rsi'), dfRsi, intUpper=70, intLower=30, strTitle='RSI')
    self.plot_chart()

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                            I N T E R N A L   F U N C T I O N S                           |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def parse_query_main(strQuery):
    """Returns a list of main indicators, if any

    Args:
        strQuery (string): from query string main
    """
  def parse_query_sub(strQuery):
    """Returns a list of sub indicators, if any

    Args:
        strQuery (string): from query string sub
    """

  def plot_chart(self):
    self.chart.BuildMain(strTitle=self.symbol)
    #-----------
    # Save chart
    if self.out == 'png':
      self.chart.save("")
      print("Success: Saved chart")

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                C L A S S   M E T A D A T A                               |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def _init_meta(self):
    """
    | _strMETACLASS, _strMETAVERSION, _strMETAFILE used to save() and load() members
    """
    self._strMETACLASS = str(self.__class__).split('.')[1][:-2]
    self._strMETAVERSION = "0.1"
    """
    | Filename "_Class_Version_"
    """
    self._strMETAFILE = "_" + self._strMETACLASS + "_" + self._strMETAVERSION + "_"
