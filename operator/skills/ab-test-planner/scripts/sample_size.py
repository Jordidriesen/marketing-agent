#!/usr/bin/env python3
"""Sample size and duration for a two-variant A/B test on a conversion rate.

Usage: sample_size.py BASELINE_RATE MDE_RELATIVE MONTHLY_VOLUME [--variants 2] [--alpha 0.05] [--power 0.8]

  BASELINE_RATE    current conversion rate as a fraction or percent (0.02 or 2%)
  MDE_RELATIVE     smallest relative lift worth detecting (0.2 or 20% means 2.0% -> 2.4%)
  MONTHLY_VOLUME   visitors or sessions per month that enter the test, all variants together

Two-sided test on two proportions, normal approximation, equal split. Prints the sample per
variant, the total, and the duration in weeks. The numbers are a planning estimate, not a promise
of a result: they say how much traffic the test needs, not what it will find.
"""
import argparse
import math
from statistics import NormalDist


def fraction(text):
    """'2%' and '0.02' both give 0.02; a bare number above 1 is read as a percent."""
    text = text.strip()
    value = float(text.rstrip('%'))
    if text.endswith('%') or value > 1:
        value /= 100
    if not 0 < value < 1:
        raise SystemExit(f'{text!r} must be between 0 and 100%')
    return value


def sample_per_variant(p1, mde, alpha, power):
    p2 = p1 * (1 + mde)
    if p2 >= 1:
        raise SystemExit('baseline x (1 + MDE) must stay below 100%')
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z_b = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    num = (z_a * math.sqrt(2 * p_bar * (1 - p_bar)) + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p2 - p1) ** 2), p2


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('baseline', type=str)
    ap.add_argument('mde', type=str)
    ap.add_argument('volume', type=float)
    ap.add_argument('--variants', type=int, default=2)
    ap.add_argument('--alpha', type=float, default=0.05)
    ap.add_argument('--power', type=float, default=0.8)
    a = ap.parse_args()
    p1, mde = fraction(a.baseline), fraction(a.mde)
    n, p2 = sample_per_variant(p1, mde, a.alpha, a.power)
    total = n * a.variants
    weeks = total / (a.volume / 4.345) if a.volume > 0 else float('inf')
    print(f'baseline {p1:.2%} -> {p2:.2%} (relative lift {mde:.0%}), alpha {a.alpha}, power {a.power}')
    print(f'sample per variant: {n:,}   total across {a.variants} variants: {total:,}')
    print(f'monthly volume {a.volume:,.0f} -> about {weeks:.1f} weeks ({weeks / 4.345:.1f} months)')
    if weeks > 8:
        print('VERDICT: longer than eight weeks. Do not run this as designed: pick a bigger lever, a higher-volume page, a micro-conversion with a real link to the goal, or fix tracking first.')
    elif weeks < 1:
        print('NOTE: under one week. Run at least two full weeks to cover weekday and weekend behaviour.')
    else:
        print('VERDICT: feasible. Run full weeks only, fixed horizon, no peeking.')


if __name__ == '__main__':
    main()
