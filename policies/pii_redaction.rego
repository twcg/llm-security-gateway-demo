package main

deny[msg] {
  t := lower(input.request_text)
  regex.match(".*\\bssn\\b.*", t)
  msg := "DENY: request asks for SSN"
}

deny[msg] {
  t := lower(input.request_text)
  regex.match(".*\\bdate of birth\\b.*", t)
  msg := "DENY: request asks for date of birth"
}

deny[msg] {
  t := lower(input.request_text)
  regex.match(".*\\bdob\\b.*", t)
  msg := "DENY: request asks for DOB"
}
