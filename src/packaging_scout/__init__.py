"""Scouting different options for packaging"""
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("packaging_scout").version
except DistributionNotFound:
     # package is not installed
     __version__ = "0+unknown"

