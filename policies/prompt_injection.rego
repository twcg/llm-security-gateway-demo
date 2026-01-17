package main

deny[msg] {
  t := lower(input.request_text)
  regex.match(".*ignore all previous instructions.*", t)
  msg := "DENY: prompt-injection pattern (ignore instructions)"
}

deny[msg] {
  t := lower(input.request_text)
  regex.match(".*system prompt.*", t)
  msg := "DENY: prompt-injection pattern (system prompt)"
}

deny[msg] {
  t := lower(input.request_text)
  regex.match(".*developer message.*", t)
  msg := "DENY: prompt-injection pattern (developer message)"
}

deny[msg] {
  t := lower(input.request_text)
  regex.match(".*bypass.*(policy|guardrail|rules).*", t)
  msg := "DENY: prompt-injection pattern (bypass guardrails)"
}
