# Indian Index Options Day Trading Routine

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/your-repo/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

This repository contains a comprehensive, structured routine for day trading Indian index options (e.g., Nifty 50, Bank Nifty, Sensex) on NSE/BSE. The routine is based on time-segmented market analysis, global correlations, option chain metrics, volatility patterns, and risk management principles synthesized from various trading guides. It includes a Python script to generate a Google Calendar `.ics` file for scheduling daily/weekly trading sessions and global market overlaps.

The routine emphasizes disciplined execution, starting from August 11, 2025 (aligned with the script's start date). Use it for consistency in intraday trading, adapting to expiries, volatility regimes, and global cues.

## Table of Contents
- [Overview](#overview)
- [Key Principles](#key-principles)
- [Daily Routine](#daily-routine)
- [Weekly/Monthly Overlays](#weeklymonthly-overlays)
- [Volatility Periods & Strategies Summary](#volatility-periods--strategies-summary)
- [Global Market Sessions](#global-market-sessions)
- [Installation and Usage](#installation-and-usage)
- [Generating the Google Calendar (.ics)](#generating-the-google-calendar-ics)
- [Tools and Resources](#tools-and-resources)
- [Risk Disclaimer](#risk-disclaimer)
- [Contributing](#contributing)
- [License](#license)

## Overview
This routine provides a data-driven framework for analyzing the Indian stock market, focusing on:
- **Time-Segmented Analysis**: Divided into pre-market, opening, mid-morning, lunch, afternoon, closing, and post-market sessions (9:15 AM - 3:30 PM IST market hours).
- **Global Correlations**: Integrates Asian, European, and US market influences via Gift Nifty and MCX commodities.
- **Option Chain Insights**: Metrics like Open Interest (OI), Put-Call Ratio (PCR), Implied Volatility (IV), Greeks, and Max Pain for strategy selection.
- **Strategies**: Opening Range Breakout (ORB), trend following, range trades, gamma scalping, etc., with risk-adjusted position sizing.
- **Calendar Integration**: A Python script generates a recurring `.ics` file for Google Calendar, including daily routines, day-specific overlays, and global sessions.

Adhere to this for consistency, refining via trade logs and backtests. Continuous learning: Incorporate alerts and evolve based on market regimes.

## Key Principles
- **Global Correlations**: Monitor Asian opens (5:30-7:00 AM IST) for pre-market bias, European overlaps (12:30-2:30 PM IST) for mid-session cues, and US markets (via Gift Nifty, 7:00 PM-1:30 AM IST) for next-day gaps.
- **Volatility & Volume Insights**: High volume spikes (e.g., ≥1.25× average) signal liquidity and potential breakouts; correlate with OI changes. IV >20% indicates expensive options (favor selling strategies); IV <15% favors buying. PCR >1.3 (bearish, potential contrarian calls); PCR <0.7 (bullish, contrarian puts).
- **Option Chain Workflow**: Spend ~23 minutes per major check: Fetch data (5m), analyze OI/PCR (5m), assess sentiment/structure (3m), risk via Greeks/Max Pain (5m), select strategies (5m).
- **ORB Integration**: Use 15-30 min OR (9:15-9:30/9:45 AM) for breakout entries, filtered by trend (e.g., above 5-EMA for longs), option chain S/R, and volume.
- **Expiry Adjustments**: Tuesdays (Nifty weekly) and Thursdays (Sensex weekly) feature high gamma/theta decay; focus on Max Pain migration and hedging. Monthly expiries (last Tue/Thu) involve institutional rebalancing.
- **Risk Management**: Position size 25-50% in high volatility; 75-100% in low. Use tight SL (0.3-0.5% in openings/closings), hedge with OTM options on expiries. Avoid illiquid strikes (wide bid-ask, low OI/volume).
- **Tools**: NSE option chain, Sensibull/QuantsApp for Greeks/PCR, TradingView for charts, economic calendar for events (RBI, US Fed, corporate results).
- **Monitoring Alerts**: Set for OI/volume spikes, PCR extremes (>1.3/<0.7), IV skew shifts, Max Pain changes.

## Daily Routine
Follow this sequence each trading day (weekdays), adapting for day-specific focuses (e.g., Monday gap analysis, Friday profit booking). All times in IST.

### 1. Pre-Market Preparation (7:00 AM - 9:15 AM)
- **Duration**: ~2 hours; focus on global setup and initial option chain scan.
- **Key Insights**:
  - Global: Review US close (Gift Nifty Session 2: 4:35 PM-2:45 AM) for gaps; Asian opens (Japan 5:30 AM, Hong Kong 6:45 AM, China 7:00 AM) for bias.
  - Economic Calendar: Domestic/global events; volatility regime (VIX/IV).
  - Option Chain: Spot, ATM, top OI, PCR, IV skew, Max Pain.
  - Volume/Volatility: Estimate from Gift Nifty; high Asian vol signals gaps.
- **Actions**:
  - 7:00-8:00 AM: Digest cues; project Nifty bias.
  - 8:00-8:30 AM: Scan MCX (opens 9:00 AM) for sectors.
  - 8:30-9:15 AM: Pre-opening volatility; plan ORB.
- **Strategy Prep**: Align with day.
- **Risk**: Set sizing (e.g., 25% for high IV/gaps).

### 2. Opening Session (9:15 AM - 10:15 AM)
- **Duration**: 1 hour; very high volatility/liquidity.
- **Key Insights**:
  - ORB: Mark 15-min range; trigger with volume ≥1.25× avg.
  - Option Chain: OI/volume spikes, PCR shifts, IV for strategies.
  - Volume/Volatility: Correlate with Asian overlaps.
  - Global: Validate Gift Nifty bias.
- **Actions**:
  - 9:15-9:30 AM: Form OR; monitor OI.
  - 9:30-10:15 AM: Execute ORB (SL inside boundary; targets 1:1/2:1); re-scan at 10:00 AM.
- **Strategy**: Breakout/ORB, gaps; gamma scalping on expiries.
- **Risk**: Tight SL (0.3-0.5%); hedge high gamma.

### 3. Mid-Morning Monitoring (10:15 AM - 12:00 PM)
- **Duration**: ~1.75 hours; high volatility, good liquidity.
- **Key Insights**:
  - Trend/Range: Momentum or consolidation; OI for S/R.
  - Option Chain: Re-analyze at 11:00 AM (volume vs OI, PCR, Greeks).
  - Volume/Volatility: Spikes for focus; low IV for buys.
  - Global: Prep European cues.
- **Actions**:
  - 10:15-11:00 AM: Confirm trend; adjust ORB.
  - 11:00-11:30 AM: Scan PCR/volume.
  - 11:30-12:00 PM: Prep lunch; enter trends.
- **Strategy**: Trend following, swings; sector rotation on Wednesdays.
- **Risk**: SL 0.5-1%; monitor theta.

### 4. Lunch Hour Check (12:00 PM - 1:00 PM)
- **Duration**: 1 hour; low volatility, moderate liquidity.
- **Key Insights**:
  - Range: High OI both sides.
  - Option Chain: Scan at 12:30 PM (IV contraction, Max Pain).
  - Volume/Volatility: Wider spreads; European breakout potential.
  - Global: European overlap starts (PMI impact).
- **Actions**:
  - 12:00-12:30 PM: Assess ranges.
  - 12:30-1:00 PM: Note reactions; check breaks.
- **Strategy**: Range trades (Iron Butterfly/Short Condor).
- **Risk**: Reduce size 50%; exit on breaks.

### 5. Afternoon Session (1:00 PM - 2:30 PM)
- **Duration**: 1.5 hours; medium volatility, good liquidity.
- **Key Insights**:
  - Momentum: Post-lunch positions; IV skew.
  - Option Chain: Re-scan at 1:30 PM (OI, Vega); US pre-market via Gift Nifty.
  - Volume/Volatility: Increasing; European correlations.
  - Global: Full European overlap; sector impacts.
- **Actions**:
  - 1:00-1:30 PM: Enter swings.
  - 1:30-2:00 PM: Review US.
  - 2:00-2:30 PM: Adjust for close.
- **Strategy**: Swings, volatility expansion (Long Strangle if low IV).
- **Risk**: SL 1%; hedge expiry weeks.

### 6. Closing Hour Execution (2:30 PM - 3:30 PM)
- **Duration**: 1 hour; very high volatility/liquidity.
- **Key Insights**:
  - Positioning: Squaring; Max Pain migration.
  - Option Chain: Final scan at 3:00 PM (PCR, theta/gamma).
  - Volume/Volatility: Settlement spikes.
  - Global: Prep US via Gift Nifty.
- **Actions**:
  - 2:30-3:00 PM: Scale out; enter momentum/expiry.
  - 3:00-3:20 PM: Trail SL; monitor reversals.
  - 3:20-3:30 PM: Exit high-risk; plan post-market.
- **Strategy**: Momentum scalping, straddles; profit booking on Fridays.
- **Risk**: Tight SL (0.3%); full hedge on expiries.

### 7. Post-Market Review (3:30 PM - 4:30 PM + Evening)
- **Duration**: 1 hour + Gift Nifty (up to 11:30 PM via MCX).
- **Key Insights**:
  - Performance: Log P&L, ORB wins, deviations.
  - Next-Day: Max Pain shift, US cues (opens 7:00 PM).
  - Volume/Volatility: Evening MCX correlations.
- **Actions**:
  - 3:40-4:00 PM: Journal.
  - 4:00-4:30 PM: Next-day plan.
  - Evening: Track Gift Nifty Session 2.
- **Strategy**: Overnight bias.

## Weekly/Monthly Overlays
- **Monday**: Gap focus; validate global cues.
- **Tuesday (Nifty Expiry)**: High gamma; PCR/Max Pain for contrarian plays.
- **Wednesday**: Consolidation; range strategies.
- **Thursday (Sensex Expiry)**: Volatility plays; BSE-NSE arbitrage.
- **Friday**: Defensive; week-end review (backtest ORB, IV thresholds).
- **Monthly Expiry Week**: Track IV term structure; deploy butterflies in final days.
- **Quarterly**: Audit metrics; adjust for rebalancing.

## Volatility Periods & Strategies Summary

| Time Slot      | Volatility Level | Key Focus         | Typical Strategies         | Position Sizing |
|----------------|------------------|-------------------|----------------------------|-----------------|
| 9:15-10:15 AM  | Very High       | ORB, gaps        | Breakout, momentum         | 25-50%         |
| 10:15-12:00 PM | High            | Trends           | Trend following            | 50-75%         |
| 12:00-1:00 PM  | Low             | Ranges           | Iron Condor, Butterfly     | 75-100%        |
| 1:00-2:30 PM   | Medium          | Swings           | Calendar spreads           | 50-75%         |
| 2:30-3:30 PM   | Very High       | Expiry/momentum  | Gamma scalping, straddles  | 25-50%         |

## Global Market Sessions
Integrated into the calendar:
- **Asian Markets Open**: 5:30-7:00 AM (Japan, HK, China) – Pre-market bias.
- **European Markets Overlap**: 12:30-2:30 PM – Mid-session cues.
- **US Markets**: 7:00 PM-1:30 AM (next day) – Gap projection.
- **Gift Nifty Session 1**: 6:30 AM-3:40 PM – Overlap with Indian market.
- **Gift Nifty Session 2**: 4:35 PM-2:45 AM (next day) – Post-market trends.
- **MCX Commodity Trading**: 9:00 AM-11:30 PM – Sector correlations.

## Installation and Usage
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Ensure Python 3.8+ is installed.
3. No additional dependencies needed (uses standard libraries: `datetime`, `zoneinfo`).

## Generating the Google Calendar (.ics)
The script (`generate_ics.py`) creates `trading_routine.ics` with recurring weekday events starting August 11, 2025.
1. Run the script:
   ```
   python generate_ics.py > trading_routine.ics
   ```
2. Import into Google Calendar: Settings > Import & export > Import the `.ics` file.
3. Events recur weekly on weekdays (MO-FR). Customize in Google Calendar (e.g., add reminders, handle holidays).

The script includes:
- Daily routine events with descriptions.
- Weekly day-specific overlays (e.g., Tuesday expiry focus).
- Global sessions (e.g., US overnight as spanning events).

## Tools and Resources
- **Platforms**: NSE option chain, Sensibull/QuantsApp, TradingView.
- **Alerts**: For OI/volume, PCR, IV, Max Pain.
- **Backtesting**: Refine ORB/strategies via trade logs.

## Risk Disclaimer
Trading involves significant risk of loss and is not suitable for all investors. This routine is for educational purposes only; consult a financial advisor. Past performance is not indicative of future results.

## Contributing
Pull requests welcome! For major changes, open an issue first.

## License
[MIT](LICENSE) - Free to use, modify, and distribute.
