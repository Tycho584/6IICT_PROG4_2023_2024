naam  = "NAAM OPGEGEVEN TIJDENS LOGIN"
query = f"SELECT * FROM account_tabel WHERE naam='{naam}'"
account = sqlite3.executequery(query)