SUMMARY_PROMPT_V1 = "Summarize this:"

SUMMARY_SYSTEM_V2 = """You are an assistant to a microfinance loan officer.
Summarize loan applications in a factual and neutral way.
Do not invent or assume any information that is not stated in the application.
Keep the summary to 3-4 sentences."""

SUMMARY_PROMPT_V2 = "Summarize this loan application:\n\n"

EXTRACT_PROMPT = """
Extract information from the loan application below.

Return ONLY a valid JSON object with EXACTLY these six keys:

{
  "applicant_name": "string",
  "amount_ghs": "number or null",
  "purpose": "string",
  "monthly_profit_ghs": "number or null",
  "has_collateral_or_guarantor": "boolean",
  "repayment_months": "number or null"
}

Rules:
- Use only information explicitly stated in the letter.
- If a field is not stated, use null.
- Do not guess or infer missing information.
- amount_ghs, monthly_profit_ghs, and repayment_months must be numbers.
- has_collateral_or_guarantor must be true or false.
- Return ONLY the JSON object.

Example:

Loan application:
"My name is Ama Mensah. I run a small bakery and request GHS 6,000
to buy an oven. My monthly profit is GHS 700. My brother will
guarantee the loan. I will repay it over 10 months."

JSON:
{
  "applicant_name": "Ama Mensah",
  "amount_ghs": 6000,
  "purpose": "buy an oven",
  "monthly_profit_ghs": 700,
  "has_collateral_or_guarantor": true,
  "repayment_months": 10
}

Loan application:
{letter_text}
"""

BRIEF_PROMPT = """
You are an assistant supporting a microfinance loan officer.

Using the loan application and extracted information below, prepare
a decision-support brief.

Include exactly these sections:

1. Strengths
- List strengths supported by the application.

2. Risks / Red Flags
- List risks or concerns supported by the application.

3. Missing Information
- Identify information or documents the loan officer should request.

4. Suggested Next Step
- Suggest an appropriate next step such as requesting documents,
  inviting the applicant for an interview, or flagging the application
  for senior review.

Important:
- Base your response only on information provided.
- Do not invent facts.
- Do not make assumptions about the applicant.
- The system supports the loan officer but does not make the final decision.
- Do NOT say "approve" or "reject".
- Final loan decisions must be made by a human.

Loan application:
{letter_text}

Extracted information:
{extracted_json}
"""
