# bootcamp_haoting_lan
# Consumer Loan Default Risk Prediction

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Consumer lenders face financial losses when borrowers fail to repay their loans, but manually reviewing every borrower in depth can be costly and inefficient. This project will examine whether historical borrower and loan characteristics can be used to estimate the probability that a borrower will default. The primary stakeholder is a credit risk manager who is responsible for monitoring and managing the lender’s credit exposure, while credit analysts or loan officers would be the main end users of the output. A useful solution should help these users identify higher-risk borrowers before or during the lending decision process so that they can determine which cases may require additional review.

The project will use a **predictive** framework rather than a causal one. The main output will be an estimated probability of default for each borrower, which can also be used to rank borrowers by relative risk. Model performance can be evaluated using metrics such as ROC-AUC and recall for default cases, with particular attention to the model’s ability to identify borrowers who are actually likely to default. The final deliverable will be a predictive model and a summary of borrower-level risk scores that can support, rather than fully automate, the lender’s credit review process.

## Stakeholder & User

The primary stakeholder is the **credit risk manager**, whose goal is to control credit losses while maintaining an efficient lending process.

The main end users are **credit analysts and loan officers**, who may use the model output when reviewing individual borrowers.

The model would fit into the lending workflow by producing a borrower-level risk score before or during the credit review process. Borrowers with higher estimated default probabilities could be flagged for additional analysis rather than being automatically rejected.

## Useful Answer & Decision

This project is primarily **predictive**.

The main question is:

**Can historical borrower and loan characteristics be used to estimate a borrower’s probability of default?**

The model will produce:

* An estimated probability of default for each borrower.
* A relative risk ranking across borrowers.
* A classification or risk flag based on an appropriate decision threshold.

Potential model evaluation metrics include:

* **ROC-AUC** to evaluate the model’s overall ability to distinguish between defaulting and non-defaulting borrowers.
* **Recall for default cases** to measure how many actual defaults the model successfully identifies.
* **Precision** to evaluate how many borrowers flagged as high risk actually default.

The output should help the credit risk team decide which borrowers may require additional review.

## Assumptions & Constraints

* Historical borrower and loan data will be available for analysis.
* The dataset will contain a clearly defined default or repayment outcome.
* Borrower characteristics used for prediction will be available at or before the time the credit decision is made.
* The dataset may contain missing values that will require cleaning or preprocessing.
* Defaults may represent a relatively small percentage of observations, creating a class imbalance problem.
* Model performance may depend on the quality and representativeness of the available historical data.
* The model is intended to support human credit review rather than independently make lending decisions.
* Sensitive or inappropriate variables should not be used simply because they improve predictive performance.

## Known Unknowns / Risks

* The exact level of class imbalance between default and non-default observations is not yet known.
* Some variables may contain substantial missing data or inconsistent definitions.
* Certain variables may have strong predictive relationships in historical data but may not generalize well to future borrowers.
* The appropriate probability threshold for defining a borrower as “high risk” has not yet been determined.
* There may be a tradeoff between identifying more potential defaults and incorrectly flagging low-risk borrowers.
* The available dataset may not fully represent the population or lending environment in which the model would eventually be used.
* Additional testing will be needed to determine whether model performance is stable across different borrower groups.

## Lifecycle Mapping

Goal → Stage → Deliverable

* Define the lending risk problem and decision context → **Problem Framing & Scoping (Stage 01)** → Project scoping statement.
* Identify the primary stakeholder and end users → **Problem Framing & Scoping (Stage 01)** → Stakeholder context artifact.
* Define what constitutes a useful prediction → **Problem Framing & Scoping (Stage 01)** → Prediction target and evaluation criteria.
* Identify assumptions, constraints, and project risks → **Problem Framing & Scoping (Stage 01)** → Assumptions and known-unknowns documentation.
* Organize the project for future analysis and modeling → **Problem Framing & Scoping (Stage 01)** → GitHub repository and project folder structure.

## Repo Plan

The repository will use the following folder structure:

data/
src/
notebooks/
docs/

* `data/` — Raw and processed datasets used in the project.
* `src/` — Reusable Python code and functions.
* `notebooks/` — Exploratory analysis, data preparation, and modeling notebooks.
* `docs/` — Stakeholder-facing documents and project documentation.
## Data Storage

The project separates data into two main folders:

- `data/raw/` stores raw or minimally modified data.
- `data/processed/` stores processed data that is ready for later analysis.

CSV is used for raw data because it is simple, readable, and widely compatible. Parquet is used for processed data because it is more storage-efficient and preserves data types more reliably.

The storage paths are controlled through environment variables in the local `.env` file:

- `DATA_DIR_RAW=data/raw`
- `DATA_DIR_PROCESSED=data/processed`

The notebook loads these variables using `python-dotenv`. The reusable `write_df()` and `read_df()` functions automatically select CSV or Parquet based on the file extension and create missing directories when necessary.
