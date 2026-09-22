# Data Journalism Knowledge

## 1. Question first
Define the journalistic question before selecting variables.

Write:
- question;
- population;
- period;
- comparison;
- expected limitation.

## 2. Acquire
Prefer the primary dataset. Preserve the original file.

Record:
- publisher;
- URL/file;
- retrieval date;
- version;
- coverage;
- licensing/terms where relevant.

## 3. Clean transparently
Check:
- encoding;
- delimiter;
- data types;
- missing versus zero;
- duplicates;
- inconsistent names;
- units;
- date formats;
- outliers.

Never delete an outlier simply because it weakens a story.

## 4. Analyze
Explicitly distinguish:
- count vs rate;
- numerator vs denominator;
- mean vs median;
- nominal vs inflation-adjusted values;
- level vs percentage change;
- correlation vs causation.

For time series, compare like periods when seasonality matters.

## 5. Statistical caution
Report uncertainty when relevant:
- sample size;
- margin of error;
- confidence interval;
- model assumptions;
- missingness;
- selection bias;
- measurement changes.

Do not treat a statistical association as proof of causation.

## 6. Visualization
A chart should answer a question.

Avoid:
- distorted axes;
- unexplained baselines;
- inconsistent scales;
- decorative 3D;
- color that encodes meaning without a legend;
- cherry-picked time windows.

## 7. Data mining
The data-mining references support structured discovery, preprocessing, pattern detection and model evaluation.

In journalism, a model output is a lead or analytical aid unless its validity has been independently established.

Use:
`data → preprocessing → exploratory analysis → model/algorithm → validation → interpretation → editorial verification`.

Do not turn a classification model into a factual claim about an individual without independent evidence.

## 8. Reproducibility
Keep:
- original dataset;
- cleaned dataset;
- code;
- dependency/version information;
- transformations;
- variable dictionary;
- output;
- publication snapshot.

## Source map
- S01–S02 — data journalism workflow and storytelling.
- S41 — data preprocessing and mining.
- S43 — data mining process and model evaluation.
- S18 — scientific evidence and uncertainty.
