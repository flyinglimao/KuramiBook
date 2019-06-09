workflow "Publisher" {
  on = "schedule(0 9 * * 1)"
  resolves = ["./publisher/"]
}

action "./publisher/" {
  uses = "./publisher/"
  secrets = ["GITHUB_TOKEN"]
}
