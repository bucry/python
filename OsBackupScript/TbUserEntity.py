class tbUser():
    def initTbUser(self, sid, uid, did, passwd, isSys, isUpdatePass, nickname, username):
        self.sid = sid
        self.uid = uid
        self.did = did
        self.passwd = passwd
        self.isSync = isSys
        self.isUpdatePass = isUpdatePass
        self.nickname = nickname
        self.username = username
