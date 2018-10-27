name = 'HFStrategy'

from HFStrategy.strategy import Strategy
from HFStrategy.indicators.indicator import Indicator
from HFStrategy.indicators.ema import EMA
from HFStrategy.indicators.rsi import RSI
from HFStrategy.indicators.roc import ROC
from HFStrategy.indicators.accumulation_distribution import AccumulationDistribution
from HFStrategy.indicators.acceleration import Acceleration
from HFStrategy.indicators.alma import ALMA
from HFStrategy.indicators.atr import ATR
from HFStrategy.indicators.accumulative_swing_index import AccumulativeSwingIndex
from HFStrategy.indicators.sma import SMA
from HFStrategy.indicators.awesome_oscillator import AO
from HFStrategy.indicators.balance_of_power import BOP
from HFStrategy.indicators.stddev import StdDeviation
from HFStrategy.indicators.bbands import BollingerBands
from HFStrategy.indicators.chaikin_money_flow import CMF
from HFStrategy.indicators.chaikin_oscillator import ChaikinOsc
from HFStrategy.indicators.chande_momentum_oscillator import ChandeMO
from HFStrategy.indicators.wma import WMA
from HFStrategy.indicators.coppock_curve import CoppockCurve
from HFStrategy.indicators.detrended_price_oscillator import DPO
from HFStrategy.indicators.donchian_channels import DC
from HFStrategy.indicators.ease_of_movement import EOM
from HFStrategy.indicators.ema_vol import EMAVolume
from HFStrategy.indicators.envelope import Envelope
from HFStrategy.backtest import execOffline