from BoardingPassScanner import findMaxSeatId, findMissingSeatId

############################Input###################################
inputSeatingInstructions = [
    "FFBFFBFLLR",
    "BFBFBFBRLR",
    "FBFFBFBRRL",
    "BBFFFBFLLR",
    "BFFFFFBLRL",
    "BFBBFBBRLR",
    "FBFBFBBRRL",
    "FBBBFBFLRL",
    "BFFFFBBRRL",
    "FBBBBBFLLR",
    "FBFFFBFLLR",
    "FFBBBFBLRR",
    "BFFFBBFLRL",
    "FFBBBFBLLL",
    "FBFBBFFLRR",
    "FBFBBBBLLR",
    "FFBBBFFRLR",
    "FBFBBFFRRL",
    "FBBBFFFLRR",
    "FFBBFFBLLR",
    "BFBFBFBLLR",
    "BFBBFFFLLL",
    "FBFBBFBRRL",
    "FFBBFFBLRR",
    "FFFBFBBLRR",
    "FFFFBBBRRL",
    "BFBBBBFRLL",
    "FBFBBFFLLR",
    "FFFBFBBLLR",
    "FFBFBBBRRL",
    "BFFBBFFLLR",
    "BFFFBBFLLR",
    "FBBFBBFRRR",
    "FFFBBFFRLL",
    "BFBFBBFRRR",
    "FBBFFBBRLR",
    "FBFFBBFRRL",
    "BFFFFBFLLR",
    "BBFFBFBLRL",
    "FBFBBBBLRL",
    "FBFBFBFRLL",
    "FFBFBFFLLR",
    "BFBFBBBRLR",
    "BFBBFFBLRR",
    "FFBFBFFLLL",
    "FFFFBBBLLR",
    "FFBBBBBLRR",
    "FFBFBBFLLR",
    "BFFFBBBRLL",
    "BFBFBFFLRR",
    "FBBBBFFRLR",
    "BFBFFBBRLL",
    "FBFBBFBRRR",
    "BFBFFBBLLL",
    "BFBFBBFLRL",
    "BBFFFFBLLR",
    "FFFBFFFRLL",
    "FBFFFBBRLL",
    "FFFBBBBLRR",
    "FBBBFBBLRL",
    "BBFFBFFRRR",
    "BFFBFFFLRR",
    "FBBBBBBLLR",
    "BFBBFFBLLL",
    "BFFBBBFRLR",
    "FBBBFFFLRL",
    "BBFFFBFRRL",
    "BBFFBFFRRL",
    "FFBBFFFLRR",
    "BBFFBFBRLR",
    "BBFFFFBRLR",
    "FFFFBBFLRL",
    "FFBBBFBRRR",
    "FFBFBBFLRR",
    "FFFBBFBRRR",
    "FBFFBFBRRR",
    "BFFFFFBRRR",
    "BFBFFBFLRL",
    "FFBBBBBLLL",
    "BFFFFBBRRR",
    "FBFBFFBRLR",
    "FBFFFFBLLR",
    "FFFBFFFLLL",
    "BFFFFFFLLR",
    "BBFFFFBRRL",
    "FBBFBBBRRL",
    "BFFFFFFLLL",
    "FBFBFFBLRR",
    "FFFBBFFRLR",
    "FBBFFBBLLL",
    "BFBBBFFLRL",
    "BFBFBBBRLL",
    "FBFBBFFLLL",
    "FFBBFFBRLL",
    "BFFFFBBLLR",
    "FFBBFBFLLL",
    "FFFFBBBRRR",
    "BFFFBBBLLL",
    "BFFBBFBRLR",
    "FFBBBFFLLR",
    "FBBBFFBRLR",
    "FFBFBFBRLL",
    "FFFBFFFLRR",
    "FFBBFBBLRL",
    "BFFBFBFLRR",
    "FFBFFFFRLR",
    "BFBFFFFLLL",
    "BFBBFBFRRR",
    "BFBFBFFRLL",
    "BFFFBFBRLL",
    "FFBBFBFLRR",
    "FFBFFFFRRL",
    "BFBBBBFLLL",
    "BFBFBFBRRR",
    "FFFFBBFLRR",
    "FBBBBFFLRL",
    "BFBFFFBLRL",
    "BFFBBFBRLL",
    "FBFFBBFLLL",
    "BFBBBBBLRL",
    "FFBFBBBLLR",
    "FBBFFBBLRR",
    "FFBFFFBRRR",
    "FFFBBBBRRR",
    "FBBBBBBLRL",
    "FFFBBFFLLL",
    "BBFFBFBLRR",
    "BFFBFFBRLR",
    "FFBBFBBRLL",
    "BFFBFBBRLR",
    "FBFBFBFRRL",
    "BFBBBFBRLL",
    "FFFFBBBLRR",
    "BBFFFFFLLR",
    "FFBFFFFLLL",
    "BFBBFBFRLR",
    "FFBBBBFRLR",
    "BFBFBBBLRL",
    "FBBFFFFRLL",
    "BFFFBBBLRL",
    "FBBBBFBRLL",
    "FFBFFFFRRR",
    "BFFFBFBRLR",
    "FBBBFBBLLL",
    "FFBFFBBLLL",
    "FBFFFBFRLL",
    "FFFFBBBRLR",
    "BBFFFBBLLL",
    "BBFFFFBLRL",
    "FBFBBBFRRL",
    "BFBFFBBRLR",
    "FBBFFBBLLR",
    "BFFBBFFLLL",
    "FFBFBBBLLL",
    "BFFBFFFRRL",
    "BFBBBFBRLR",
    "FBFBBBFLLL",
    "BFFBBBBLRR",
    "BFFBFBFLLL",
    "FFFBBBBLLR",
    "BFFFBFFLLR",
    "FFFBFBBRLL",
    "FFBBBBFRRL",
    "FBFBFBBLLR",
    "BBFFBFFLRL",
    "FBFBFBFLLR",
    "FBFBFFFLLR",
    "BFFFBFFLRR",
    "BFFBFFBRRR",
    "FFFFBBBLLL",
    "FBBFBFFLLR",
    "FFBBFBFRRL",
    "BFBFBBBLRR",
    "BFFFFFBRLR",
    "BFBBBBFRRL",
    "FFFBBBFLRR",
    "FBBFBFBRLL",
    "FFFBFFBRLR",
    "BFFFFFFRRL",
    "BFFBFBFRRL",
    "BFBBBBBRRL",
    "FBBFBFFRLL",
    "FFBFBBBRRR",
    "BBFFFBFLRL",
    "FBBBFBFRRR",
    "FBFFFFFLRL",
    "FFFBBBBRLR",
    "FBFFFFBLRR",
    "FBBFFBBLRL",
    "BFFFBBFRRL",
    "FFFBFBFRRR",
    "BFFBFFFRLL",
    "BFBFBFFLLR",
    "BFFBFBFRLL",
    "FFBFFBBLRR",
    "BFBBBBBLLR",
    "FBBBFFBRRL",
    "FFBBBFFRLL",
    "BFFBFBFLLR",
    "FFBBBBFRLL",
    "BFBFFFBRLR",
    "FBFFFFBLRL",
    "FFFBBFBRLR",
    "FFFBBFFLLR",
    "BFBBBBFLRR",
    "FFBFBFFRRR",
    "BFFBBBBRLR",
    "FBFFFFFRRL",
    "BFFFFFBRLL",
    "FFBBBBFLRL",
    "BFFFBFBRRL",
    "FFBFBFFLRL",
    "FFFBFFBLLR",
    "FBBBBFBRRL",
    "FFFFBBFLLR",
    "BFBFFBFRLR",
    "FBFFBFBRLL",
    "BFBBFBFLRL",
    "FBBFBBFLLL",
    "BFFFFFFRLL",
    "FBBBBBBRLR",
    "BFFFFBBRLL",
    "FBFBBFFLRL",
    "FBFFBBFLLR",
    "FBFBFBBLLL",
    "FFBBBFBLRL",
    "FFBBBBFRRR",
    "FFFFBBBLRL",
    "BFBBBBFRLR",
    "BFBFBBFLRR",
    "FFFBBFFRRL",
    "FFFBBFFRRR",
    "FBBBBFBRRR",
    "FFBBBBBRLL",
    "FBBBFFBRLL",
    "FBFBBFBLRR",
    "BFFFBBBRRR",
    "BFFBBBBLLR",
    "BFFFFBFRLR",
    "FFBFFFFLRR",
    "BFBBBFBLRR",
    "FBFFFBBRLR",
    "FFBFFBFLRR",
    "FFFBFBBLLL",
    "BFFBFFBRLL",
    "FBFFFBFLRR",
    "FBBBFBFLLL",
    "FBBFFBFLRR",
    "FFBFBFBRLR",
    "FFBBBBBRRR",
    "BFFBFBBRRL",
    "BFBFFBBRRR",
    "BFFBBFBLRR",
    "FBBFFFBRLL",
    "FBBBBFFLLL",
    "FBBBBBFLRR",
    "FBFFBBBLLL",
    "BFFBFFBLRR",
    "BBFFFFBRRR",
    "FBFFFBBLLL",
    "FFFFBFBRRL",
    "FBBFBBBRLR",
    "FBFBFBFRLR",
    "FBFFBFFRRR",
    "BBFFFBFRLL",
    "BFBBBFFRLR",
    "FBBFFFFRRL",
    "BBFFFFFLLL",
    "FBBFFFBRLR",
    "FFBFBFFRLR",
    "BFBFBBFRRL",
    "BFBBBBFLLR",
    "BFFFBBFLRR",
    "FBFBFBBLRR",
    "FBBFFFBLRR",
    "BFBFFBFLLR",
    "BFBFBFBRRL",
    "FBFBFFBLLR",
    "FBBFBFBLRL",
    "BFBFFFFRLR",
    "BFFBBFBLLR",
    "BFBBFBBRLL",
    "BFBFBFFRRR",
    "FFBBFBBLLR",
    "FFBFBFFLRR",
    "FFFBFFBLRR",
    "BFBFFFFLLR",
    "FBFBFFBRRL",
    "FBFBFFFRRL",
    "FBFFFFBRRR",
    "FFBBFFFRRL",
    "FFBFFBBRLR",
    "BFBBBFFLRR",
    "BBFFBFBRLL",
    "FBBBBBFRRL",
    "BBFFFFBRLL",
    "FFBBBBFLLR",
    "FBBBBFBRLR",
    "FFBFFBFRLR",
    "FFFFBFBRLR",
    "FBBFBFBLRR",
    "BFBBFBFLLR",
    "FFBFBBFRRR",
    "FFBBFBFRRR",
    "FFBBBBBLLR",
    "BFBBFFBLRL",
    "BFFBBFFRLR",
    "FFFBBFBRRL",
    "BFFFFFBRRL",
    "BFBBFFBRRL",
    "BFFBFBBLLR",
    "FBBFFFBRRR",
    "FBBBFFFLLR",
    "BFFFFFFRLR",
    "FBBFFFFLRL",
    "BFFFBBBLLR",
    "BFFFBFBLLR",
    "BFFFBFBLLL",
    "FFFBFBFLRL",
    "FBFBBBBRLR",
    "FBFFFFFRLL",
    "BFFBFFBLLL",
    "FFBBFBBLLL",
    "FBFFBFFRLL",
    "FBFFBFBLLR",
    "FFBBFBBLRR",
    "FFBFFFFLLR",
    "FBBFBFBRLR",
    "FFBBBFBRRL",
    "FBFBBFBRLL",
    "FBFFBFFLLR",
    "BFFBFBFRRR",
    "FBBFBBBLLR",
    "BFBBFFBRLR",
    "BFFBBFBRRR",
    "FBBBBFFLRR",
    "BBFFFFFLRR",
    "FBFFFFFRRR",
    "FFBBFFFLLR",
    "FFBFFBBRRL",
    "FBBFBBFRRL",
    "BFFFFFBLLL",
    "FFFBBBFLLL",
    "FBBBBFBLRR",
    "FFFBBFFLRL",
    "BFBBBFBLRL",
    "FBBFBBFLRL",
    "FBBFFBBRRR",
    "FFBFBBFRLL",
    "FBFFFFFLLL",
    "FFFBBBFRLL",
    "BFBBFBBRRR",
    "FFFBBFBRLL",
    "FFBBBFBRLL",
    "FBBBBBBLRR",
    "FBFBBBBRLL",
    "FFBBFFFRRR",
    "FFFBFFBLRL",
    "FBBFBFFRLR",
    "BFFFBFFRRR",
    "BFFFBFFRLL",
    "FBBBFFFRLR",
    "FFBBFBBRRL",
    "FFBBFFFRLL",
    "FFBBFBFRLL",
    "FBBFFBFLLL",
    "FBFFBBBRRL",
    "FBFBFFBRRR",
    "FFBFBFFRLL",
    "FFFBFFFRRR",
    "FFBFFFBLRR",
    "FFBFFFFRLL",
    "FBFFFFBLLL",
    "BFBBFFFLLR",
    "BFBFBFBLRR",
    "FBBFFFFLLR",
    "FBBBBFBLLR",
    "FBBBFBFRRL",
    "BFBBBBBRLR",
    "FBFFBFBLLL",
    "FFBBFFFLLL",
    "FFFFBBFRRR",
    "FBFBBBFLRR",
    "BBFFBBFLLL",
    "FFBBBFBLLR",
    "FBBFFFFLRR",
    "FBBFBFBLLR",
    "FFBFFFBLRL",
    "FBFBBBFLLR",
    "BFBBBFFLLR",
    "BFFFFBBRLR",
    "FBBFBFBLLL",
    "FBBFFBFRLR",
    "BFBBFFBRLL",
    "FBBBBFFLLR",
    "BFFBBBBLRL",
    "FBBFBFBRRL",
    "FBBFFBFLRL",
    "FBBBFFFRRL",
    "BFBFBFFLRL",
    "BFBFFFFLRR",
    "BBFFBFBLLL",
    "BBFFBFFLLR",
    "FBFBBFFRLL",
    "BFFBBBFLLR",
    "FFBFBBFRRL",
    "FBFFBBBLRR",
    "FBBBFBBLLR",
    "FBFFFBBRRL",
    "FFBBBBFLRR",
    "BFBFFBFLRR",
    "FFFBBBFLRL",
    "FBFFBFFRRL",
    "FBBFBFFLRL",
    "FBBFFFBLRL",
    "FFBBBFFRRR",
    "BBFFFBFLLL",
    "FBFFBFBLRR",
    "BBFFBFBLLR",
    "FBFFFFBRLR",
    "BFFFFFFLRL",
    "FBBFBBBLLL",
    "BFBFFBBLRR",
    "FFBBFFBRRL",
    "BFFFBFBLRL",
    "BFBBBBBRLL",
    "FBFFFBBLRR",
    "BFBBFBBLLR",
    "FBBBFFBLLL",
    "FBFFFBFRLR",
    "FFBBBFFRRL",
    "FFBFBBFLRL",
    "FFBFBFBLLR",
    "FBBFFBFRLL",
    "FFBBBFFLLL",
    "BFBBBBBLLL",
    "FBBFFFBLLL",
    "BFBFFFBLRR",
    "FFBFFBFLRL",
    "BFFFBBBRRL",
    "BFBFBBBLLR",
    "BFBFFFFLRL",
    "BFBFBFFRLR",
    "FBBFBBBRLL",
    "FFBFBBBLRL",
    "FBBBFFFRRR",
    "FBBFBFFRRR",
    "FFFFBBBRLL",
    "FBFFBBBLRL",
    "FBBBFBBRRL",
    "FBFFBBBLLR",
    "FFFBBBFRLR",
    "BFBFBFBLLL",
    "BBFFFFFRRR",
    "BFBBFBFRLL",
    "FBBBFBBLRR",
    "BFFFFBFLRL",
    "FBBBFFBLRL",
    "BBFFBFFLRR",
    "FFBFBFFRRL",
    "FBFFFBBLRL",
    "FFFFBBFRLL",
    "FFBFFFBLLR",
    "FBBBFBFLRR",
    "FFFBFFBRRR",
    "BFFBBBFLRR",
    "FBFFBFBLRL",
    "FFBFFFBRLR",
    "FFBFFFBRRL",
    "FFBBFFBLRL",
    "FBFBFBBRLR",
    "FFFBBBBLLL",
    "BFBBBFFLLL",
    "FFBBFBFLRL",
    "BFBFFFBRLL",
    "BFFBFFBRRL",
    "FBBFFFFLLL",
    "FBFFFFBRRL",
    "FFFBFFFLLR",
    "FBFFFBFLRL",
    "FFBFBFBLRL",
    "FBBBFFBLRR",
    "BFBFFBBRRL",
    "BBFFFFFLRL",
    "BFFBBBFRRR",
    "BFFFBBFRLR",
    "BFBBBBBLRR",
    "BFFFBFBLRR",
    "FBBBBFFRLL",
    "BFBBFFFLRR",
    "BBFFFBFLRR",
    "FBFFBBFRLL",
    "FBFFFFFLRR",
    "FBBBBBFLLL",
    "FBFBFBBRRR",
    "FBFBBFBLRL",
    "BFBBFFBRRR",
    "BBFFBFFLLL",
    "FBBFBBFLLR",
    "BFFBBFFRLL",
    "FBFBBBBRRL",
    "FBBFBBFRLL",
    "FBBFBBFLRR",
    "FBBFFBBRRL",
    "FFFBBFFLRR",
    "BFBBFBFLRR",
    "BFBFBFFRRL",
    "FFBBFFFRLR",
    "FBFBBBBLRR",
    "BBFFFFBLLL",
    "BBFFFFFRLR",
    "FBFBFFBLRL",
    "FBBFBBBLRR",
    "BFBFFBFRRL",
    "BFFFFFFLRR",
    "FFFBBBFLLR",
    "FBFFBFFLLL",
    "BFFBFFFRLR",
    "FBBFFBFRRR",
    "FFFBFFFRRL",
    "FFFFBBFLLL",
    "BFBFBBFRLL",
    "BFFFFBBLRL",
    "FFFBFBFLLR",
    "FBBBFBFRLR",
    "BFBBBFBLLR",
    "BFFBFBFLRL",
    "BFBFFFBLLL",
    "FFBFFBBLRL",
    "BFBBFFFRRR",
    "FFFBFFBLLL",
    "BBFFFFBLRR",
    "FFBBFBFLLR",
    "FBFBBBBRRR",
    "FBFBBBFLRL",
    "BFFBFFFLLR",
    "FBFBFFFRLL",
    "FBBBBFBLLL",
    "FBBBBBBRRR",
    "FBBBBBFLRL",
    "BFBBFFFRLL",
    "FFFBFFFRLR",
    "FFBFFBBLLR",
    "FFBFBBBRLL",
    "BBFFFFFRLL",
    "FFFBFBBRLR",
    "FFBFBBBRLR",
    "BFFFFBFLRR",
    "BBFFFBBLRL",
    "FBBBBFFRRL",
    "FBBFBBBRRR",
    "BFBFFFFRLL",
    "FBBBBBBRRL",
    "BFFBFFBLRL",
    "BFFBBFBRRL",
    "FBFFFBBRRR",
    "BFFBBFBLLL",
    "BFBFBFBRLL",
    "BBFFFBBRLL",
    "FBFBBBBLLL",
    "BBFFFBBLRR",
    "BFFFFBFRRL",
    "BFBBFBFLLL",
    "FBBBFBBRLR",
    "BFBBFBBLRL",
    "BFBBBFBRRL",
    "FBFFBBBRLL",
    "FBBBFBBRLL",
    "FFBBBBBRRL",
    "FBFBBBFRLL",
    "BFFFFFBLLR",
    "BFFBBBBRRR",
    "BFBBFBBLLL",
    "FFBFBBBLRR",
    "FFBFBFBRRR",
    "BFBFFFBRRL",
    "FBBBFFBRRR",
    "BFBFBBBLLL",
    "BBFFFBBRLR",
    "BBFFFBBRRL",
    "FBBBBFBLRL",
    "FBBBBFFRRR",
    "FBBBFFBLLR",
    "BFFFFBFLLL",
    "BFBFBFFLLL",
    "BFFFFBFRLL",
    "BFFBFBBLRL",
    "FFBFFBBRLL",
    "FBFBBFFRLR",
    "BFBFFFBRRR",
    "FBFFBFBRLR",
    "FBBFBFFLLL",
    "FBFFBBFLRR",
    "FFBFBFBLRR",
    "FFBBFFBRRR",
    "FBBFFFBLLR",
    "FBFFFBFRRR",
    "BFBFFFFRRL",
    "FBBBBBFRRR",
    "FFFFBFBRRR",
    "FFBBBBBLRL",
    "FBFBFFFLRR",
    "FBBBFFFLLL",
    "BFFFBFFRLR",
    "FFBFFBFRRL",
    "FBFBFFFRRR",
    "FFBFBFBLLL",
    "BFBBBFFRRL",
    "BFBFBFBLRL",
    "BFFFBFFLRL",
    "FBBBBBFRLR",
    "FBFBBFBLLL",
    "FFFBBBBLRL",
    "FBBFBFFLRR",
    "BFBBBFBRRR",
    "FBBBFBBRRR",
    "FFFBFBFRLL",
    "FFBBBBFLLL",
    "FBFFBFFRLR",
    "FBFBFBFLLL",
    "FBFFFFBRLL",
    "FBBBBBBRLL",
    "FBBBBBFRLL",
    "FBBFFBFLLR",
    "BFFBBBFRRL",
    "FBFFFBFLLL",
    "FBBBFFFRLL",
    "BFFFBBBRLR",
    "FBFBBBFRRR",
    "BFFBFBBRLL",
    "FBBFFFBRRL",
    "FBFFBBBRLR",
    "BFBFFBBLRL",
    "BFFBBFFLRL",
    "FBFBBBFRLR",
    "BBFFFBBLLR",
    "FFFBFFBRLL",
    "BFBFBBFLLL",
    "BFFBBFBLRL",
    "FFFBBFBLRL",
    "BFBBBFFRRR",
    "FBFBFFFRLR",
    "BFFBBFFLRR",
    "BFFBBBFLLL",
    "FBFFBBBRRR",
    "FBFBFFFLLL",
    "FFBFBBFLLL",
    "FBFFFFFLLR",
    "BFBBFBFRRL",
    "BFBBBBBRRR",
    "BFFBFBBLLL",
    "BFFFBFBRRR",
    "FFFBFBFLLL",
    "FFBFFFBRLL",
    "FBBFBFBRRR",
    "FBBBBBBLLL",
    "FBFBFFFLRL",
    "FFFBFFBRRL",
    "FBFBBFFRRR",
    "FFBBFBFRLR",
    "BFFFFBBLLL",
    "FBBFBFFRRL",
    "BFFBFFFRRR",
    "BFFBFFFLRL",
    "BFBBBBFRRR",
    "BFBFBBBRRL",
    "FFFBBFBLLL",
    "FBBFFBBRLL",
    "BFBBBFFRLL",
    "BFFFBBFRRR",
    "FBFBFBBRLL",
    "BFFFBFFRRL",
    "FFFBFBBLRL",
    "FBFFFBBLLR",
    "BFFFBBFLLL",
    "BFFBFFFLLL",
    "BFFBBBBLLL",
    "BFFFFFFRRR",
    "FFBFFBFRLL",
    "FBBFFBFRRL",
    "BBFFFFFRRL",
    "FFFBBFBLRR",
    "BFBFFBFLLL",
    "FBFBBFBRLR",
    "BFBBFBBLRR",
    "FBFFBFFLRL",
    "BFBFFFBLLR",
    "FFFBBBFRRR",
    "FFBBBFFLRR",
    "FBFBFFBLLL",
    "BFBFBBFRLR",
    "FBFBFBFRRR",
    "FFBBFBBRRR",
    "FBBFFFFRLR",
    "FBFBFBBLRL",
    "FBBFFFFRRR",
    "FFBBFFBRLR",
    "BFBFBBFLLR",
    "BFFBFBFRLR",
    "BBFFBFFRLL",
    "BFFBBFFRRR",
    "BFFFFBFRRR",
    "FBFBFBFLRL",
    "FFBFFBFRRR",
    "FBBFBBBLRL",
    "FFFBBBFRRL",
    "FBFFBFFLRR",
    "FFBFBBFRLR",
    "BBFFBFBRRL",
    "FBFFBBFLRL",
    "FFFFBBFRRL",
    "BFBFFBFRLL",
    "BFBBFBBRRL",
    "FFFBBFBLLR",
    "FFBFFBFLLL",
    "FFBBBBBRLR",
    "BFFFFFBLRR",
    "BFFBBBFLRL",
    "BFBBFFBLLR",
    "FBFFFFFRLR",
    "FFFFBBFRLR",
    "FBFFFBFRRL",
    "BFFBBBBRRL",
    "FFBFFFFLRL",
    "BFBBFFFRRL",
    "FFFBBBBRLL",
    "BFBFBBBRRR",
    "BBFFFBFRLR",
    "BFFBFFBLLR",
    "FBFBBFBLLR",
    "BFFBFBBRRR",
    "BBFFFBFRRR",
    "BFFBBFFRRL",
    "FBBBFBFRLL",
    "FFBFFFBLLL",
    "BFFBBBFRLL",
    "FBFFBBFRRR",
    "FFFBFBFLRR",
    "BFFBFBBLRR",
    "FBFFBBFRLR",
    "FFFBFBFRRL",
    "FFFBBBBRRL",
    "BFBFFBBLLR",
    "BFBFFFFRRR",
    "FFBBBFFLRL",
    "FBBFBBFRLR",
    "FFFBFFFLRL",
    "BFFBBBBRLL",
    "BFBBFFFRLR",
    "FFBFFBBRRR",
    "FBFBFFBRLL",
    "BFFFBFFLLL",
    "FFBFBFBRRL",
    "FFFBFBBRRL",
    "BFBBBBFLRL",
    "BBFFBFFRLR",
    "BFFFBBFRLL",
    "BFFFBBBLRR",
    "BFBFFBFRRR",
    "FBBBFBFLLR",
    "BFBBFFFLRL",
    "FFFBFBFRLR",
    "FBFBFBFLRR",
    "BBFFBFBRRR",
    "BBFFFBBRRR",
    "FFBBFFBLLL",
    "BFBBBFBLLL",
    "FFBBFFFLRL",
    "FFFBFBBRRR",
    "FFBBBFBRLR",
    "FFBBFBBRLR"
]

testSeatingInstructions = [
    "FBFBBFFRLR",
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"
]
############################Part 1##################################
assert(820 == findMaxSeatId(testSeatingInstructions))

print(findMaxSeatId(inputSeatingInstructions))
############################Part 2##################################
print(findMissingSeatId(inputSeatingInstructions))
