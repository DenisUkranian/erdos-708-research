// Exact verifier for the coefficient-two density interval in the accompanying note.
// Compile: c++ -std=c++17 -O3 verify708_density.cpp -o verify708_density
// Arguments: lower density and upper density in 1/10000 units, then 0 (high mean) or 1 (low mean).
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>

using Int = std::int64_t;
using Box = std::array<Int, 10>;
constexpr Int unit = 32000000;
constexpr Int tableUnit = unit / 32000;
constexpr Int rawCap = 12976 * tableUnit;
constexpr Int margin = 16;
constexpr std::array<Int, 24> capacity = {
    660, 647, 634, 622, 610, 599, 588, 577, 567, 557, 548, 538,
    529, 521, 513, 504, 497, 489, 482, 475, 468, 461, 454, 448};
constexpr std::array<Int, 24> highThreshold = {
    9206, 8871, 8533, 8190, 7844, 7495, 7141, 6784, 6422, 6056, 5686, 5312,
    4933, 4550, 4162, 3770, 3372, 2970, 2562, 2149, 1731, 1307, 877, 442};
constexpr std::array<Int, 24> prefixLoss = {
    336, 674, 1016, 1362, 1712, 2066, 2423, 2785, 3151, 3521, 3895, 4274,
    4657, 5045, 5437, 5835, 6237, 6645, 7058, 7476, 7900, 8330, 8765, 9206};
constexpr std::array<Int, 19> thresholds = {
    70, 65, 60, 55, 50, 45, 40, 35, 30, 27, 25, 23, 20, 17, 15, 12, 10, 8, 5};

Int positive(Int x) { return std::max<Int>(0, x); }
Int floorProduct(Int a, Int b) { return a * b / unit; }
Int ceilingRatio(Int numerator, Int denominator) { return (numerator + denominator - 1) / denominator; }
Int ceilingProduct(Int a, Int b) { return ceilingRatio(a * b, unit); }
Int prefix(Int mass, Int loss) { return std::clamp<Int>(mass - loss, 0, unit); }

using Allocation = std::array<std::pair<Int, Int>, 24>;
Int minimumCost(Allocation& costs, Int demand) {
    std::sort(costs.begin(), costs.end());
    Int total = 0;
    for (auto [cost, limit] : costs) {
        Int take = std::min(demand, limit);
        total += floorProduct(take, cost);
        demand -= take;
        if (demand == 0) break;
    }
    return total;
}

struct Checker {
    Int densityLow, densityHigh, odds, goal;
    bool lowMean;
    Int boxes = 0, schurBoxes = 0;

    bool passes(Box box) {
        ++boxes;
        auto [nuLow, nuHigh, qLow, qHigh, offsetLow, offsetHigh,
              chargeLow, chargeHigh, prefixChargeLow, prefixChargeHigh] = box;
        const Int meanUpper = unit + (lowMean ? -offsetLow : offsetHigh);
        const Int meanLower = unit + (lowMean ? -offsetHigh : offsetLow);
        const Int posOffsetHigh = lowMean ? 0 : offsetHigh;
        const Int poolLow = std::clamp<Int>(meanLower - nuHigh - qHigh, 0, 3 * unit / 2);
        const Int poolHigh = std::clamp<Int>(meanUpper - nuLow - qLow, 0, 3 * unit / 2);
        const Int cut = prefixLoss[15] * tableUnit;
        const Int rLow = prefix(poolLow, cut), rHigh = prefix(poolHigh, cut);
        const Int tLow = poolLow - rLow, tHigh = poolHigh - rHigh;

        prefixChargeHigh = std::min({prefixChargeHigh, chargeHigh, rHigh});
        if (prefixChargeLow > prefixChargeHigh) return true;

        // Lower-bound half the mass of forbidden pairs, D0/2.
        Int half = 0, remainder = qLow;
        for (int i = 0; i < 24; ++i) {
            Int take = std::min(remainder, capacity[i] * tableUnit);
            half += floorProduct(take, positive(nuLow - highThreshold[i] * tableUnit));
            remainder -= take;
        }
        const Int baseline = offsetLow + chargeLow + floorProduct(nuLow, nuLow) + 2 * half;
        if (baseline >= goal) return true;

        // Existing split-pair/triple lower bound on the pure target contribution.
        const Int crossCharge = rLow >= tLow ? prefixChargeLow : prefixChargeHigh;
        const Int rr = floorProduct(rLow, positive(rLow - 2 * prefixChargeHigh));
        const Int tt = floorProduct(tLow, positive(tLow - 2 * (chargeHigh - prefixChargeLow)));
        const Int rt = 2 * positive(floorProduct(rLow, tLow) - ceilingProduct(tLow, crossCharge)
                                    - ceilingProduct(rLow, chargeHigh - crossCharge));
        const Int lossRR = std::min(ceilingProduct(3 * tHigh, rr), ceilingRatio(ceilingProduct(3 * rHigh, rt), 2));
        Int lossTT = ceilingRatio(ceilingProduct(3 * tHigh, rt), 2);
        if (3 * unit >= tHigh + 3 * rHigh) lossTT = std::min(lossTT, ceilingProduct(3 * rHigh, tt));
        const Int pure = std::max({
            floorProduct(3 * unit - rHigh, rr) + floorProduct(3 * unit - tHigh, tt) + 3 * rt - lossRR - lossTT,
            floorProduct(3 * unit - poolHigh, rr + tt + rt),
            floorProduct(floorProduct(poolLow, 3 * unit - poolLow), positive(poolLow - 2 * chargeHigh))}) / 6;

        // Bernoulli rounding of high labels gives the unconditional squared-remainder charge.
        const Int p0 = nuLow + qLow - densityHigh - ceilingRatio(ceilingProduct(qHigh, qHigh), 2)
                       - ceilingProduct(qHigh, nuHigh) + half;
        const Int capMaximizer = std::clamp<Int>(rawCap / 2, qLow, qHigh);
        const Int upperChargeCap = capMaximizer - capMaximizer * capMaximizer / rawCap;
        Int previousSquare = 0, source = 0, slope = 0;
        std::array<Int, 19> breaks{};
        for (unsigned i = 0; i < thresholds.size(); ++i) {
            Int tau = thresholds[i] * (unit / 100);
            Int v = positive(odds - tau - posOffsetHigh), square = v * v;
            Int weight = (square - previousSquare) / tau;
            Int scaledP0 = p0 >= 0 ? floorProduct(tau, p0) : -ceilingProduct(tau, -p0);
            Int breakpoint = positive(scaledP0 - std::min(upperChargeCap, ceilingProduct(unit - tau, rawCap - qLow)));
            breaks[i] = breakpoint;
            if (weight && breakpoint) {
                source += floorProduct(weight, breakpoint);
                slope += floorProduct(weight, tau) / 2;
            }
            previousSquare = square;
        }
        if (baseline + source >= goal) return true;

        // Couple the affine source estimate in D with the split mixed target estimate.
        Allocation mixed, combined;
        for (int i = 0; i < 24; ++i) {
            Int loss = prefixLoss[i] * tableUnit, ri = prefix(poolLow, loss);
            Int charge = std::min(chargeHigh, prefixChargeHigh + positive(cut - loss));
            Int gain = floorProduct(2 * unit - ri, positive(ri - charge));
            if (i < 15) {
                Int riHigh = prefix(poolHigh, loss);
                Int v = std::min(ri - rLow, riHigh - rHigh);
                Int vHigh = std::min(cut - loss, riHigh - rLow);
                Int hr = positive(rLow - prefixChargeHigh), hv = positive(v - (chargeHigh - prefixChargeLow));
                gain = std::max({gain,
                    floorProduct(positive(2 * unit - rHigh - 2 * vHigh), hr) + floorProduct(2 * unit - vHigh, hv),
                    floorProduct(2 * unit - rHigh, hr) + floorProduct(positive(2 * unit - vHigh - 2 * rHigh), hv)});
            }
            Int forbidden = 2 * positive(nuLow - highThreshold[i] * tableUnit);
            mixed[i] = {gain, capacity[i] * tableUnit};
            combined[i] = {gain + floorProduct(forbidden, unit + slope), capacity[i] * tableUnit};
        }
        Int jointGamma = offsetLow + chargeLow + floorProduct(nuLow, nuLow) + source - ceilingProduct(2 * half, slope)
                         + 2 * (pure - posOffsetHigh) + minimumCost(combined, qLow);
        if (jointGamma >= goal) return true;

        // If the upper-price variance exceeds this allowance, the source bound already closes the box.
        Int allowedCharge = std::min(upperChargeCap, positive(goal - baseline - source));
        Int g = std::max(lowMean ? Int(0) : offsetLow,
                         pure + minimumCost(mixed, qLow) / 2 - ceilingRatio(allowedCharge, 2));

        // A sequence of counterexamples would force positive mean residual on A and negative mean on its complement.
        Int forced = floorProduct(unit - densityHigh, g);
        Int sourceOnA = forced * forced / densityHigh;
        for (Int shiftPercent : {0, 3, 7, 12, 18, 25}) {
            Int shift = shiftPercent * (unit / 100), previous = 0, shiftedSource = 0;
            for (unsigned i = 0; i < thresholds.size(); ++i) {
                Int tau = thresholds[i] * (unit / 100);
                Int v = positive(odds + shift - tau - posOffsetHigh), square = v * v;
                Int weight = (square - previous) / tau;
                shiftedSource += floorProduct(weight, breaks[i]);
                previous = square;
            }
            Int extra = sourceOnA + floorProduct(2 * shift, forced) - ceilingProduct(unit - densityLow, ceilingProduct(shift, shift));
            if (std::max(baseline, jointGamma - source) + shiftedSource + extra >= goal) return true;
        }

        // Integer Schur envelope on the original, unrounded source prices.
        for (Int rank = 1; rank <= 4; ++rank) {
            Int z = (rank - 1) * unit / 2 - meanLower;
            Int linear = z > 0 ? ceilingProduct(densityHigh, z) : -floorProduct(densityLow, -z);
            Int numerator = ceilingProduct(meanUpper, meanUpper) - floorProduct(nuLow, nuLow) - 2 * half;
            Int pairs = numerator > 0 ? ceilingRatio(numerator, 2 * rank) : numerator / (2 * rank);
            if (linear + pairs - floorProduct(unit - densityHigh, g) <= -margin) {
                ++schurBoxes;
                return true;
            }
        }

        box[9] = prefixChargeHigh;
        int axis = 0;
        for (int i = 2; i < 10; i += 2) {
            if (box[i + 1] - box[i] > box[axis + 1] - box[axis]) axis = i;
        }
        if (box[axis + 1] - box[axis] <= 128) {
            std::fprintf(stderr, "Unresolved box at coordinates");
            for (Int v : box) std::fprintf(stderr, " %lld", static_cast<long long>(v));
            std::fprintf(stderr, "\n");
            return false;
        }
        Int middle = (box[axis] + box[axis + 1]) / 2;
        Box right = box;
        box[axis + 1] = middle;
        right[axis] = middle;
        return passes(box) && passes(right);
    }
};

int main(int argc, char** argv) {
    if (argc != 4) return 2;
    long lo = std::strtol(argv[1], nullptr, 10), hi = std::strtol(argv[2], nullptr, 10);
    long lowMean = std::strtol(argv[3], nullptr, 10);
    if (lo < 3750 || hi > 3960 || lo > hi || (lowMean != 0 && lowMean != 1)) return 2;
    Int lower = lo * (unit / 10000), upper = hi * (unit / 10000);
    Checker checker{lower, upper, lower * unit / (unit - lower),
                    ceilingRatio((unit - 2 * lower) * unit, unit - lower) + margin, lowMean != 0};
    Int nuMax = 0;
    while (nuMax * nuMax < checker.goal * unit) nuMax += unit / 1000;
    Int bound = checker.goal;
    bool ok = checker.passes({0, nuMax, 0, rawCap, 0, bound, 0, bound, 0, bound});
    std::printf("%s density=%ld..%ld low_mean=%ld nodes=%lld schur_nodes=%lld\n", ok ? "PASS" : "FAIL",
                lo, hi, lowMean, static_cast<long long>(checker.boxes), static_cast<long long>(checker.schurBoxes));
    return ok ? 0 : 1;
}
