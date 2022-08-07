class EmailYahoo extends Email(string address) {
  this.value = address + "@yahoo.com"
}


class AccountYahoo extends Account {
  @override
  fun createName(string name): Name {
    return new Name(name)
  }

  @override
  fun createEmail(string address): Email {
    return new EmailYahoo(address)
  }
}
