#!/usr/bin/env python3
"""
Quantitative Metrics Calculator

A module for calculating basic quantitative financial metrics including
simple moving averages, volatility, and Sharpe ratios.
"""

import math
from typing import List, Union


def validate_prices(prices: List[Union[int, float]]) -> None:
    """
    Validate price data for calculations.
    
    Args:
        prices: List of price values
        
    Raises:
        ValueError: If prices list is empty or contains invalid values
        TypeError: If prices is not a list or contains non-numeric values
    """
    if not isinstance(prices, list):
        raise TypeError("Prices must be a list")
    
    if len(prices) == 0:
        raise ValueError("Prices list cannot be empty")
    
    for i, price in enumerate(prices):
        if not isinstance(price, (int, float)):
            raise TypeError(f"Price at index {i} is not numeric: {price}")
        if math.isnan(price) or math.isinf(price):
            raise ValueError(f"Price at index {i} is invalid: {price}")


def validate_window_size(window_size: int, data_length: int) -> None:
    """
    Validate window size for moving average calculations.
    
    Args:
        window_size: Size of the moving window
        data_length: Length of the data series
        
    Raises:
        ValueError: If window size is invalid
        TypeError: If window size is not an integer
    """
    if not isinstance(window_size, int):
        raise TypeError("Window size must be an integer")
    
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    
    if window_size > data_length:
        raise ValueError("Window size cannot be larger than data length")


def simple_moving_average(prices: List[Union[int, float]], window_size: int) -> List[float]:
    """
    Calculate simple moving average for a list of prices.
    
    Args:
        prices: List of price values
        window_size: Number of periods to include in moving average
        
    Returns:
        List of moving averages (length = len(prices) - window_size + 1)
        
    Raises:
        ValueError: If inputs are invalid
        TypeError: If inputs are of incorrect type
    """
    validate_prices(prices)
    validate_window_size(window_size, len(prices))
    
    if len(prices) < window_size:
        return []
    
    moving_averages = []
    for i in range(len(prices) - window_size + 1):
        window = prices[i:i + window_size]
        average = sum(window) / window_size
        moving_averages.append(round(average, 6))
    
    return moving_averages


def calculate_returns(prices: List[Union[int, float]]) -> List[float]:
    """
    Calculate period-to-period returns from price data.
    
    Args:
        prices: List of price values
        
    Returns:
        List of returns (length = len(prices) - 1)
    """
    validate_prices(prices)
    
    if len(prices) < 2:
        return []
    
    returns = []
    for i in range(1, len(prices)):
        if prices[i-1] == 0:
            raise ValueError("Cannot calculate return when previous price is zero")
        ret = (prices[i] - prices[i-1]) / prices[i-1]
        returns.append(ret)
    
    return returns


def volatility(returns: List[Union[int, float]]) -> float:
    """
    Calculate volatility as standard deviation of returns.
    
    Args:
        returns: List of return values
        
    Returns:
        Volatility (standard deviation) of returns
        
    Raises:
        ValueError: If returns list is empty
        TypeError: If returns is not a list or contains non-numeric values
    """
    if not isinstance(returns, list):
        raise TypeError("Returns must be a list")
    
    if len(returns) == 0:
        raise ValueError("Returns list cannot be empty")
    
    for i, ret in enumerate(returns):
        if not isinstance(ret, (int, float)):
            raise TypeError(f"Return at index {i} is not numeric: {ret}")
        if math.isnan(ret) or math.isinf(ret):
            raise ValueError(f"Return at index {i} is invalid: {ret}")
    
    if len(returns) == 1:
        return 0.0
    
    mean_return = sum(returns) / len(returns)
    squared_diffs = [(r - mean_return) ** 2 for r in returns]
    variance = sum(squared_diffs) / (len(returns) - 1)
    return math.sqrt(variance)


def sharpe_ratio(returns: List[Union[int, float]], risk_free_rate: float = 0.0) -> float:
    """
    Calculate Sharpe ratio of returns.
    
    Args:
        returns: List of return values
        risk_free_rate: Risk-free rate (default: 0.0)
        
    Returns:
        Sharpe ratio
        
    Raises:
        ValueError: If returns list is empty or if all returns equal risk-free rate
        TypeError: If inputs are of incorrect type
    """
    if not isinstance(returns, list):
        raise TypeError("Returns must be a list")
    
    if not isinstance(risk_free_rate, (int, float)):
        raise TypeError("Risk-free rate must be numeric")
    
    if len(returns) == 0:
        raise ValueError("Returns list cannot be empty")
    
    if math.isnan(risk_free_rate) or math.isinf(risk_free_rate):
        raise ValueError("Risk-free rate is invalid")
    
    for i, ret in enumerate(returns):
        if not isinstance(ret, (int, float)):
            raise TypeError(f"Return at index {i} is not numeric: {ret}")
        if math.isnan(ret) or math.isinf(ret):
            raise ValueError(f"Return at index {i} is invalid: {ret}")
    
    mean_return = sum(returns) / len(returns)
    excess_return = mean_return - risk_free_rate
    vol = volatility(returns)
    
    if vol == 0:
        if excess_return == 0:
            return 0.0
        else:
            # Return infinity with appropriate sign
            return math.copysign(float('inf'), excess_return)
    
    return excess_return / vol


def main() -> None:
    """
    Example usage of the quant metrics calculator.
    """
    # Example data
    prices = [100, 102, 101, 103, 105, 107, 106, 108, 110, 112]
    risk_free_rate = 0.01
    
    print("Quantitative Metrics Calculator Example")
    print("=" * 40)
    print(f"Prices: {prices}")
    print(f"Risk-free rate: {risk_free_rate}")
    print()
    
    try:
        # Calculate simple moving average
        window = 3
        sma = simple_moving_average(prices, window)
        print(f"Simple Moving Average (window={window}):")
        print(f"  {sma}")
        print()
        
        # Calculate returns
        returns = calculate_returns(prices)
        print("Returns:")
        print(f"  {[round(r, 6) for r in returns]}")
        print()
        
        # Calculate volatility
        vol = volatility(returns)
        print(f"Volatility: {vol:.6f}")
        print()
        
        # Calculate Sharpe ratio
        sr = sharpe_ratio(returns, risk_free_rate)
        print(f"Sharpe Ratio: {sr:.6f}")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()