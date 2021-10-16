# a file with initialization of constants that're used in all files
from os import execlp
from bases import conn,cur,id

class User:
    
    def __init__(self, vk, discord) -> None:
        self.vk = vk
        self.discord = discord
        self.id = id()
    def __init__(self,vk,discord,nickname) -> None:
        self.vk = vk
        self.discord = discord
        self.nickname = nickname
        self.id = id()
    
    def save(self):
        global cur
        global conn
        if User.objects.permission(self.vk, self.discord):
            try:
                cur.execute("""INSERT INTO whitelist
                            (id, vk, discord, nickname)
                            VALUES
                            (?,?,?,?);
                            """,(self.id, self.vk, self.discord, self.nickname))
            except:
                cur.execute("""UPDATE whitelist SET vk =?, discord=?,nickname=?  where id = ?""",
                    (self.vk,self.discord,self.nickname,self.id)
                )
            conn.commit() 
        else:
            print("You are in black list")
           
    def __str__(self):
        return self.nickname + ':' + str(self.id)  
    def __repr__(self) -> str:
        return self.__str__() 
    
    class objects():
        # class of operations for combining a class and a database
        def permission_vk(vk):
            cur.execute("select * from blacklist_vk where vk = ?",(vk,))
            return len(cur.fetchall())==0
        def permission_dis(discord):
            cur.execute("select * from blacklist_dis where discord = ?",(discord,))
            return len(cur.fetchall())==0
        def permission(vk,discord):
            return User.objects.permission_vk(vk) and User.objects.permission_dis(discord)

        def all_vk_blacklist():
            _all = []
            cur.execute('select * from blacklist_vk') 
            for _i in cur.fetchall():
                _all.append(_i)
            return _all
        def all_dis_blacklist():
            _all = []
            cur.execute('select * from blacklist_dis') 
            for _i in cur.fetchall():
                _all.append(_i)
            return _all
        def all_blacklists():
            vk_black = User.objects.all_vk_blacklist()
            dis_black =User.objects.all_dis_blacklist()
            return {'vk' : vk_black, 'discord' : dis_black}


        def all():
            # getting all lines
            cur.execute('select * from whitelist') 
            _all = []

            # creating an instance of a class for each line
            # and appending it to list that will be return
            for _i in cur.fetchall():
                u = User(vk = _i[1], discord=_i[2],nickname = _i[3])
                u.id = _i[0]
                _all.append(u)
            return _all
        def get(id: int):
            # creating an instance of a class from data 
            # and return it
            try:
                us = cur.execute('select * from whitelist where id=?', str(id)).fetchone()
                u = User(vk = us[1], discord=us[2], nickname = us[3])
                u.id = us[0]
                return u
            except:
                return None
        

        def delete(id: int):
            cur.execute("""DELETE from whitelist where id = ?""",(id,) )
            conn.commit()


        def create(vk: str, discord: str, nickname: str):
            if User.objects.permission(vk,discord):
                u = User(vk,discord,nickname)
                u.save()
            else:
                u = None
            return u


        def move_vk_to_black_list(vk):
            cur.execute("""DELETE from whitelist where vk = ?""",(vk,) )
            try:
                cur.execute("""INSERT INTO blacklist_vk
                            (vk)
                            VALUES
                            (?);
                            """, (vk,))
            except:
                pass
            conn.commit() 
        def move_dis_to_black_list(discord):
            cur.execute("""DELETE from whitelist where discord = ?""",(discord,) )
            try:
                cur.execute("""INSERT INTO blacklist_dis
                            (discord)
                            VALUES
                            (?);
                            """, (discord,))
            except:
                pass
            conn.commit() 


        def remove_vk_from_black_list(vk):
            cur.execute("""DELETE from blacklist_vk where vk = ?""",(vk,) )
            conn.commit()        
        def remove_dis_from_black_list(discord):
            cur.execute("""DELETE from blacklist_discord where discord = ?""",(discord,) )
            conn.commit() 
