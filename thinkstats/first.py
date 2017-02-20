"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import survey

# copying Mean from thinkstats.py so we don't have to deal with
# importing anything in Chapter 1

def Mean(t):
    """Computes the mean of a sequence of numbers.

    Args:
        t: sequence of numbers

    Returns:
        float
    """
    return float(sum(t)) / len(t)
    
def Var(t, mu=None):
    """Computes the variance of a sequence of numbers.

    Args:
        t: sequence of numbers
        mu: value around which to compute the variance; by default,
            computes the mean.

    Returns:
        float
    """
    if mu is None:
        mu = Mean(t)

    # compute the squared deviations and return their mean.
    dev2 = [(x - mu)**2 for x in t]
    var = Mean(dev2)
    return var

def MeanVar(t):
    """Computes the mean and variance of a sequence of numbers.

    Args:
        t: sequence of numbers

    Returns:
        tuple of two floats
    """
    mu = Mean(t)
    var = Var(t, mu)
    return mu, var

def PartitionRecords(table):
    """Divides records into two lists: first babies and others.

    Only live births are included

    Args:
        table: pregnancy Table
    """
    firsts = survey.Pregnancies()
    others = survey.Pregnancies()

    for p in table.records:
        # skip non-live births
        if p.outcome != 1:
            continue

        if p.birthord == 1:
            firsts.AddRecord(p)
        else:
            others.AddRecord(p)

    return firsts, others


def Process(table):
    """Runs analysis on the given table.
    
    Args:
        table: table object
    """
    table.lengths = [p.prglength for p in table.records]
    table.n = len(table.lengths)
    table.mu, table.var = MeanVar(table.lengths)


def MakeTables(data_dir='.'):
    """Reads survey data and returns tables for first babies and others."""
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)

    firsts, others = PartitionRecords(table)
    
    return table, firsts, others


def ProcessTables(*tables):
    """Processes a list of tables
    
    Args:
        tables: gathered argument tuple of Tuples
    """
    for table in tables:
        Process(table)
        
        
def Summarize(data_dir):
    """Prints summary statistics for first babies and others.
    
    Returns:
        tuple of Tables
    """
    table, firsts, others = MakeTables(data_dir)
    ProcessTables(firsts, others)
        
    print ('Number of first babies', firsts.n)
    print ('Number of others', others.n)

    mu1, mu2 = firsts.mu, others.mu
    var1, var2 = firsts.var, others.var

    print ('Mean gestation in weeks:') 
    print ('First babies', mu1)
    print ('Others', mu2)
    
    print ('First babies', var1)
    print ('Others', var2)
    
    print ('Difference in days', (mu1 - mu2) * 7.0)
    print ('Difference in days', (var1 - var2) * 7.0)


def main(name, data_dir='.'):
    Summarize(data_dir)
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)
